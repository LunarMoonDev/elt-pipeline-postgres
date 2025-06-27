#!/usr/bin/env bash
cd "$(dirname "$0")"

source ./common.sh

# STOPPING AIRFLOW
log_message YELLOW 1 "Stopping Airflow servers"
docker compose -f ../airflow-project/docker-compose.yaml down
log_newline

# STOPPING POSTGRES
log_message GREEN 2 "Stopping Postgres servers"
docker compose -f ../docker-compose.yaml down
log_newline