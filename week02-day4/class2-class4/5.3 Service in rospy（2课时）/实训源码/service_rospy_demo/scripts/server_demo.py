#!/usr/bin/env python
# coding:utf-8

# 上面指定编码utf-8，使python能够识别中文

# 加载必需模块，注意service模块的加载方式，from 包名.srv import * 获取刚刚定义的服务
# 其中srv指的是在包根目录下的srv文件夹，也即srv模块
import rospy
from service_rospy_demo.srv import *

def server_srv(): 
    # 初始化节点，命名为 "greetings_server"
    rospy.init_node("greetings_server")
    # 定义service的server端，service名称为"greetings"， service类型为Greeting_demo
    # 收到的request请求信息将作为参数传递给handle_function进行处理
    s = rospy.Service("greetings", Greeting_demo, handle_function)
    print "Ready to handle the request:"
    # 用来触发所有的topic或者service，必须有
    rospy.spin()

# Define the handle function to handle the request inputs
def handle_function(req):
    
    # 注意我们是如何调用request请求内容的，是将其认为是一个对象的属性，通过对象调用属性，在我们定义
    # 的Greeting_demo类型的service中，request部分的内容包含两个变量，一个是字符串类型的name，另外一个是整数类型的age
    print "Hi Server, my name is %s and I'm %s years old"%(req.name,req.age)

    # 返回一个Greeting_demoResponse实例化对象，其实就是返回一个response的对象，其包含的内容为我们再Greeting_demo.srv中定义的
    # response部分的内容，我们定义了一个string类型的变量，因此，此处实例化时传入字符串即可
    return Greeting_demoResponse("Hi %s"%req.name)

# 如果单独运行此文件，则将上面定义的server_srv作为主函数运行
if __name__=="__main__":
    server_srv()
