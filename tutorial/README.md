# Exercise Description

## Gazebo world container
1. Navigate to the /exercises_summer_school_hri_day/tutorial directory
2. Make the run_gazebo.sh file executable
    - `chmod +x run_gazebo.sh`
3. Launch the gazebo world
    - `/.run_gazebo.sh`

## Controller container
1. Navigate to the directory /exercises_summer_school_hri_day/tutorial
2. Make the run_controller.sh file executable
    - `chmod +x run_controller.sh`
3. Launch the gazebo world
    - `/.run_controller.sh`

## Exercise implementation
1. In the controller container navigate to the ~/catkin_ws/src/summer_school_controller/src/ directory
    - `cd ~/catkin_ws/src/summer_school_controller/src/`
### Tasks
1. Edit with your preferable editor the velocity_controller.py file to control the UAV
2. Edit with your preferable editor the keyboard_teleoperation.py file to give position setpoints from your keyboard
3. Edit with your preferable editor the position_prediction.py file to compensate for communication delays
* If you need extra terminals for your controller container: in a new window terminal run: `docker exec -it <your_container_name> bash`

## Troubleshooting
Consider opening an Issue if you have [troubles](https://github.com/AERO-TRAIN/exercises_summer_school_hri_day/issues) with the exercises of the repo.\
Feel free to use the [Discussions](https://github.com/AERO-TRAIN/exercises_summer_school_hri_day/discussions) tab to exchange ideas and ask questions.
