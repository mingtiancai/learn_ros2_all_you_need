import rclpy
from rclpy.node import Node

import cv2

def main(args=None):
    rclpy.init(args=args)
    node = Node("node_object_webcam")
    node.get_logger().info("ROS2 DEMO")
    cap = cv2.VideoCapture("data/output.mp4")

    while rclpy.ok():
        ret, image = cap.read()
        if ret == True:
            cv2.imshow("object", image)
            cv2.waitKey(50)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
