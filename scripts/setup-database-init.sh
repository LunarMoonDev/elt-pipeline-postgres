#!/usr/bin/env bash
cd "$(dirname "$0")"

source ./common.sh

# DELETE FOLDERS FOR DATA
log_message YELLOW 1 "Removing local database volume"
{ set -x; } 2>/dev/null
rm -rf ../.data/
{ set +x; } 2>/dev/null
log_newline

# BOOTING UP POSTGRES
log_message GREEN 2 "Booting up postgres server"
{ set -x; } 2>/dev/null
docker compose -f ../docker-compose.yaml up -d
{ set +x; } 2>/dev/null
log_newline

# WAITING 40 SECONDS
log_message GREEN 3 "Waiting for 40 seconds"
{ set -x; } 2>/dev/null
sleep 40
{ set +x; } 2>/dev/null
log_newline

# CREATING SOURCE DATA
log_message BLUE 4 "Creating source data"
{ set -x; } 2>/dev/null
pipenv run python -b ../scripts/create-source-data.py
{ set +x; } 2>/dev/null
log_newline
