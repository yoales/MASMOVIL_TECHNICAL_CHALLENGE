from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(1900, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds= 5)
}

dag = DAG(
    'test',
    default_args=default_args,
    description='MASMOVIL_TECHNICAL_CHALLENGE DAG',
    schedule_interval='0 3 * * *',
)
