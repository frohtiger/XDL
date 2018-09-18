#!/usr/bin/env python
# coding:utf-8

# 上面指定编码utf-8，使python能够识别中文
import rospy
from service_rospy_demo.srv import *    #导入定义的服务


def kfc_server_srv():
    # 初始化节点，命名为 "kfc_server"
    rospy.init_node("kfc_server")
    #定义服务节点名称，服务的类型，处理函数
    s = rospy.Service("kfc_order", KFC_demo, handle_order_function)
    
    print "ready to order:"
    rospy.spin()
  
#定义处理函数
def handle_order_function(req):
    
    #print "The guest wants %s %s. The unit price of the %s is %s."%(req.number,req.menu,req.menu,req.price)
    #计算客人的账单
    bill = req.price * req.number
    return KFC_demoResponse(bill)
    
# 如果单独运行此文件，则将上面定义的kfc_server_srv作为主函数运行   

if __name__=="__main__":
    kfc_server_srv()
