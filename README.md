# Digital-Control-Project-3
The files of this repository are intended to be working on a Raspberry PI so that they be can used to manipulate the Roomba.

Author: **Hattan Badyah**

**Objective of this Repository**
- The main goal of this project is to create a publisher/subscriber to control the Roomba.
- The publisher sends the six IR sensors readings from the Roomba.
- The subscriber receives the IR sensors readings and control the left and right wheels for the Roomba.

![ROSCORE](https://github.com/tuf76885/Digital-Control-Project-3/blob/master/ROS/Screen%20Shot%202017-11-29%20at%204.58.21%20PM.png)

**Download the following**:
- fundamental information about Raspberry pi -> refer to the following link(https://www.raspberrypi.org).
- We use Ubuntu as the OS for the pi in this project -> the installation instruction can be found at the following     link(https://wiki.ubuntu.com/ARM/RaspberryPi).
- Installation of ROS/Kinect -> refer to the following link(http://wiki.ros.org/Installation/UbuntuARM)
- The libraries to manipulate the Roomba -> refer to the following link(https://pypi.python.org/pypi/pycreate2/0.7.3).
- A good book for reference about ROS is (O'REILLY: Programming Robots with ROS) 

**How to Begin With ROS**
- To be able to use ROS, you first have to create a workspace the will contain all your code. The following code is a sample to create a workspace called (catkin_ws)_:
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```
- The next step is to create a package in the source file of the workspace. This package will contain the code files:
```
cd ~/catkin_ws/src
catkin_create_pkg my_code rospy
```
- To add the Python scripts to the package, we have to go the source directory of the package we created in the last step:
```
cd ~/catkin_ws/src/my_code/src
```
- Copy and paste the following code to access the Rwheel and Rsensor scripts:
```
git clone https://github.com/tuf76885/Digital-Control-Project-3
```
- Copy and paste the following code to go back to the workspace directory:
```
cd ~/catkin_ws
```
- Copy and paste the following code to source your new setup.bash file:
```
source devel/setup.bash
```
**After completeing the last step, follow the following procedure to run the publisher and subscriber for the Roomba:**
- In the current Terminal window, type in the following command:
```
roscore
```
- The next step is to open a new Terminal window and the run the following command to establish the connection between the roscore and the Rsensor.py script, which is the publisher:
```
rosrun Rsensor.py
```
- The last step is to open up a third Terminal window and run the following code to connect the publisher with the Rwheel.py script, which is the subscriber:
```
rosrun Rwheel.py
```
**Code To help in Debugginh**
- If you want to check the topics available to connect to:
``` 
rostopic list
```
- To check the message published by publisher:
```
rostopic echo Rsensor
```
- To find information about the topic:
```
rostopic info Rsensor
```

