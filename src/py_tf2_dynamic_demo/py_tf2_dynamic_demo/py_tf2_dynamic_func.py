import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from transforms3d.euler import euler2quat
from tf2_ros import TransformBroadcaster
from turtlesim.msg import Pose


class TurtleTFBroadcaster(Node):
    def __init__(self, name):
        super().__init__(name)
        self.declare_parameter("turtlename", "turtle")
        self.turtlename = (
            self.get_parameter("turtlename").get_parameter_value().string_value
        )
        self.tf_broadcaster = TransformBroadcaster(self)
        self.subscription = self.create_subscription(
            Pose, f"/{self.turtlename}/pose", self.turtle_pose_callback, 1
        )

    def turtle_pose_callback(self, msg):
        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = "world"
        transform.child_frame_id = self.turtlename

        transform.transform.translation.x = msg.x
        transform.transform.translation.y = msg.y
        transform.transform.translation.z = 0.0

        q = euler2quat(0, 0, msg.theta)
        transform.transform.rotation.x = q[1]
        transform.transform.rotation.y = q[2]
        transform.transform.rotation.z = q[3]
        transform.transform.rotation.w = q[0]

        self.tf_broadcaster.sendTransform(transform)


def main(args=None):
    rclpy.init(args=args)
    node = TurtleTFBroadcaster("turtle_tf_broadcaster")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
