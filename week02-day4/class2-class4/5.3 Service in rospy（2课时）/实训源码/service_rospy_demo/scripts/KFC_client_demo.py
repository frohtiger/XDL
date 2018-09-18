#!/usr/bin/env python
# coding:utf-8

# 上面的第二句指定编码类型为utf-8，是为了使python能够识别中文

# 加载所需模块
import sys  #sys模块包含了与Python解释器和它的环境有关的函数。
import rospy
from service_rospy_demo.srv import *

def kfc_client_srv(m,p,n):
    # 服务客户端不必是节点，所以不用调用rospy.init_node
    # 等待有可用的服务 "kfc_order"
    rospy.wait_for_service("kfc_order")
    
    #调用服务求解结果并将结果返回 
    try:
        # 定义service客户端，创建服务处理句柄.service名称为“kfc_order”，service类型为KFC_demo
        kfc_client = rospy.ServiceProxy("kfc_order",KFC_demo)     
        resp = kfc_client(m,p,n)
	
        #上述为简化风格，也可用正式的。
        #resp = kfc_client.call(KFC_demoRequest(m,p,n)
        return resp.bill
       
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
        return "%s [m p n]"%sys.argv[0]

# 如果单独运行此文件，则将上面函数kfc_client_srv()作为主函数运行
if __name__=="__main__":
    
    #判断客户端输入的参数是否符合条件 
         
    if len(sys.argv)==4:
       m=str(sys.argv[1])
       p=float(sys.argv[2])
       n=int(sys.argv[3])
       print "The guest wants %s %s. The unit price of the %s is %s."%(n,m,m,p)
       bill = kfc_client_srv(m,p,n)
    else:
       print usage()
       sys.exit(1)
    
    print "The guest has to pay %s yuan."% bill
