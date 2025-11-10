import pytest
from airflow.models import DagBag
from airflow.operators.python import PythonOperator

class TestGoodEtlPatternDAG:
    DAG_ID = "good_etl_pattern_for_testing_users_to_pg"

    @pytest.fixture(scope="class")
    def t_dag(self):
        bag = DagBag(dag_folder="dags/orchestration", include_examples=False)
        dag = bag.get_dag(self.DAG_ID)
        assert dag is not None, f"DAG {self.DAG_ID} не найден"
        assert bag.import_errors == {}
        return dag

    def test_dag_loaded(self, t_dag):
        assert t_dag.dag_id == self.DAG_ID

    def test_task_count(self, t_dag):
        assert len(t_dag.tasks) == 3

    def test_task_ids(self, t_dag):
        assert set(t_dag.task_ids) == {"start", "etl_load_user_to_pg", "end"}

    def test_etl_task_type(self, t_dag):
        task = t_dag.get_task("etl_load_user_to_pg")
        assert isinstance(task, PythonOperator)

    def test_dependencies(self, t_dag):
        start = t_dag.get_task("start")
        etl = t_dag.get_task("etl_load_user_to_pg")
        end = t_dag.get_task("end")
        # Проверяем направленную цепочку
        assert etl in start.downstream_list
        assert end in etl.downstream_list
        assert start in etl.upstream_list or not start.upstream_list
        assert etl in end.upstream_list

    @pytest.mark.parametrize("task_id", ["start", "etl_load_user_to_pg", "end"])
    def test_task_exists(self, t_dag, task_id):
        assert t_dag.has_task(task_id)