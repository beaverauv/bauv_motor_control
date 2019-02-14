#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64

def pusher(data):
	print(data.orientation.z)
	yaw_plant_pub.publish(data.orientation.z)
	#global first_time
	#if first_time == 1:
	#	first_time = 0

def main():
	rospy.init_node('value_Feeder', anonymous=True)
	rospy.Subscriber('imu/imu', Imu, pusher)
	yaw_setpoint_pub.publish(0)
	rospy.spin()

if __name__ == '__main__':
	first_time = True
	yaw_plant_pub = rospy.Publisher('yaw_plant', Float64, queue_size=10)
	yaw_setpoint_pub = rospy.Publisher('yaw_setpoint', Float64, queue_size=10)
	main()
