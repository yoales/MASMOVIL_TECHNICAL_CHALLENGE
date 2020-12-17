from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from time_diff import TimeDiff

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

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

with dag:
    timeDiff_task = TimeDiff(task_id='timeDiff_task', diff_date='2020-12-10')

# Una conexión almacena información que permite el acceso a un sistema (ej: hostname, port, login, pass, etc.)
# Un hook es una interfaz a una plataforma externa, utilizando una conexión para obtener información de la plataforma a la que se desea establecer la conexión
# Gracias a los hook podemos abstraer los detalles de autenticación y de conexión a otras plataformas fuera de los pipelines