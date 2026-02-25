import argparse
import logging
import json
import time
import sys
import yaml
import pandas as pd
import numpy as np

def write_error_and_exit(output_path, version, message):
    """Writes the error payload to metrics.json, prints to stdout, and exits with 1."""
    metrics = {
        "version": version,
        "status": "error",
        "error_message": message
    }
    # Write to metrics.json
    with open(output_path, 'w') as f:
        json.dump(metrics, f, indent=4)
    # Print to stdout
    print(json.dumps(metrics, indent=4))
    sys.exit(1)

def main():
    start_time = time.time()
    
    # Required CLI arguments
    parser = argparse.ArgumentParser(description="MLOps Batch Job")
    parser.add_argument('--input', required=True, help="Input CSV file")
    parser.add_argument('--config', required=True, help="Input YAML config")
    parser.add_argument('--output', required=True, help="Output metrics JSON")
    parser.add_argument('--log-file', required=True, help="Output log file")
    args = parser.parse_args()

    # Configure Logging
    logging.basicConfig(
        filename=args.log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    logging.info("Job started")
    version = "unknown"
    
    try:
        # 1. Load + validate config
        try:
            with open(args.config, 'r') as f:
                config = yaml.safe_load(f)
        except Exception as e:
            raise ValueError(f"Failed to load config file: {e}")
            
        if not isinstance(config, dict):
            raise ValueError("Invalid config structure: must be a YAML dictionary")
            
        for k in ['seed', 'window', 'version']:
            if k not in config:
                raise ValueError(f"Missing required config key: {k}")
                
        version = config['version']
        seed = config['seed']
        window = int(config['window'])
        
        logging.info(f"Config loaded and validated. version={version}, seed={seed}, window={window}")
        
        # Ensure reproducibility
        np.random.seed(seed)
        
        # 2. Load + validate dataset
        try:
            df = pd.read_csv(args.input)
        except FileNotFoundError:
            raise ValueError(f"Missing input file: {args.input}")
        except Exception as e:
            raise ValueError(f"Invalid CSV format: {e}")
            
        if df.empty:
            raise ValueError("Empty file: dataset contains no rows")
            
        if 'close' not in df.columns:
            raise ValueError("Missing required column: close")
            
        rows_loaded = len(df)
        logging.info(f"Rows loaded: {rows_loaded}")
        
        # 3. Processing (Rolling mean)
        logging.info("Computing rolling mean...")
        # Note: First window-1 rows will be NaN.
        df['rolling_mean'] = df['close'].rolling(window=window).mean()
        
        # 4. Signal Generation
        logging.info("Generating signals...")
        # If rolling_mean is NaN, close > NaN evaluates to False, making signal 0. 
        # This keeps handling consistent for the first window-1 rows.
        df['signal'] = (df['close'] > df['rolling_mean']).astype(int)
        
        # 5. Metrics + timing
        rows_processed = len(df)
        signal_rate = float(df['signal'].mean())
        latency_ms = int((time.time() - start_time) * 1000)
        
        metrics = {
            "version": version,
            "rows_processed": rows_processed,
            "metric": "signal_rate",
            "value": round(signal_rate, 4),
            "latency_ms": latency_ms,
            "seed": seed,
            "status": "success"
        }
        
        # Write success metrics
        with open(args.output, 'w') as f:
            json.dump(metrics, f, indent=4)
            
        logging.info(f"Metrics summary: {json.dumps(metrics)}")
        logging.info("Job ended successfully")
        
        # Print final metrics JSON to stdout
        print(json.dumps(metrics, indent=4))
        sys.exit(0)
        
    except Exception as e:
        error_msg = str(e)
        logging.error(f"Validation/Execution error: {error_msg}")
        write_error_and_exit(args.output, version, error_msg)

if __name__ == "__main__":
    main()