import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

#camset
bridge=CvBridge()
def cv2_to_imgmsg(cv_image):
    img_msg = Image()
    img_msg.height = cv_image.shape[0]
    img_msg.width = cv_image.shape[1]
    img_msg.encoding = "bgr8"
    img_msg.is_bigendian = 0
    img_msg.data = cv_image.tostring()
    img_msg.step = len(img_msg.data) // img_msg.height # That double line is actually integer division, not a comment
    return img_msg
class cameraPub(Node):

    def __init__(self):
        super().__init__('camera')
        self.camPub= self.create_publisher(Image, 'camImage', 10)
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        cap = cv2.VideoCapture(0)
        ret,img=cap.read()
        cv2.imshow('camera',img)
        #im=cv2_to_imgmsg(img)
        im=bridge.cv2_to_imgmsg(img,encoding="bgr8")
        self.get_logger().info("hi")
        self.camPub.publish(im)
        cv2.waitKey(10)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    camera_publisher= cameraPub()
    rclpy.spin(camera_publisher)
###  WITHOUT USING CLASS & TIMER
# def main():
#     rclpy.init()
#     camName=Node('camera')
#     camPub=camName.create_publisher(Image,'camImage',10)
#     cap = cv2.VideoCapture(0)
#     while(True):
#         ret,img=cap.read()
#         cv2.imshow('camera',img)
#         im=bridge.cv2_to_imgmsg(img,encoding="bgr8")
#         camPub.publish(im)
#         if cv2.waitKey(1) % 0xFF==ord('q'):
#             break



if __name__ == '__main__':
    main()