#!/usr/bin/env bash

# to prepare for logs, make it nice
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
NC='\033[0m'

log_message() {
    local COLOR=$1
    local BLOCK=$2
    local MESSAGE=$3
    eval "echo -e \"\${$COLOR}\$(date '+%Y-%m-%d %H:%M:%S') - === Block \${BLOCK}: \${MESSAGE} ===\${NC}\""
}

log_newline() {
    echo -e "\n\n"
}