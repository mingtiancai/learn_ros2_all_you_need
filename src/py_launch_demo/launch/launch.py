from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(package="py_launch_demo", executable="talker"),
            Node(package="py_launch_demo", executable="listener"),
        ]
    )
