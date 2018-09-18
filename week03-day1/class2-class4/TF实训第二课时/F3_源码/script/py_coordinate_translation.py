#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import rospy
import tf
import math

if __name__=='__main__':
    rospy.init_node('py_coordinate_transfomation')

    q=tf.transformations.random_quaternion(rand=None)
    print '定义均匀随机四元数'
    print q