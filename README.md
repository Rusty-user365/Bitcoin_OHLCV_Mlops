# Bitcoin_OHLCV_Mlops
---

## 📌 Overview
# MLOps Task: Trading Signal Pipeline

A minimal, reproducible MLOps batch job that calculates a rolling mean on OHLCV data, generates a binary trading signal, and outputs strictly structured metrics.

## Local Run Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

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
docker build -t bitcoin-ohlcv-mlops .
```

### 2. Run the container
```bash
docker run --rm -it bitcoin-ohlcv-mlops
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

# Bitcoin_OHLCV_Mlops
---

# ML/MLOps Internship — Task 0 Technical Assessment

## 📌 Overview
# MLOps Task: Trading Signal Pipeline

A minimal, reproducible MLOps batch job that calculates a rolling mean on OHLCV data, generates a binary trading signal, and outputs strictly structured metrics.

## Local Run Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

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
