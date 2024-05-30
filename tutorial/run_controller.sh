# Run the docker image for the gazebo simulator
xhost +
docker run --privileged -it --net=host achilleas2942/aerotrain-hri-controller
