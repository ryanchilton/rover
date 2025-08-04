import math
import time 
# ROS2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from mecanum_platform.motion_effort import MotionEffort

class TeleopInterface(Node):
    def __init__(self, robot_interface):
        rclpy.init(args=None)
        super().__init__('teleop_node')
        self.joy_subscriber = self.create_subscription(Joy, 'joy', self.joy_callback, 10)
        self.platform = robot_interface

    def joy_callback(self, msg):
        self.print_controller_state(msg)
        # Process joystick input and control the platform
        effort = MotionEffort(
            linear_x=msg.axes[3],  # Forward/backward
            linear_y=-msg.axes[2],  # Left/right
            rotational_z=msg.axes[0]  # Rotation
        )
        self.platform.twist(effort)


    def print_controller_state(self, msg):
        # Print the current state of the controller
        self.get_logger().info('Controller state: {}'.format(msg))

    def loop(self):
        # Main loop to keep the node running
        rclpy.spin(self) # Keep the node alive
        self.destroy_node() # Destroy the node when done
        rclpy.shutdown() # Shutdown rclpy