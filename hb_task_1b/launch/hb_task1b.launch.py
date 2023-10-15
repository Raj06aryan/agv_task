from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    controller_node = Node(
        package="my_robot_control",            # Replace with your actual package name
        executable="robot_controller_node",    # Replace with your actual executable name
    )
    
    service_node = Node(
        package="my_robot_control",            # Replace with your actual package name
        executable="service_node",             # Replace with your actual executable name
    )

    ld.add_action(controller_node)
    ld.add_action(service_node)

    return ld


