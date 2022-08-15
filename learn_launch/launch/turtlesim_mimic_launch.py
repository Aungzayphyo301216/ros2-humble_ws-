from http.server import executable
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription( [
        Node (
            package="turtlesim",
            executable="turtlesim_node",
            name="tt1",
        ),

        Node (
            package="turtlesim",
            executable="turtlesim_node",
             name="tt2",
             remappings=[
                ('turtle1/cmd_vel', 'turtle2/cmd_vel'),
            ]
        ),
        Node (
            package="turtlesim",
            executable="mimic",
            name="mimic",
            remappings=[
                ('/input/pose','turtle1/pose'),
                ('/output/cmd_vel','turtle2/cmd_vel'),
        ]

        )
])