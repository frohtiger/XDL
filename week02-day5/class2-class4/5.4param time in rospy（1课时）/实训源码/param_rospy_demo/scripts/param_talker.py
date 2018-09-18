#!/usr/bin/env python
# coding:utf-8

import rospy
from std_msgs.msg import String

def param_talker():
    
    #初始化参数节点
    rospy.init_node('param_talker')

    # 从参数服务器获取参数，在这个例子中，我们从三个不同的命名空间获取参数
    # 1) global (/global_example)
    # 2) parent (/foo/utterance)
    # 3) private (/foo/param_talker/topic_name)

    # 从全局命名空间获取一个参数/global parameter，
    global_example = rospy.get_param("/global_example")
    #写入日志，rospy.resolve_name用来获取/global_example的实际名称
    rospy.loginfo("%s is %s", rospy.resolve_name('/global_example'), global_example)
    
    # 从目前命令空间 parent namespace获取一个utterance参数
    utterance = rospy.get_param('utterance')
    rospy.loginfo("%s is %s", rospy.resolve_name('utterance'), utterance)
    
    # 从私有命名空间private namespace获取topic_name参数
    topic_name = rospy.get_param('~topic_name')
    rospy.loginfo("%s is %s", rospy.resolve_name('~topic_name'), topic_name)

    # 获取参数，如果没有，使用默认值default_value
    default_param = rospy.get_param('default_param', 'default_value')
    rospy.loginfo('%s is %s', rospy.resolve_name('default_param'), default_param)
    
    # 获取一组参数
    gains = rospy.get_param('gains')
    p, i, d = gains['P'], gains['I'], gains['D']
    rospy.loginfo("gains are %s, %s, %s", p, i, d)    

    # 设置一些参数
    rospy.loginfo('setting parameters...')
    rospy.set_param('bool_True', True)
    rospy.set_param('to_delete', 'baz')
    bool_True = rospy.get_param('bool_True')
    to_delete = rospy.get_param('to_delete')
    rospy.loginfo('%s is %s;%s is %s', rospy.resolve_name('bool_True'), bool_True,rospy.resolve_name('to_delete'), to_delete)
    rospy.loginfo('...parameters have been set')
    
    # 判断参数是否存在，如果to_delete存在，则删除，并输出日志信息，若不存在，则输出参数已被删除的信息
    if rospy.has_param('to_delete'):
        rospy.delete_param('to_delete')
        rospy.loginfo("deleted %s parameter"%rospy.resolve_name('to_delete'))
    else:
        rospy.loginfo('parameter %s was already deleted'%rospy.resolve_name('to_delete'))

    # 搜索参数，搜索由私有命名空间开始，向上到全局命名空间。
    param_name = rospy.search_param('global_example')
    rospy.loginfo('found global_example parameter under key: %s'%param_name)
    
    # publish the value of utterance repeatedly
    pub = rospy.Publisher(topic_name, String, queue_size=10)
    while not rospy.is_shutdown():
        pub.publish(utterance)
        rospy.loginfo(utterance)
        rospy.sleep(1)
        
if __name__ == '__main__':
    try:
        param_talker()
    except rospy.ROSInterruptException: pass
