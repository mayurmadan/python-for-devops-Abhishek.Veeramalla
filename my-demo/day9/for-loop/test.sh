#!/bin/bash
docker_conatiner_list=$(docker ps)
echo "$docker_conatiner_list"

for container in $docker_conatiner_list; do 
 docker rm -f $container > /dev/null 2>&1
done
