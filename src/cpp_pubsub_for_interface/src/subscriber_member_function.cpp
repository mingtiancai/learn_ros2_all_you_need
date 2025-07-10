#include <functional>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "tutorial_interfaces_demo/msg/num.hpp"                                       // CHANGE

using std::placeholders::_1;

class MinimalSubscriber : public rclcpp::Node
{
public:
  MinimalSubscriber()
  : Node("minimal_subscriber")
  {
    auto topic_callback = [this](const tutorial_interfaces_demo::msg::Num & msg){     // CHANGE
      RCLCPP_INFO_STREAM(this->get_logger(), "I heard: '" << msg.num << "'");    // CHANGE
    };
    subscription_ = this->create_subscription<tutorial_interfaces_demo::msg::Num>(    // CHANGE
      "topic", 10, topic_callback);
  }

private:
  rclcpp::Subscription<tutorial_interfaces_demo::msg::Num>::SharedPtr subscription_;  // CHANGE
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();
  return 0;
}