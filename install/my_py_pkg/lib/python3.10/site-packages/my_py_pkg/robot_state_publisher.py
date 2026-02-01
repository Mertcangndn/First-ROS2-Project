#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotStatePublisherNode(Node):
    def __init__(self):
        super().__init__("robot_state_publisher")
        
        self.robotname = "yeyeb001"
        self.publisher = self.create_publisher(String,"state_publisher",10)
        self.timer = self.create_timer(0.5, self.publish_state)

        self.get_logger().info("Robot State Publisher has been started.")
    
    def publish_state(self):
        msg = String()
        msg.data = f"HELLO, this is {self.robotname} from Tukkan!"
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotStatePublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()