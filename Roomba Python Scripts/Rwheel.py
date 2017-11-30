#!/usr/bin/env python

from __future__ import print_function
from pycreate2 import Create2
import time

import rospy
from std_msgs.msg import Int32MultiArray

x = [0,0,0,0,0,0]

def callback(msg):
    print (msg.data)
    global x,x1
    x = msg.data
    x1 = x[0]+x[1]+x[2]+x[3]+x[4]+x[5]

rospy.init_node('Rwheel',anonymous=True)

rospy.Subscriber('Rsensor', Int32MultiArray, callback)
baud = {
		'default': 115200,
		'alt': 19200  # shouldn't need this unless you accidentally set it to this
	}

port = '/dev/ttyUSB0'
bot = Create2(port=port, baud=baud['default'])

	#bot.start()
	#bot.full()

while not rospy.is_shutdown():
	bot.drive_direct(100,100)
	if x[0]+x[1]+x[2]<x[3]+x[4]+x[5]:
		while x1!=0 and (not rospy.is_shutdown()):
                  bot.drive_direct(50,-50)
	if x[0]+x[1]+x[2]>x[3]+x[4]+x[5]:
        	while x1!=0 and (not rospy.is_shutdown()):
                  bot.drive_direct(-50,50)


rospy.spin()

if __name__ == '__main__':
       try:
           Rwheel()
       except rospy.ROSInterruptException:
           pass
