import serial
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16MultiArray,Int8MultiArray
def serSub_callback(msg):
    global arr
    arr=msg.data
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = '/dev/ttyUSB0'
    ser.open()
    values = bytearray(arr)
    
    ser.write(values)   

    total = 0

    while total < len(values):
        print(ord(ser.read(1)))
        total=total+1
    ser.close()

def main():
    rclpy.init()
    serialNode=Node('serial')
    serSub=serialNode.create_subscription(Int16MultiArray,
            'visionData',
            serSub_callback,
            10)
    # ser = serial.Serial()
    # ser.baudrate = 115200
    # ser.port = '/dev/ttyUSB0'
    # ser.open()
    # values = bytearray(arr)
    # ser.write(values)

    # total = 0

    # while total < len(values):
    #     print(ord(ser.read(1)))
    #     total=total+1

    # ser.close()
    rclpy.spin(serialNode)
if __name__ == '__main__':
    main()
