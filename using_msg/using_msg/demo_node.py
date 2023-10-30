import rclpy
from rclpy.node import Node
from custom_msgs.msg import Demo

class DemoNode(Node):

    def __init__(self):
        super().__init__('demo_node')

        self.pub = self.create_publisher(
            Demo,
            '/test_msg',
            10
        )

        self.create_timer(1.0, self.execute)

    def execute(self):
        msg = Demo()
        msg.header.frame_id = 'my_frame'
        msg.num = 500

        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = DemoNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()