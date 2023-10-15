from setuptools import find_packages, setup
from setuptools import setup
import os
from glob import glob

package_name = 'hb_task_1b'

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
    maintainer='raj',
    maintainer_email='raj@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "gazebo.launch = hb_task_1b.gazebo.launch:main",
            "hb_task1b.launch = hb_task_1b.hb_task1b.launch:main"
        ],
    },
)
