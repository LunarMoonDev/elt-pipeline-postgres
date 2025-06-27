import logging
import pendulum

from airflow import DAG
from airflow.sdk import dag, task
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

from config import conf

logger = logging.getLogger(__name__)
default_args = { 'owner': 'airflow' }

@dag(
    dag_id="dbt_daily_increments",
    default_args=default_args,
    schedule="@daily",
    start_date=pendulum.datetime(2025, 6, 24),
    catchup=False,
    tags=['dbt']
)
def dbt_daily_increments() -> DAG:
    """Main flow for running daily increments update with dbt

    Returns:
        DAG: dag pipeline
    """

    @task()
    def pre_dbt_run():
        logger.info("No pre-processing necessary...")
        logger.info("Running Docker command for daily increments...")

    dbt_run = DockerOperator(
        task_id="dbt-increment-run-task",
        image=conf.LOCAL_IMAGE_NAME,
        command="run --select tag:incremental",
        docker_url=conf.DOCKER_URL,
        network_mode=conf.DOCKER_NETWORK,
        auto_remove='force',
        mount_tmp_dir=False,
        mounts=[
            # TODO: need to place these in .env
            # TODO: find a way to grab the absolute value with Path library
            Mount(source=r"C:\Users\Harjit\.dbt", target="/root/.dbt", type="bind"),
            Mount(source=r"C:\Users\Harjit\Documents\Repository\elt-pipeline-postgres\dbt-project", target="/usr/app", type="bind"),
        ],
        tty=True
    )

    @task()
    def post_dbt_run(ti=None):
        logger.info('Docker successfully ran dbt updates for daily increments...')
        logger.info("No post-processing necessary...")


    dbt_test = DockerOperator(
        task_id="dbt-increment-test-task",
        image=conf.LOCAL_IMAGE_NAME,
        command="test --select tag:incremental",
        docker_url=conf.DOCKER_URL,
        network_mode=conf.DOCKER_NETWORK,
        auto_remove='force',
        mount_tmp_dir=False,
        mounts=[
            # TODO: need to place these in .env
            # TODO: find a way to grab the absolute value with Path library
            Mount(source=r"C:\Users\Harjit\.dbt", target="/root/.dbt", type="bind"),
            Mount(source=r"C:\Users\Harjit\Documents\Repository\elt-pipeline-postgres\dbt-project", target="/usr/app", type="bind"),
        ],
        tty=True
    )

    return pre_dbt_run() >> dbt_run >> post_dbt_run() >> dbt_test

_ = dbt_daily_increments()