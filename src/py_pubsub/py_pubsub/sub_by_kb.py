import rclpy
from rclpy.node import Node

from std_msgs.msg import String
#발행할 타입의 메세지 타입을 import 한다 


class Sub_by_KB(Node):

    def __init__(self):
        super().__init__('sub_by_kb')
        sub = self.create_subscription(String, 'control', self.get_control,10)

    def get_control(self, msg):
        print('"%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    sub_by_kb = Sub_by_KB()

    rclpy.spin(sub_by_kb)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    sub_by_kb.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
