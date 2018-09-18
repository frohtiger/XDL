#include <ros/ros.h>
#include <tf/transform_listener.h>
#include <geometry_msgs/Twist.h>

int main(int argc, char** argv){
  ros::init(argc, argv, "tf_listener");
  ros::NodeHandle node;
  tf::TransformListener listener;
  ros::Rate rate(1);
  while (node.ok()){
    tf::StampedTransform transform;
    try{
      listener.lookupTransform("/base_link", "/link1",
                               ros::Time(0), transform);
                               //ros::Time(0)表示最近的一帧坐标变换，不能写成ros::Time::now()
    }
    catch (tf::TransformException &ex) {
      ROS_ERROR("%s",ex.what());
      ros::Duration(1.0).sleep();
      continue;
    }
    std::cout<<"输出的位置坐标：x="<<transform.getOrigin().x()<<",y="<<transform.getOrigin().y()<<",z="<<transform.getOrigin().z()<<std::endl;
    std::cout<<"输出的旋转四元数：w="<<transform.getRotation().getW()<<",x="<<transform.getRotation().getX()<<
    ",y="<<transform.getRotation().getY()<<",z="<<transform.getRotation().getZ()<<std::endl;
    rate.sleep();
  }
  return 0;
};
