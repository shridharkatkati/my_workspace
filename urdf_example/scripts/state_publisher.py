#!/usr/bin/env python3

# importing the necessary dependencies
import rclpy
from rclpy.node import Node
# importing the JointState message from the sensor_msgs library
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from std_msgs.msg import Header

# class instance
class Joint_PublisherNode(Node):
    def __init__(self):
        super().__init__("Joint_Publisher_Node")
        self.joint_publisher = self.create_publisher(JointTrajectory,"/set_joint_trajectory", 10)

        self.timer = self.create_timer(0.3,self.callback_publisher) 
        self.get_logger().info("State_Publisher_Node has started: ")
        self.loop_rate = self.create_rate(30)


    def callback_publisher(self):
        
        now = self.get_clock().now()
        header = Header()
        header.frame_id = 'base'
        msg = JointTrajectory() 
        msg.header.stamp = now.to_msg()
        msg.joint_names = ['slider_joint','new_link_joint']
        point_msg = JointTrajectoryPoint()
        point_msg.positions = [1.5, 1.6]
        msg.points = [point_msg]
        self.joint_publisher.publish(msg)
        self.loop_rate.sleep()
        



def main(args = None):
    rclpy.init(args = args)
    node = Joint_PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()