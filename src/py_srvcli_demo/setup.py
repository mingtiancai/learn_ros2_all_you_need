from setuptools import find_packages, setup

package_name = 'py_srvcli_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gaoming',
    maintainer_email='2427373908@qq.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'service = py_srvcli_demo.service_member_function:main',
        'client = py_srvcli_demo.client_member_function:main',
    ],
    },
)
