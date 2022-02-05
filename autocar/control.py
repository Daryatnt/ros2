
import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import String
# def visSub_callback(img):
#     print("hi")
  
class visNode(Node):

    def __init__(self):
        super().__init__('vision')
        self.visionSub = self.create_subscription(
            String,
            'freertos_int32_publisher',
            self.visSub_callback,
            10)
        self.visionPub= self.create_publisher(String, 'visiondata', 10)

        ###########
        ### WITHOUT TIMER
        # while(True):
        #     self.visionPub.publish(data) 
        ### WITH TIMER 
    #     timer_period = 0.05  # seconds
    #     self.timer = self.create_timer(timer_period, self.timer_callback)
    #     self.i = 0
    # def timer_callback(self):
    #     self.visionPub.publish(data)


    def visSub_callback(self, img):
        print(img)

def main(args=None):
    rclpy.init(args=args)
    vision_node= visNode()
    rclpy.spin(vision_node)