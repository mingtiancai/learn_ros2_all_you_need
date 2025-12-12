# learn_ros2_all_you_need

| key   | value | 
|--------|------|
| ros2    | jazzy  |
| sys| ubuntu24.04 |


# 1.compile code and run

## 1.1.cpp_pubsub_demo

Tips:Most simplest topic demo sample for topic publish and subscribe in c++

Go to the project root directory 

```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select cpp_pubsub_demo
```

source package directory
```bash
source ./install/setup.sh
```

run a terminal
```bash
ros2 run cpp_pubsub_demo talker
```

run another terminal
```bash
ros2 run cpp_pubsub_demo listener
```

## 1.2.py_pubsub_demo

Tips:Most simplest topic demo sample for topic publish and subscribe in python


Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select py_pubsub_demo
```

source package directory
```bash
source ./install/setup.sh
```

run a terminal
```bash
ros2 run py_pubsub_demo talker
```

run another terminal
```bash
ros2 run py_pubsub_demo listener
```

## 1.3.cpp_srvcli_demo

Tips:Most simplest service demo sample for service server and client in c++

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select cpp_srvcli_demo
```

source package directory
```bash
source ./install/setup.sh
```

run a terminal
```bash
ros2 run cpp_srvcli_demo server
```

run another terminal
```bash
ros2 run cpp_srvcli_demo client
```

## 1.4.py_srvcli_demo

Tips:Most simplest service demo sample for service server and client in python

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select py_srvcli_demo
```

source package directory
```bash
source ./install/setup.sh
```

run a terminal
```bash
ros2 run py_srvcli_demo server
```

run another terminal
```bash
ros2 run py_srvcli_demo client
```

## 1.5.tutorial_interfaces_demo
Tips:Most simplest interface sample for message and srv files

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select tutorial_interfaces_demo
```

source package directory
```bash
source ./install/setup.sh
```

[optional]show message file for Num.msg
```bash
ros2 interface show tutorial_interfaces_demo/msg/Num
```

[optional]show message file for Sphere.msg
```bash
ros2 interface show tutorial_interfaces_demo/msg/Sphere
```

[optional]show srv file for AddThreeInts.srv
```bash
ros2 interface show tutorial_interfaces_demo/srv/AddThreeInts
```

## 1.6.cpp_pubsub_for_interface
Tips:The simplest code example is used to demonstrate topic message subscription and publishing using custom message types based on C++

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select cpp_pubsub_for_interface
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run cpp_pubsub_for_interface talker
```

run another terminal
```bash
ros2 run cpp_pubsub_for_interface listener
```

## 1.7.py_pubsub_for_interface
Tips:The simplest code example is used to demonstrate topic message subscription and publishing using custom message types based on python

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select py_pubsub_for_interface
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run py_pubsub_for_interface talker
```

run another terminal
```bash
ros2 run py_pubsub_for_interface listener
```

## 1.8.cpp_srvcli_for_interface_demo
Tips:The simplest code example is used to demonstrate srv message server and client using custom message types based on c++

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select cpp_srvcli_for_interface_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run cpp_srvcli_for_interface_demo server
```

run another terminal
```bash
ros2 run cpp_srvcli_for_interface_demo client
```

## 1.9.py_srvcli_for_interface_demo
Tips:The simplest code example is used to demonstrate srv message server and client using custom message types based on python

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select py_srvcli_for_interface_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run py_srvcli_for_interface_demo server
```

run another terminal
```bash
ros2 run py_srvcli_for_interface_demo client
```

## 1.10.more_interfaces_demo
Tips:Use custom topic format in the package to publish messages to the outside world

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select more_interfaces_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run more_interfaces_demo publish_address_book
```

run another terminal
```bash
ros2 topic echo /address_book
```

## 1.11.cpp_parameters_demo
Tips:The simplest parameter example using C++

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select cpp_parameters_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run cpp_parameters_demo minimal_param_node
```

run another terminal
```bash
ros2 ros2 param set /minimal_param_node my_parameter earth
```

## 1.12.cpp_parameters_by_launch_demo
Tips:The simplest parameter example using C++ by launch file

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select cpp_parameters_by_launch_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run cpp_parameters_by_launch_demo minimal_param_node
```

## 1.13.python_parameters_demo
Tips:The simplest parameter example using python

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select python_parameters_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run python_parameters_demo minimal_param_node
```

run another terminal
```bash
ros2 ros2 param set /minimal_param_node my_parameter earth
```

## 1.14.python_parameters_by_launch_demo
Tips:The simplest parameter example using python by launch file

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select python_parameters_by_launch_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run python_parameters_by_launch_demo minimal_param_node
```

## 1.15.custom_action_interfaces_demo
Tips:The simplest action interfaces demo

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select custom_action_interfaces_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 interface show custom_action_interfaces_demo/action/Fibonacci
```

## 1.16.custom_action_cpp_demo
Tips:The simplest action server and client demo for c++

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select custom_action_cpp_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run custom_action_cpp_demo fibonacci_action_server
```

run another terminal
```bash
ros2 run custom_action_cpp_demo fibonacci_action_client
```

## 1.17.custom_action_py_demo
Tips:The simplest action server and client demo for python

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select custom_action_py_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run custom_action_py_demo server
```

run another terminal
```bash
ros2 run custom_action_py_demo client
```

## 1.18.python_camera_demo
Tips:The simplest camera demo, read mp4 video and show

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select python_camera_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run python_camera_demo demo 
```

## 1.19.py_camera_node
Tips:The simplest camera node demo, pub node publish camera use ros2 image message and sub node receive data and show

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select py_camera_node
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run py_camera_node pub_demo
```

run another terminal
```bash
ros2 run py_camera_node sub_demo  
```

## 1.20.py_qos_demo
Tips:The simplest qos demo

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select py_qos_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run py_qos_demo talker
```

run another terminal
```bash
ros2 run py_qos_demo listener  
```

## 1.21.py_launch_demo
Tips:The simplest launch demo, one node is pub and other node is sub

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select py_launch_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 launch py_launch_demo launch.py
```

## 1.22.py_tf2_static_demo
Tips:The simplest tf2 static broadcaster demo by python

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select py_tf2_static_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run py_tf2_static_demo broadcaster
```

run another terminal
```bash
ros2 run tf2_tools view_frames
```
generate static tf broadcaster pdf file

## 1.23.cpp_tf2_static_demo
Tips:The simplest tf2 static broadcaster demo by cpp

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select cpp_tf2_static_demo
```

source package directory
```bash
source ./install/setup.sh
```
run a terminal
```bash
ros2 run cpp_tf2_static_demo broadcaster
```

run another terminal
```bash
ros2 run tf2_tools view_frames
```

## 1.24.py_tf2_dynamic_demo
Tips:The simplest tf2 dynamic broadcaster demo by python

Go to the project root directory 
```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```

compiler package
```bash
colcon build --packages-select py_tf2_dynamic_demo
```

source package directory
```bash
source ./install/setup.sh
```

run a terminal
```bash
ros2 run turtlesim turtlesim_node
```

run another terminal
```bash
ros2 run py_tf2_dynamic_demo broadcaster --ros-args -p turtlename:=turtle1
```

run another terminal
```bash
ros2 run tf2_tools view_frames
```

if you want to look dynamic tf braodcaster ,you can use command
```bash
ros2 run tf2_ros tf2_echo world turtle1
```



