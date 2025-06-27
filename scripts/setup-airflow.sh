#!/usr/bin/env bash
cd "$(dirname "$0")"

source ./common.sh

# CHECKING OF LOCAL_IMAGE EXISTENCE
log_message YELLOW 2 "Checking existence of LOCAL_IMAGE_NAME"
{ set -x; } 2>/dev/null
if [ "${LOCAL_IMAGE_NAME}" = "" ]; then
    echo -e "$(date '+%Y-%m-%d %H:%M:%S') - LOCAL_IMAGE_NAME has not been set, please run create-docker-image"
    exit 1
fi
{ set +x; } 2>/dev/null
log_newline

# RUNNING AIRFLOW WITH DOCKER
log_message GREEN 3 "Booting up airflow"
{ set -x; } 2>/dev/null
docker compose -f ../airflow-project/docker-compose.yaml up -d
{ set +x; } 2>/dev/null
log_newline