import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDrivesStamped

class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher = self.create_publisher(AckermannDriveStamped,'drive',10)

        self.declare_parameter('v',0.0)
        self.declare_parameter('d',0.0)
        
        timer_period = 0.01 #10Hz
        self.timer = self.create_timer(timer_period,self.publish_drive)
        
    def publish_drive(self):
        msg = AckermannDriveStamped()
        msg.drive.speed = self.get_parameter('v').get_parameter_value().double_value
        msg.drive.steering_angle = self.get_parameter('d').get_parameter_value().double_value
        self.publisher.publish(msg)

    def main(args=None):
        rclpy.init(args=args)
        node = TalkerNode()
        rclpy.spin(node)
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
