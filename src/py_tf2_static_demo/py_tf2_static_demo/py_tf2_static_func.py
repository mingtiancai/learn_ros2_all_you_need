import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from transforms3d.euler import euler2quat
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster


class StaticTFBroadcaster(Node):
    def __init__(self, name):
        super().__init__(name)
        self.tf_broadcaster = StaticTransformBroadcaster(self)

        static_transformStamped = TransformStamped()
        static_transformStamped.header.stamp = self.get_clock().now().to_msg()
        static_transformStamped.header.frame_id = "world"
        static_transformStamped.child_frame_id = "house"
        static_transformStamped.transform.translation.x = 10.0
        static_transformStamped.transform.translation.y = 5.0
        static_transformStamped.transform.translation.z = 0.0

        quat = euler2quat(0.0, 0.0, 0.0)

        static_transformStamped.transform.rotation.x = quat[0]
        static_transformStamped.transform.rotation.y = quat[1]
        static_transformStamped.transform.rotation.z = quat[2]
        static_transformStamped.transform.rotation.w = quat[3]

        self.tf_broadcaster.sendTransform(static_transformStamped)


def main(args=None):
    rclpy.init(args=args)
    node = StaticTFBroadcaster("static_tf_broadcaster")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
