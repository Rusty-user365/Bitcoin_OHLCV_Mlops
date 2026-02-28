
# Bitcoin_OHLCV_Mlops
---
## 📌 Overview
# MLOps Task: Trading Signal Pipeline

A minimal, reproducible MLOps batch job that calculates a rolling mean on OHLCV data, generates a binary trading signal, and outputs strictly structured metrics.

## Local Run Instructions


## ⚙️ Project Structure
```
├── run.py              # Main entry point
├── config.yaml         # Configuration file (seed, window, version)
├── data.csv            # Dataset (OHLCV, 15,1226 rows)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Containerization setup
├── README.md           # Documentation
├── metrics.json        # Sample metrics output
└── run.log             # Sample log output
```

---

## Local Setup Instructions(using Git Bash)

### 1.Clone the repo
```bash
git clone https://github.com/Rusty-user365/Bitcoin_OHLCV_Mlops.git

```
### 2.Change the directory to 
```bash
cd  ./Bitcoin_OHLCV_Mlops
```
### 3.Open Vscode 
```bash
code .
```
### 4.Open Terminal (Inside Vscode)
```bash
Ctrl+`
```



---

## Local Run Instructions(Powershell of Vscode)

### 1.Create the environment
```bash
conda env create -f environment.yml 

```
### 2.Activate the environment
```bash
conda activate mlops_env
```

### 3. Run the program
```bash
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

### 4. Expected output
- **metrics.json** → structured metrics (success or error)  
- **run.log** → detailed logs of execution steps  

---

## 🐳 Docker Run Instructions

###1. Login with Docker(Optional if already done)
```bash
 docker login
```

### 2. Pull the image
```bash
docker pull anxious01/mlops-task:latest
```

### 3. Run the container
```bash
docker run --rm anxious01/mlops-task:latest
```

### 4. Behavior
- Container includes `data.csv` and `config.yaml`  
- Produces `metrics.json` and `run.log`  
- Prints final metrics JSON to stdout  
- Exit code: `0` on success, non-zero on failure  

---

## 📊 Example Metrics Output
```json
{
    "version": "v1",
    "rows_processed": 151226,
    "metric": "signal_rate",
    "value": 0.5087,
    "latency_ms": 211,
    "seed": 42,
    "status": "success"
}
```

---

## 📝 Log Sample 

The job generates a detailed execution trace in `run.log`. Below is a sample from a successful run:

```log
2026-02-26 11:35:11,726 - INFO - Job started [cite: 73]
2026-02-26 11:35:11,726 - INFO - Config loaded and validated. version=v1, seed=42, window=5 [cite: 74]
2026-02-26 11:35:14,404 - INFO - Rows loaded: 3334058 [cite: 74]
2026-02-26 11:35:14,404 - INFO - Computing rolling mean... [cite: 76]
2026-02-26 11:35:14,497 - INFO - Generating signals... [cite: 76]
2026-02-26 11:35:14,512 - INFO - Metrics summary: {"version": "v1", "rows_processed": 3334058, "metric": "signal_rate", "value": 0.5015, "latency_ms": 2789, "seed": 42, "status": "success"} [cite: 77]
2026-02-26 11:35:14,512 - INFO - Job ended successfully [cite: 78]
```
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



---
