#!/usr/bin/env python

import rospy
import math
from topic_demo.msg import gps

def callback(gps):
        distance = math.sqrt(math.pow(gps.x, 2) + math.pow(gps.y, 2))
        rospy.loginfo('Listener: GPS distance=%f, state : %s', distance, gps.state)

def listener():
       rospy.init_node('pylistener')
       rospy.Subscriber('gps_info', gps, callback)
       rospy.spin()

if __name__ == '__main__':
       listener()
