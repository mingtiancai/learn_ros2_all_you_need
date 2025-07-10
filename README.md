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