# Exercise Description

## Gazebo world container
1. Navigate to the /exercises_summer_school_hri_day/tutorial directory
2. Make the run_gazebo.sh file executable
    - `chmod +x run_gazebo.sh`
3. Launch the gazebo world
    - `./run_gazebo.sh`

## Controller container
1. Navigate to the /exercises_summer_school_hri_day/tutorial directory
2. Make the run_controller.sh file executable
    - `chmod +x run_controller.sh`
3. Enter the controller environment
    - `./run_controller.sh`

## Exercise implementation
1. In the controller container navigate to the ~/catkin_ws/src/summer_school_controller/src/ directory
    - `cd ~/catkin_ws/src/summer_school_controller/src/`
### Tasks
**Aim:** The aim of this workshop is to design a basic teleoperation interface to navigate a quadrotor UAV to a desired position.
**Goal:** The goal is to navigate the UAV through the three pipes to establish smooth contact with the target.
**Task 1** Design a position controller for the UAV.
    1. Please open the _velocity_controller.py_ file with your preferred editor.
    2. Under the _vel_sp()_ method in the _VelocityController_ class, please insert your code to send velocity inputs to track the position setpoints.
    3. You may publish waypoints on the _/setpoints_ topic to test the tracking performance of the controller.
**Task 2** Enable a Teleoperation Interface.
    1. Please open the _keyboard_teleoperation.py_ with your preferred editor.
    2. Under the _on_press_ method in the _DroneTeleoperator_ class, insert your code to read keyboard inputs and publish position setpoints.
    3. Test it with the _velocity_controller.py_ to navigate the UAV to different positions.
**Task 3** Compensate for the Communication Delays.
    You may have noticed that there is a delay in the communication between the controller and the simulator.
    1. Please open the _position_prediction.py_ with your preferred editor.
    2. Under the _esimate_delay_ method in the _PositionPredictor_ class, insert your code to estimate the average delay from the ROS messages.
    3. Under the _esimate_position_ method in the _PositionPredictor_ class, insert your code to estimate the current position of the UAV from the available knowledge of the delays.
    4. Test it with the _velocity_controller.py_ and _keyboard_teleoperation.py_ to navigate the UAV through the pipes.

**NOTE: If you need extra terminals for your controller container: in a new window terminal run:** `docker exec -it <your_container_name> bash`

## Troubleshooting
Consider opening an Issue if you have [troubles](https://github.com/AERO-TRAIN/exercises_summer_school_hri_day/issues) with the exercises of the repo.\
Feel free to use the [Discussions](https://github.com/AERO-TRAIN/exercises_summer_school_hri_day/discussions) tab to exchange ideas and ask questions.
