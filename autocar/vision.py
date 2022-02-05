from numpy.core.numeric import True_
import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import Int16MultiArray


bridge=CvBridge()
# class visNode(Node):

#     def __init__(self):
#         super().__init__('vision')
#         self.visionSub = self.create_subscription(
#             Image,
#             'camImage',
#             self.visSub_callback,
#             10)
#         self.visionPub= self.create_publisher(Int16MultiArray, 'visiondata', 10)
#         ###########
#         global data
#         data=Int16MultiArray()
#         data.data=[1,2,3,4]
#         ###########
#         ### WITHOUT TIMER
#         # while(True):
#         #     self.visionPub.publish(data) 
#         ### WITH TIMER 
#     #     timer_period = 0.05  # seconds
#     #     self.timer = self.create_timer(timer_period, self.timer_callback)
#     #     self.i = 0
#     # def timer_callback(self):
#     #     self.visionPub.publish(data)


#     def visSub_callback(self, img):
#         global camImg
#         camImg=bridge.imgmsg_to_cv2(img,desired_encoding="bgr8")
#         cv2.imshow("vision",camImg)
#         cv2.waitKey(10)



# def main(args=None):
#     rclpy.init(args=args)
#     vision_node= visNode()
#     rclpy.spin(vision_node)
###     WITHOUT CLASS & TIMER
data=Int16MultiArray()
def visSub_callback(img):
    camImg=bridge.imgmsg_to_cv2(img,desired_encoding="bgr8")
    data.data=[1,2,3,4]
    visPub.publish(data)   
def main():
     rclpy.init()
     visionName=Node('vision')
     global visPub
     visPub=visionName.create_publisher(Int16MultiArray,'visiondata',10)
     visSub=visionName.create_subscription(Image,
            'camImage',
            visSub_callback,
            10)
     #visPub=visionName.create_publisher(Int16MultiArray,'visiondata',10)
     rclpy.spin(visionName)
     
         

if __name__ == '__main__':
    main()
