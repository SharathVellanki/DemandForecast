

from prometheus_client import start_http_server, Gauge
import time
import pandas as pd
import os


MAE = Gauge('model_mae', 'Mean Absolute Error')
RMSE = Gauge('model_rmse', 'Root Mean Squared Error')
R2 = Gauge('model_r2', 'R² Score')

def get_latest_metrics():
    try:
        df = pd.read_csv("data/metrics/latest_metrics.csv")  # Path relative to /app in Docker
        return df["mae"].iloc[-1], df["rmse"].iloc[-1], df["r2"].iloc[-1]
    except Exception as e:
        print(f"[Exporter] Error reading metrics: {e}")
        return None, None, None

if __name__ == "__main__":
    start_http_server(8000)
    print("[Exporter] Running on port 8000...")

    while True:
        mae, rmse, r2 = get_latest_metrics()
        if mae is not None:
            MAE.set(mae)
            RMSE.set(rmse)
            R2.set(r2)
            print(f"[Exporter] Updated MAE={mae}, RMSE={rmse}, R2={r2}")
        else:
            print("[Exporter] No metrics found.")
        time.sleep(60)
