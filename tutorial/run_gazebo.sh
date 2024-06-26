#!/bin/bash

# Allow connections to the X server
xhost +

# Run the container for the gazebo simulator
docker run --privileged -it --net=host --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" achilleas2942/aerotrain-hri-gazebo:latest
