import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DigitalTwinNode(Node):
    def __init__(self):
        super().__init__('digital_twin_node')
        self.subscription = self.create_subscription(
            Twist,
            'turtle1/cmd_vel',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)

    def listener_callback(self, msg):
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)

def main(args=None):
    rclpy.init(args=args)
    digital_twin_node = DigitalTwinNode()
    rclpy.spin(digital_twin_node)
    digital_twin_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
