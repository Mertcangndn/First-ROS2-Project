#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class NodeName(Node):
    
    def __init__(self):
        super().__init__("node_name")
        self.get_logger().info("Node has been started!")
        self. pulisher = self.create_publisher(String , "TOPIC-001" , 10)
        self.timer = self.create_timer(0.5 , self.timer_callback)
    
    def timer_callback(self):
        msg = String()
        msg.data = "riceb"
        self.get_logger().info(msg)

def main(args=None):
    rclpy.init(args=args)
    node = NodeName()
    rclpy.spin(node)
    rclpy(shutdown)

if __name__ == "__main__":
    main()
