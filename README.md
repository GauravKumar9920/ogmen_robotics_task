# ogmen_autonomous_slam[ video_solutions/Documentation](https://drive.google.com/drive/folders/1LddGGvEboLfEoY1EKUzDgPqOiyOkMALp?usp=sharing).
## Prerequisites and setup for the Project
### ROS Installation
I used Ubuntu 20.04 OS with ros noetic Version. Check the ROS official documentation for the Installation

### Gazebo ROS Installation
The main Gazebo Simulator which is an stand alone application must be installed. Go through the documentation
[Gazebo Installation](http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install).
Test the working of Gazebo and its version with 

After Installing the Gazebo, the Gazebo ROS Package must be installed seperately
```
sudo apt-get install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control
```
Replace `noetic` with your version of ROS everwhere in this tutorial.
### Turtlebot3 packages([More Details](http://wiki.ros.org/turtlebot3))
The Turtlebot3 ROS packages can be either downloaded and built from source files in your workspace
or else directly installed from the linux terminal. Either way works, I would recommend doing both as it installs all the missing dependencies required automatically.
#### Direct Installation
```
source /opt/ros/noetic/setup.bash
sudo apt-get install ros-noetic-turtlebot3-msgs
sudo apt-get install ros-noetic-turtlebot3
```
Building the packages
```
cd catkin_ws/src
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations
cd ..
catkin_make
source /devel/setup.bash
```

### Navigation Stack ([More Details](http://wiki.ros.org/navigation))
The Navigation stack can also be downloaded as souce files to your workspace and built.
```
sudo apt-get install ros-noetic-navigation
cd catkin_ws/src
git clone -b noetic-devel https://github.com/ros-planning/navigation
cd ..
catkin_make
source /devel/setup.bash
```


## For Task 1 
Set your environment variable to the model robot to be used.
```
export TURTLEBOT3_MODEL=waffle
source ~/.bashrc
```
1st way (reccomended)
run - 
```
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/gaurav/catkin_ws/src/ogmen_robotics/src/maps/map.yaml
```
then run in a diffrent termaina (you can specify the start and goal location in the code)-
```
rosrun ogmen_robotics navigate_goal.py
```
2nd way(works effortlessly, try this)-

Execute the given launch to open Gazebo with the given world file and place the robot Turtlebot3 Waffle model in it and Perform Navigation from point A to B.
```
roslaunch ogmen_robotics q1.launch
```
This will gerate and map and a path and display it before starting. Press-1 to start the process.



## For Task 2 
## Step 1 : Place the Robot in the Environment within Gazebo
Set your environment variable to the model robot to be used.
```
export TURTLEBOT3_MODEL=waffle
source ~/.bashrc
```
Execute the given launch to open Gazebo with the given world file and place the robot Turtlebot3 Waffle pi model in it and Perform Autonomous exploration of the environment and generate the Map
```
roslaunch ogmen_robotics q2.launch
```

Run the q2.launch file which executes two tasks for us at the same time.
1. It starts the **SLAM** node in the Navigation stack with a custom modified RVIZ file to monitor the mapping of the environment.
2. It simultaneously starts the **Autonomous explorer** which is a Python based controller to move around the robot grazing all the areas whcih helps the **SLAM** Node to complete the mapping. The default algorithm used for the exploration is RRT algorithm. 
### Setting Exploration region for RRT in RVIZ Window ([More Details](http://wiki.ros.org/rrt_exploration/Tutorials/singleRobot))
The RRT exploration requires a rectangular region around to be defined in the RVIZ window using four points and an starting point for exploration within the known region of the robot. The total five points must be defined in the exact sequence given below using the RVIZ **Publish Points** option. [Source](http://wiki.ros.org/rrt_exploration/Tutorials/singleRobot)<br />
**Monitor the Mapping process in RVIZ window** and sit back and relax unitll our robot finishes mapping XD .

**Once you are satisfied with the constructed map, Save the map.**
```
rosrun map_server map_saver -f my_map
```
The **my_map.pgm** and **my_map.yaml** gets saved in your worspace directory. Move these to files to the package's **maps** folder (catkin_ws\src\ogmen_robotics\src\maps).**Now your new map.
<br />
