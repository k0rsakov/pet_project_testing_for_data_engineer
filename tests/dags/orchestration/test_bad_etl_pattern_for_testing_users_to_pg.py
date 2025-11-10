import pytest
from airflow.models import DagBag
from airflow.operators.python import PythonOperator


class TestBadEtlPatternDAG:
    DAG_ID = "bad_etl_pattern_for_testing_users_to_pg"

    @pytest.fixture(scope="class")
    def dag_fixture(self):
        bag = DagBag(dag_folder="dags/orchestration", include_examples=False)
        dag = bag.get_dag(self.DAG_ID)
        assert dag is not None, f"DAG {self.DAG_ID} не найден"
        assert bag.import_errors == {}
        return dag

    def test_dag_loaded(self, dag_fixture):
        assert dag_fixture.dag_id == self.DAG_ID

    def test_task_count(self, dag_fixture):
        assert len(dag_fixture.tasks) == 3

    def test_task_ids(self, dag_fixture):
        assert set(dag_fixture.task_ids) == {"start", "etl_load_user_to_pg", "end"}

    def test_etl_task_type(self, dag_fixture):
        task = dag_fixture.get_task("etl_load_user_to_pg")
        assert isinstance(task, PythonOperator)

    def test_dependencies(self, dag_fixture):
        start = dag_fixture.get_task("start")
        etl = dag_fixture.get_task("etl_load_user_to_pg")
        end = dag_fixture.get_task("end")
        # Проверяем направленную цепочку
        assert etl in start.downstream_list
        assert end in etl.downstream_list
        assert start in etl.upstream_list or not start.upstream_list  # start может быть первым
        assert etl in end.upstream_list

    @pytest.mark.parametrize("task_id", ["start", "etl_load_user_to_pg", "end"])
    def test_task_exists(self, dag_fixture, task_id):
        assert dag_fixture.has_task(task_id)
