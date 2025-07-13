import subprocess, sys
from prefect import flow, task

@task
def clean_data():
    subprocess.run([sys.executable, "src/data/make_dataset.py"], check=True)

@task
def build_features():
    subprocess.run([sys.executable, "src/features/build_features.py"], check=True)

@task
def train_model():
    subprocess.run([sys.executable, "src/models/train_with_mlflow.py"], check=True)

@flow(name="demand-forecast-pipeline")
def main_flow():
    clean_data()
    build_features()
    train_model()

if __name__ == "__main__":
    main_flow()
