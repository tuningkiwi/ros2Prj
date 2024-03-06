import rclpy
from rclpy.node import Node

from std_msgs.msg import String
#발행할 타입의 메세지 타입을 import 한다 


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        sub = self.create_subscription(String, 'hello', self.callback,10)

    def callback(self, msg):
        print('"%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimalsubscriber = MinimalSubscriber()

    rclpy.spin(minimalsubscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
