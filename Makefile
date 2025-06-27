# global variables
LOCAL_TAG:=$(shell date +"%Y-%m-%d")
LOCAL_IMAGE_NAME:=dbt-project:${LOCAL_TAG}

init:
	bash scripts/setup-database-init.sh

set_database:
	bash scripts/boot_database.sh

set_dbt_image:
	bash scripts/create-docker-image.sh

set_airflow:
	LOCAL_IMAGE_NAME=${LOCAL_IMAGE_NAME} bash scripts/setup-airflow.sh

stop_servers:
	bash scripts/stop-servers.sh
