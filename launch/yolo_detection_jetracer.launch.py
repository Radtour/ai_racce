from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ai_race',
            namespace='ai_race',
            executable='motor_jetracer',
            name='ai_race_motor'
        ),
        Node(
            package='ai_race',
            namespace='ai_race',
            executable='camera_pub',
            name='ai_race_camera_pub'
        ),
        Node(
            package='ai_race',
            namespace='ai_race',
            executable='yolo_jetracer',
            name='ai_race_yolo'
        )
    ])