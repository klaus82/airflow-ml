from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from algorithm import test

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2015, 6, 1),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}


dag = DAG('k-means', default_args=default_args, schedule_interval=timedelta(1))

PythonOperator(dag=dag,
               task_id='k-means',
               provide_context=False,
               python_callable=test.my_test
               #op_args=['arguments_passed_to_callable'],
               #op_kwargs={'keyword_argument':'which will be passed to function'}
               )