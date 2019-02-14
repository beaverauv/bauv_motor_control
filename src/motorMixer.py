#!/usr/bin/env python
import rospy
from bauv_motor_control.msg import motor_Values

def main():
	rospy.init_node('motor_Mixer', anonymous=True)
	motor_publisher = rospy.Publisher('motor_Values', motor_Values, queue_size=10)
	rospy.spin()

if __name__ == '__main__':
	main()
