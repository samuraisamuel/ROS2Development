#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
 
class RocketLaunch(Node):
    def __init__(self):
        super().__init__("rocket_launch") 
        self.count = 10 # counter variable
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):

        if (self.count  > 1) :
            self.get_logger().info(str(self.count) + " seconds till blast off!!")
            self.count -= 1

        elif (self.count == 1) :
            self.get_logger().info(str(self.count) + " second till blast off!!")
            self.count -= 1

        else : 
            self.get_logger().info("Blast Off!!")
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = RocketLaunch() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
