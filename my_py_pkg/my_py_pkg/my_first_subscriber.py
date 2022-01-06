#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class MyFirstSubscriberNode(Node): 
    def __init__(self):
        super().__init__("my_first_subscriber")         
        self.subscriber = self.create_subscription(String,"my_updates",self.subscribe_msg,10)
        self.get_logger().info("Subscriber node started reciving msgs")
    
    def subscribe_msg(self, msg):
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = MyFirstSubscriberNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
