#!/usr/bin/env bash
cd "$(dirname "$0")"

source ./common.sh

# BOOTUP POSTGRES server
log_message YELLOW 1 "Booting up postgres server"
{ set -x; } 2>/dev/null
docker compose -f ../docker-compose.yaml up -d
{ set +x; } 2>/dev/null
log_newline