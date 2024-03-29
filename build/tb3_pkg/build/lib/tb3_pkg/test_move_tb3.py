import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from tb3_pkg.move_tb3 import MoveTB3
from math import radians, degrees, sqrt, atan2


def main(args=None):
    rclpy.init(args=args)
    node = MoveTB3()
    
    try:
        angle = radians(float(input("input rotation (deg): ")))
        dist = float(input("input distance (m)  : "))
        
        #angle = atan2(y, x)
        #dist  = sqrt(pow(x, 2) + pow(y, 2))
        
        #print("rotate %s(deg), and than straight %s(m)" %(degrees(angle), dist))
        
        node.rotate(angle)
        node.straight(dist)
        
        rclpy.spin(node)
                
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
        
    finally:
        node.destroy_node()
        rclpy.shutdown()
    
            
if __name__ == '__main__':
    main()
    
