from sympy import im
import cv_bridge
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class ImageSubscriber(Node):
    def __init__(self, name):
        super().__init__(name)
        self.sub = self.create_subscription(
            Image, "image_raw", self.listener_callback, 10
        )
        self.cv_bridge = CvBridge()

    def listener_callback(self, data):
        self.get_logger().info("receive video frame")
        image = self.cv_bridge.imgmsg_to_cv2(data, "bgr8")
        cv2.imshow("object", image)
        cv2.waitKey(50)


def main(args=None):
    rclpy.init(args=args)
    node = ImageSubscriber("topic_webcam_sub")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
