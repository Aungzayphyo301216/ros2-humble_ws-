from http.server import executable
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription ([

        Node (
            package="turtlesim",
            executable="turtlesim_node",
            #namespace="turtlesim1",
            name="aa",
        
         ),
        Node (
            package="turtlesim",
            executable="turtlesim_node",
            #namespace="turtlesim2",
            name="bb",
            remappings=([
                ('turtle1/pose','turtle2/pose'),
                ('turtle1/cmd_vel','turtle2/cmd_vel')
            ])

            ),

            Node (
            package="turtlesim",
            executable="turtlesim_node",
            #namespace="turtlesim2",
            name="cc",
            remappings=([
                ('turtle1/pose','turtle3/pose'),
                ('turtle1/cmd_vel','turtle2/cmd_vel')
            ])

            ),
        
        
        Node (
            package="turtlesim",
            executable="mimic",
            name="mimic",
        
            remappings=([
                 ('input/pose', 'turtle1/pose'),
                ('output/cmd_vel', 'turtle2/cmd_vel'),
                
                
            ])
            ),
    
    
    ])