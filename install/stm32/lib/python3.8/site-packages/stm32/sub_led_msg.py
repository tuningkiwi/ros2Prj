import rclpy
from rclpy.node import Node
import serial

from std_msgs.msg import String
#발행할 타입의 메세지 타입을 import 한다 

sp  = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

class Sub_Led_Msg(Node):

    def __init__(self):
        super().__init__('sub_led_msg')
        sub = self.create_subscription(String, 'led_ctrl', self.get_led_msg,10)

    def get_led_msg(self, msg):
        print('"%s"' % msg.data)
        if msg.data == "LED Off":
            sp.write(b'0')
            print("LED Off")
        elif  msg.data == "LED On":
            sp.write(b'1')
            print("LED On")
        else:
            pass


def main(args=None):
    rclpy.init(args=args)

    sub_led_msg = Sub_Led_Msg()

    rclpy.spin(sub_led_msg)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    sub_led_msg.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
