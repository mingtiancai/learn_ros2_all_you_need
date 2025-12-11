from setuptools import find_packages, setup

package_name = "py_tf2_static_demo"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=[
        "setuptools",
        "rclpy",
        "geometry_msgs",
        "tf2_ros",
        "transforms3d",
    ],
    zip_safe=True,
    maintainer="gaoming",
    maintainer_email="2427373908@qq.com",
    description="TODO: Package description",
    license="TODO: License declaration",
    extras_require={
        "test": [
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": ["broadcaster = py_tf2_static_demo.py_tf2_static_func:main"],
    },
)
