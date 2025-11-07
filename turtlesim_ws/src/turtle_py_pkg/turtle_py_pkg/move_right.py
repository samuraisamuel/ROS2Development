import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
# Publishes the message “move right” to the /commands topic every 2 seconds
 
class MoveRightNode(Node):
    def __init__(self):
        super().__init__("move_right")
        self.publisher = self.create_publisher(String, "commands", 10)  # create publisher on /commands topic
        self.create_timer(2.0, self.timer_callback)                     # create timer that executes timer_callback every 2 seconds
        self.get_logger().info("Move Right node has started")         # prints text to console at runtime
   
    def timer_callback(self):
        msg = String()               # create String object
        msg.data = "move right"      # edit actual String content
        self.publisher.publish(msg)  # publish the string 
 
 
def main(args=None):
    rclpy.init(args=args)
    node = MoveRightNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
