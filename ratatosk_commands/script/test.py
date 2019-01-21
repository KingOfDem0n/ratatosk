#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan

def drive(left, right):
	left_wheel_pub.publish(left)
	right_wheel_pub.publish(right)

def callback(data):
	drive(1,1)
	

rospy.init_node("test_drive")

left_wheel_pub = rospy.Publisher("/left_wheel_controller/command", Float64, queue_size=0)
right_wheel_pub = rospy.Publisher("/right_wheel_controller/command", Float64, queue_size=0)

laser = rospy.Subscriber("/scan", LaserScan, callback)

rospy.spin()
