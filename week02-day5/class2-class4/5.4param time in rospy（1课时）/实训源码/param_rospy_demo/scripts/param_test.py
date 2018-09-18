#!/usr/bin/env python
# coding:utf-8

import rospy
from std_msgs.msg import String

def param_test():
    #初始化参数节点
    #while not rospy.is_shutdown():
    rospy.init_node('param_test')

    testglobal = rospy.get_param("test_global")
    print "%s is %s"%(rospy.resolve_name('test_global'), testglobal)

    myrobot = rospy.get_param("myrobot")
    print " the value of %s is %s"%(rospy.resolve_name('myrobot'), myrobot)
        
        
    #获取一组test1参数
    test1 = rospy.get_param('test1')
    p, i, d = test1['P'], test1['I'], test1['D']
    print "test1 are %s, %s, %s"%(p, i, d)
  
        
      #获取一组test2参数
    test2 = rospy.get_param('test2')
    pp, ii, dd = test2['PP'], test2['II'], test2['DD']
    print "test2 are %s, %s, %s"%(pp, ii, dd)

        
  
     #设置参数
    rospy.set_param('test_global', "I am changed")
    print "parameters have been changed"
    testglobal = rospy.get_param("test_global")
    print "after change,%s is %s" % (rospy.resolve_name('test_global'), testglobal)


if __name__=="__main__":
    param_test()
        
        
