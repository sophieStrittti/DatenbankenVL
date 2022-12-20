from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from random import randint

def _training_model():
    print("Ich bin die Training Model Funktion")
    return randint(1,10)

def _choose_best_model(ti):
    accuracies = ti.xcom.pull(task_id = ['training_model_A', 'training_model_B', 'training_model_C'])
    
    for i in accuracies:
        print(i)
        
    best_accuracy = max(accuracies)
    if best_accuracy > 5:
        return 'accurate'
    else:
        return 'inaccurate'

with DAG("tif20DAG", start_date=datetime(2022, 12, 13),schedule_interval="@daily", catchup=False) as dag:
    training_model_A = PythonOperator(
        task_id = "training_model_A",
        python_callable = _training_model
    )
    
    training_model_B = PythonOperator(
        task_id = "training_model_B",
        python_callable = _training_model
    )
    
    training_model_C = PythonOperator(
        task_id = "training_model_C",
        python_callable = _training_model
    )
    
    choose_best_model = BranchPythonOperator(
        task_id = "choose_best_model",
        python_callable = _choose_best_model
    )
    
    accurate = BashOperator(
        task_id = 'accurate',
        bash_command = 'echo xxxxxxxxx ist akkurat'
    )
    
    inaccurate = BashOperator(
        task_id = 'inaccurate',
        bash_command = 'echo xxxxxxxxx ist inakkurat'
    )
    
    [ training_model_A, training_model_B, training_model_C ] >> choose_best_model >> [ accurate, inaccurate ]    
    