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

TASK_PREFIX = 'task_'

def getTasks(n):
    task_n = []
    task_ids = list(range(1,n+1))

    for i in task_ids:
        task_id = f'{TASK_PREFIX}{i}'
        task = DummyOperator(
            task_id=task_id,
            dag=dag)
        task_n.append(task)
    return task_n

def getOddTasks(lTask):
    lOddTask = []
    for task in lTask:
        id_task = int(task.task_id.replace(TASK_PREFIX, ""))
        if id_task %2 != 0:
            lOddTask.append(task)
    return lOddTask

def getEvenTasks(lTask):
    lEvenTask = []
    for task in lTask:
        id_task = int(task.task_id.replace(TASK_PREFIX, ""))
        if id_task %2 == 0:
            lEvenTask.append(task)
    return lEvenTask

def getDependList(l_odd, l_even):
    if(len(l_odd) == 1):
        if(len(l_even) == 1):
            return l_even[0] << l_odd[0]
        else:
            task = l_even[0]
            l_even.remove(l_even[0])
            return task << getDependList(l_odd, l_even)
    else:
        task = l_odd[0]
        l_odd.remove(l_odd[0])
        return getDependList(l_odd, l_even) << task

n_task = 5
lTask = getTasks(n_task)
getDependList(getOddTasks(lTask), getEvenTasks(lTask))
