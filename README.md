\# DemandForecastX



End-to-end demand forecasting pipeline with automated training, logging, and monitoring.



\## Overview



\- Cleans 800K+ rows of sales data → builds features → trains LightGBM model  

\- Logs RMSE, MAE, R² to MLflow  

\- Exposes metrics via `/metrics` endpoint  

\- Prometheus scrapes metrics → Grafana dashboards visualize trends  

\- Alert rules fire if RMSE spikes or model fails  



\## Stack



Python · LightGBM · Prefect · MLflow · Prometheus · Grafana · Docker



\## Setup



```bash

git clone https://github.com/SharathVellanki/DemandForecastX.git

cd DemandForecastX

python -m venv venv \&\& venv\\Scripts\\activate

pip install -r requirements.txt

mkdir mlruns

echo. > mlflow.db

docker compose up --build



