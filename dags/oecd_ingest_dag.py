from datetime import timedelta
from airflow import DAG


default_args = {
    "owner": "opendatafusion",
    "retries": 2,
    "retry_delay": timedelta(minutes=3),
}

with DAG(
    "oecd_ingest_dag",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=datetime(2025,1,1),
    cat
) as dag:
    ingest_task = PythonOperator(

    )

    ingest_task
