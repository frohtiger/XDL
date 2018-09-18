#include "ros/ros.h"  
#include "std_msgs/String.h"  
#include "beginner_tutorials/stu.h"  
#include <sstream>  
      


int main(int argc, char **argv)
{  
      ros::init(argc, argv, "talker");  
      ros::NodeHandle n;  
      ros::Publisher chatter_pub = n.advertise<beginner_tutorials::stu>("chatter", 1000);  
      ros::Rate loop_rate(10);
      int count = 0;
      while (ros::ok())
      {  
        beginner_tutorials::stu msg;
      
        std::stringstream ss;  
        ss << "john" << count;
        msg.name = ss.str();  
        msg.date = count;
         
      
        ROS_INFO("%s %d", msg.name.c_str(),msg.date);
      
        chatter_pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
        ++count;
      }  
      return 0;  
}  
