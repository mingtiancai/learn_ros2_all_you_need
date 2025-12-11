from tutorial_interfaces.srv import AddThreeInts                                                           # CHANGE

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(AddThreeInts, 'add_three_ints', self.add_three_ints_callback)       # CHANGE

    def add_three_ints_callback(self, request, response):
        response.sum = request.a + request.b + request.c                                                   # CHANGE
        self.get_logger().info('Incoming request\na: %d b: %d c: %d' % (request.a, request.b, request.c))  # CHANGE

        return response

def main(args=None):
    try:
        rclpy.init(args=args)
        minimal_service = MinimalService()
        rclpy.spin(minimal_service)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()