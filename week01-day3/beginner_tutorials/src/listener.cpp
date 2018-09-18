#include "ros/ros.h"  
#include "std_msgs/String.h"  
#include "beginner_tutorials/stu.h"  
  
void chatterCallback(const beginner_tutorials::stu::ConstPtr& msg)  
{  
  ROS_INFO("name and date: [%s] [%d] ", msg->name.c_str(),msg->date);  
}  
  
int main(int argc, char **argv)  
{  
  
  ros::init(argc, argv, "listener");  
  
  ros::NodeHandle n;  
  
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);  
  
  ros::spin();  
  return 0;  
}  
