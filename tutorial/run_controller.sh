#!/bin/bash

# Allow connections to the X server
xhost +

# Run the container in detached mode
container_id=$(docker run --privileged -d --net=host --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" achilleas2942/aerotrain-hri-controller:latest)

# Open a bash terminal in the running container for the controller
docker exec -it $container_id bash