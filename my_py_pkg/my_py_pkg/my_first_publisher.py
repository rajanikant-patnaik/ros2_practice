#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String


class MyFirstPublisherNode(Node): 
    def __init__(self):
        super().__init__("my_first_publisher") 
        self.counter =0
        self.publisher = self.create_publisher(String, "my_updates",10)
        self.timer = self.create_timer(0.5,self.publish_message)
        self.get_logger().info("my_first_publisher package has been stared")

    def publish_message(self):
        msg =String()
        self.counter += 1
        msg.data ="Hello From my first publisher number" + str(self.counter)
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyFirstPublisherNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
