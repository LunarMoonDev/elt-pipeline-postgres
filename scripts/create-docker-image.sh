#!/usr/bin/env bash
cd "$(dirname "$0")"

source ./common.sh

# CREATE DOCKER IMAGE
log_message YELLOW 1 "Creating docker image for dbt app"
{ set -x; } 2>/dev/null
if [ "${LOCAL_IMAGE_NAME}" = "" ]; then
    LOCAL_TAG=$(date +"%Y-%m-%d")
    export LOCAL_IMAGE_NAME="dbt-project:${LOCAL_TAG}"
    echo -e "$(date '+%Y-%m-%d %H:%M:%S') - LOCAL_IMAGE_NAME is not set, building a new image with tag ${LOCAL_IMAGE_NAME}"
    docker build -f ../dbt-project/Dockerfile -t ${LOCAL_IMAGE_NAME} ../dbt-project
else
    echo -e "$(date '+%Y-%m-%d %H:%M:%S') - LOCAL_IMAGE_NAME is already set, using tag ${LOCAL_IMAGE_NAME}"
fi
{ set +x; } 2>/dev/null
log_newline


# SETTING LOCAL_IMAGE_NAME in .env
log_message GREEN 2 "Creating docker image for dbt app"
ENV_FILE="../airflow-project/.env"
if grep -q '^LOCAL_IMAGE_NAME=' "$ENV_FILE"; then
    { set -x; } 2>/dev/null
    sed -i 's/^LOCAL_IMAGE_NAME=.*/LOCAL_IMAGE_NAME='"${LOCAL_IMAGE_NAME}"'/' "$ENV_FILE"
    { set +x; } 2>/dev/null
else
    { set -x; } 2>/dev/null
    echo "LOCAL_IMAGE_NAME=${LOCAL_IMAGE_NAME}" >> "$ENV_FILE"
    { set +x; } 2>/dev/null
fi
log_newline