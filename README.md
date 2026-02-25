# Bitcoin_OHLCV_Mlops
---

# ML/MLOps Internship — Task 0 Technical Assessment

## 📌 Overview
This project demonstrates a minimal **MLOps-style batch job** in Python.  
It showcases:
- **Reproducibility**: deterministic runs via config + seed  
- **Observability**: structured logs and machine-readable metrics  
- **Deployment readiness**: Dockerized, one-command execution  

The workflow mirrors trading-signal pipelines used in production environments.

---

## ⚙️ Project Structure
```
├── run.py              # Main entry point
├── config.yaml         # Configuration file (seed, window, version)
├── data.csv            # Dataset (OHLCV, 10,000 rows)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Containerization setup
├── README.md           # Documentation
├── metrics.json        # Sample metrics output
└── run.log             # Sample log output
```

---

## 🚀 Local Execution

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the program
```bash
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

### 3. Expected output
- **metrics.json** → structured metrics (success or error)  
- **run.log** → detailed logs of execution steps  

---

## 🐳 Docker Instructions

### 1. Build the image
```bash
docker build -t mlops-task .
```

### 2. Run the container
```bash
docker run --rm mlops-task
```

### 3. Behavior
- Container includes `data.csv` and `config.yaml`  
- Produces `metrics.json` and `run.log`  
- Prints final metrics JSON to stdout  
- Exit code: `0` on success, non-zero on failure  

---

## 📊 Example Metrics Output
```json
{
  "version": "v1",
  "rows_processed": 10000,
  "metric": "signal_rate",
  "value": 0.4990,
  "latency_ms": 127,
  "seed": 42,
  "status": "success"
}
```

---

## 📝 Logging Details
The log file (`run.log`) includes:
- Job start timestamp  
- Config validation (seed, window, version)  
- Rows loaded  
- Processing steps (rolling mean, signal generation)  
- Metrics summary  
- Job end + status  
- Exceptions / validation errors  

---

## ✅ Evaluation Rubric
- **Correctness & determinism (40%)**: signal logic, reproducible results  
- **Dockerization (25%)**: builds + runs cleanly, no hardcoded paths  
- **Code quality (20%)**: clean structure, validation, error handling  
- **Observability (15%)**: meaningful logs + error reporting  

⚠️ **Auto-fail conditions**:
- Docker build/run fails  
- Metrics JSON not written  
- Non-deterministic outputs  
- Hardcoded paths or missing README steps  


