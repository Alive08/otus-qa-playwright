#!/bin/bash

usage()
{
    cat << USAGE >&2
Usage:
    ${0##*/} <path[s] to tests to be executed>
USAGE
    exit 1
}

if [ $# -eq 0 ]; then
    usage
fi

CI_USER=jenkins

export USER_ID=$(id ${CI_USER} -u)

export GROUP_ID=$(id ${CI_USER} -g)

export UID

export GID=$(id -g)

export DEBUG=${DEBUG}

export PYTEST_ARGS="$@"

rm -rf artifacts

mkdir -p artifacts

docker network create --driver bridge test_net || true

docker-compose up --build --abort-on-container-exit

tests_status=$?

docker-compose down

docker network rm test_net

docker images -a -q -f "dangling=true" | xargs docker rmi

exit ${tests_status}
