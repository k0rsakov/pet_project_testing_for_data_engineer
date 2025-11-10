import pytest
from airflow.models import DagBag
from airflow.operators.python import PythonOperator

@pytest.fixture(scope="module")
def dagbag():
    # Укажи актуальный путь, если он отличается!
    return DagBag(dag_folder="dags/orchestration", include_examples=False)

def test_dag_loaded(dagbag):
    dag = dagbag.get_dag('bad_etl_pattern_for_testing_users_to_pg')
    assert dag is not None, "DAG не найден"
    assert dagbag.import_errors == {}

def test_task_count(dagbag):
    dag = dagbag.get_dag('bad_etl_pattern_for_testing_users_to_pg')
    assert len(dag.tasks) == 3

def test_task_ids(dagbag):
    dag = dagbag.get_dag('bad_etl_pattern_for_testing_users_to_pg')
    assert set(dag.task_ids) == {'start', 'etl_load_user_to_pg', 'end'}

def test_etl_task_type(dagbag):
    dag = dagbag.get_dag('bad_etl_pattern_for_testing_users_to_pg')
    task = dag.get_task('etl_load_user_to_pg')
    assert isinstance(task, PythonOperator)

def test_dependencies(dagbag):
    dag = dagbag.get_dag('bad_etl_pattern_for_testing_users_to_pg')
    start = dag.get_task('start')
    etl = dag.get_task('etl_load_user_to_pg')
    end = dag.get_task('end')

    # Проверяем зависимости
    assert etl in start.downstream_list
    assert end in etl.downstream_list
    assert start in etl.upstream_list or not start.upstream_list  # start может не иметь апстримов
    assert etl in end.upstream_list

@pytest.mark.parametrize("task_id", ["start", "etl_load_user_to_pg", "end"])
def test_task_exists(dagbag, task_id):
    dag = dagbag.get_dag('bad_etl_pattern_for_testing_users_to_pg')
    assert dag.has_task(task_id)