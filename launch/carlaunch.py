from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
         Node(
            package='autocar',
            #namespace='cameranode',
            executable='camera',
            name='camera'
        ),
         Node(
            package='autocar',
            #namespace='visionnode',
            executable='vision',
            name='vision'
        )
         
    ])