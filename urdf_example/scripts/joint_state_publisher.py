#!/usr/bin/env python3

# importing the necessary dependencies
import rclpy
from rclpy.node import Node
# importing the JointState message from the sensor_msgs library
from sensor_msgs.msg import JointState

# class instance
class Joint_PublisherNode(Node):
    def __init__(self):
        super().__init__("Joint_Publisher_Node")
        
        # creating the publisher with topic /joint_states
        self.joint_publisher = self.create_publisher(JointState,"joint_states", 10)

        self.timer = self.create_timer(0.3,self.callback_publisher) #timer frequency should be same as when you create rate  
        
        self.get_logger().info("Joint_Publisher_Node has started: ")
        
        # creating the rate to publish the message to the topic on rviz
        self.loop_rate = self.create_rate(30) # rate should be same as the timer frequency

    def callback_publisher(self):

        # The self.get_clock().now() method in ROS2 Python is used to retrieve the current time from the ROS2 clock.
        now = self.get_clock().now()

        # message type from imported library is JointState
        msg = JointState()
        # message interface for JointState
        # std_msgs/Header header
        # 	builtin_interfaces/Time stamp
        # 		int32 sec
        # 		uint32 nanosec
        # 	string frame_id

        # string[] name
        # float64[] position
        # float64[] velocity
        # float64[] effort
        # The self.get_clock().now() 
        # method in ROS2 Python is used to retrieve the current time from the ROS2 clock. 
        msg.header.stamp = now.to_msg()
        # name of the joints
        msg._name = ['slider_joint' , 'new_link_joint']
        # position of the joint
        msg.position = [1.90 , 2.0]
        # publishing the state values to the joints mentioned in the above name[]
        self.joint_publisher.publish(msg)
        # sleep method of create_rate is used to keep the node from
        # publishing data and give it necessary time to calculate the functions, for which the
        # node is designed for
        self.loop_rate.sleep()
        

# #################################################################################################################################


# to add new joint states to the robot get all the name of the robot joints and know their limits 
# if they are prismatic or revolute joints

# adding new states for the joints using JointState message from sensor_msg.msg
# 
# name = ["joint_1", "joint_2", "joint_3"]      name in line 31 takes string type array of joint names
# position = [0.1, 0.4, 05]                     position in line 33 takes an array of float values as joint position

# ##################################################################################################################################


def main(args = None):
    rclpy.init(args = args)
    node = Joint_PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()