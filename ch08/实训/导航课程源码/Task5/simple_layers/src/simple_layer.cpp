    #include<simple_layers/simple_layer.h>  
    #include <pluginlib/class_list_macros.h>  
      
    PLUGINLIB_EXPORT_CLASS(simple_layer_namespace::SimpleLayer, costmap_2d::Layer)  //注册插件
      
    using costmap_2d::LETHAL_OBSTACLE;//类型：占有  
      
    namespace simple_layer_namespace  
    {  
      
    SimpleLayer::SimpleLayer() {}  
      
    void SimpleLayer::onInitialize()  
    {  
      ros::NodeHandle nh("~/" + name_);//定义节点  
      current_ = true;       
      dsrv_ = new dynamic_reconfigure::Server<costmap_2d::GenericPluginConfig>(nh);  
      dynamic_reconfigure::Server<costmap_2d::GenericPluginConfig>::CallbackType cb = boost::bind(  
          &SimpleLayer::reconfigureCB, this, _1, _2);//订阅插件服务
      dsrv_->setCallback(cb);//回调函数  
    }  
      
      
    void SimpleLayer::reconfigureCB(costmap_2d::GenericPluginConfig &config, uint32_t level)  
    {  
      enabled_ = config.enabled;//使能插件功能  
    }  
     
    void SimpleLayer::updateBounds(double origin_x, double origin_y, double origin_yaw, double* min_x,  
                                               double* min_y, double* max_x, double* max_y)  
    {  
      if (!enabled_)  
        return;  
      //障碍点位置
      mark_x_ = origin_x + cos(origin_yaw);  
      mark_y_ = origin_y + sin(origin_yaw);  
      //判断障碍点位置，避免出地图
      *min_x = std::min(*min_x, mark_x_);
      *min_y = std::min(*min_y, mark_y_);  
      *max_x = std::max(*max_x, mark_x_);  
      *max_y = std::max(*max_y, mark_y_);  
    }  
    /*更新costmap*/
    void SimpleLayer::updateCosts(costmap_2d::Costmap2D& master_grid, int min_i, int min_j, int max_i,  
                                              int max_j)  
    {  
      if (!enabled_)  
        return;  
      unsigned int mx;  
      unsigned int my;  
      if(master_grid.worldToMap(mark_x_, mark_y_, mx, my)){  
         master_grid.setCost(mx, my, LETHAL_OBSTACLE);//设置cost点  
      }  
    }  
    } // end namespace  
