#!/bin/bash

XVFB=""

# echo "Starting Xvfb"
# Xvfb :99 -ac &
# sleep 2
# export DISPLAY=:99

if grep -q "headed" <<< "$@"; then
    XVFB="xvfb-run"
fi

echo "Executing $@"

$@
