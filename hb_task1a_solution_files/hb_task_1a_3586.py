#!/usr/bin/env python3

########################################################################################################################
########################################## eYRC 23-24 Hologlyph Bots Task 1A ###########################################
# Team ID: eYRC#HB#3586
# Team Leader Name: Raj Aryan
# Team Members Name: Prasit Mazumder, Satyabrata Nayak, Prasanna Paithankar
# College: Indian Institute of Technology Kharagpur
########################################################################################################################

# Importing the required module
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn

# Class to move the robot
class Turtle(Node):
    def __init__(self) -> None:
        super().__init__('task_1a_3586')
        self.i = 0
        # Creating a publisher object to publish messages to the topic '/turtle1/cmd_vel'
        self.subscriber = self.create_subscription(Pose, '/turtle1/pose', self.listener_callback, 1000)
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        # Creating a timer object to track the time
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def listener_callback(self, msg):
        '''
        Purpose:
        ---
        This is a subscriber callback function. It is called when a message is received on the topic '/turtle1/pose'. It checks if the first turtle ha completed one revolution, then spawning the second turtle and subscribing to its pose topic.

        Input Arguments:
        ---
        `msg` :  [ object ]
            The message received from the topic '/turtle1/pose'

        Returns:
        ---
        None
        '''

        # self.get_logger().info(f'x: {msg.x}, y: {msg.y}, theta: {msg.theta}')
        if (msg.x < 5.544445 - 0.005) and (msg.y < 5.544445 + 0.005) and self.i == 0:
            self.get_logger().info('Reached')
            self.timer.cancel()

            self.spawn_client = self.create_client(Spawn, '/spawn')
            while not self.spawn_client.wait_for_service(timeout_sec=3.0):
                self.get_logger().info('service not available, waiting again...')
            self.spawn_request = Spawn.Request()
            self.spawn_request.name = 'turtle2'
            self.spawn_request.x = 5.544445
            self.spawn_request.y = 5.544445
            self.spawn_request.theta = 0.0
            self.spawn_client.call_async(self.spawn_request)
            self.get_logger().info('spawned turtle2')
            self.i = 1
            self.subscriber = self.create_subscription(Pose, '/turtle2/pose', self.listener_callback2, 1000)
            self.publisher = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
            # Creating a timer object to track the time
            timer_period = 0.5
            self.timer = self.create_timer(timer_period, self.timer_callback2)

    def listener_callback2(self, msg):
        '''
        Purpose:
        ---
        This is a subscriber callback function. It is called when a message is received on the topic '/turtle2/pose'. It checks if the second turtle has reached the goal, then cancelling the timer and destroying the node.

        Input Arguments:
        ---
        `msg` :  [ object ]
            The message received from the topic '/turtle1/pose'

        Returns:
        ---
        None
        '''

        # self.get_logger().info(f'x: {msg.x}, y: {msg.y}, theta: {msg.theta}')
        if (msg.x < 5.544445) and (msg.y > 5.544445 - 0.005):
            self.get_logger().info('Reached')
            self.timer.cancel()
            self.destroy_node()
        
    def timer_callback(self):
        '''
        Purpose:
        ---
        This is a timer callback function. It is called when the timer is fired. It publishes a message to the topic '/turtle1/cmd_vel' to move the turtle in a circle with linear and angular velocities as 0.7 and 0.7 respectively.

        Input Arguments:
        ---
        None

        Returns:
        ---
        None
        '''

        # Creating a Twist message object
        msg = Twist()
        # Assigning the linear and angular velocities
        msg.linear.x = 0.7
        msg.angular.z = 0.7
        # Publishing the message
        self.publisher.publish(msg)

    def timer_callback2(self):
        '''
        Purpose:
        ---
        This is a timer callback function. It is called when the timer is fired. It publishes a message to the topic '/turtle2/cmd_vel' to move the turtle in a circle with linear and angular velocities as 0.7 and -0.42 respectively.

        Input Arguments:
        ---
        None

        Returns:
        ---
        None
        '''

        # Creating a Twist message object
        msg = Twist()
        # Assigning the linear and angular velocities
        msg.linear.x = 0.7
        msg.angular.z = -0.42
        # Publishing the message
        self.publisher.publish(msg)

def main(args=None):
    '''
    Purpose:
    ---
    This is the main function. It creates an object of the class Turtle and spins the node. It also destroys the node and shuts down the ROS client.
    
    Input Arguments:
    ---
    None
    
    Returns:
    ---
    None
    
    Example call:
    ---
    Called automatically by the Operating System
    '''

    # Initializing the ros client
    rclpy.init(args=args)
    # Creating an object of the class Turtle
    turtle = Turtle()
    # Spin the node
    rclpy.spin(turtle)
    # Destroy the node explicitly
    turtle.destroy_node()
    # Shutdown the ROS client
    rclpy.shutdown()

if __name__ == '__main__':
    main()




