#!/bin/bash

CI_USER=jenkins

USER_ID=$(id ${CI_USER} -u)
GROUP_ID=$(id ${CI_USER} -g)

docker build --rm -t mypw --build-arg USER_ID=${USER_ID} --build-arg GROUP_ID=${GROUP_ID} .

# cleanup
docker images -a -q -f "dangling=true" | xargs docker rmi
