from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from ingestion.oecd_ingest import run_ingest
from ingestion.clean_oecd import run_clean
from ingestion.load_clickhouse import run_load


with DAG(
    "oecd_ingest", start_date=datetime(2025, 11, 1), schedule_interval="@daily"
) as dag:
    t1 = PythonOperator(task_id="ingest", python_callable=run_ingest)
    t2 = PythonOperator(task_id="clean", python_callable=run_clean)
    t3 = PythonOperator(task_id="load", python_callable=run_load)
    t1 >> t2 >> t3
