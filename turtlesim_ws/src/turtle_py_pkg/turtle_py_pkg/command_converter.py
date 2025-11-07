#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

from geometry_msgs.msg import Twist # for publishing to turtlesim

# Subscribes to the /commands topic and, based on the messages it receives, publishes commands to the /turtle1/cmd_vel topic.

 
class CommandConverterNode(Node):
    def __init__(self):
        super().__init__("command_converter")
        self.subscriber = self.create_subscription(String, "commands", self.callback_commands, 10)
        self.publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.get_logger().info("Command Converter has been started")
 
    def callback_commands(self, msg_in: String):
        mvmt = Twist()
        if (msg_in.data == "move right") :
            mvmt.linear.x = 0.1
            mvmt.linear.y = 0.0
            self.publisher.publish(mvmt)
        elif (msg_in.data == "move forward") :
            mvmt.linear.x = 0.0
            mvmt.linear.y = 0.1
            self.publisher.publish(mvmt)
        

def main(args=None):
    rclpy.init(args=args)
    node = CommandConverterNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
