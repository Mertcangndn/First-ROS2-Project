#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotStateSubscriberNode(Node):

    def __init__(self):
        super().__init__("robot_state_subscriber")

        self.subscriber = self.create_subscription(String , "state_publisher" , self.callback , 10)
        self.get_logger().info("Robot State Publisher has been started.")
    
    def callback(self,msg):
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = RobotStateSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()    