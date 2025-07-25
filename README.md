# learn_ros2_all_you_need

| key   | value | 
|--------|------|
| ros2    | kilted  |
| sys| ubuntu24.04 |


# 1.compile code and run

## 1.1.cpp_pubsub_demo

Tips:Most simplest topic demo sample for topic publish and subscribe in c++

Go to the project root directory 

```bash
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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
rosdep install -i --from-path src --rosdistro kilted -y
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