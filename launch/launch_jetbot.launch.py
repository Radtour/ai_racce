from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ai_race',
            namespace='ai_race',
            executable='teleop_gamepad',
            name='ai_race_teleop'
        ),
        Node(
            package='ai_race',
            namespace='ai_race',
            executable='motor_jetbot',
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
            executable='flask_server',
            name='ai_race_flask_server'
        ),
        Node(
            package='ai_race',
            namespace='ai_race',
            executable='line_follower',
            name='ai_race_line_follower'
        )
    ])