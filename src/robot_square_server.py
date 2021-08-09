#! /usr/bin/env python

import rospy
from robot_square_pkg.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist
import time


def my_callback(request):
    rospy.loginfo("The service bb8 has been called")
    move_square = Twist()
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    
    if (request.side == 1):
        rospy.loginfo("running small square ")
        i = 0
        while i < request.repetitions:
            j = 0
            while j < 4:
                move_square.linear.x = 1
                pub.publish(move_square)
                time.sleep(2)
                move_square.linear.x = 0
                pub.publish(move_square)
                time.sleep(1)
                move_square.angular.z = 0.9
                pub.publish(move_square)
                time.sleep(2)
                move_square.angular.z = 0.0
                pub.publish(move_square)
                time.sleep(1)
            
                j = j + 1
            i = i + 1
        
    
    #time.sleep(8)
    rospy.loginfo("Finished small square ")
   

    if (request.side == 2):
        rospy.loginfo("The big square has started")
        
        i = 0
        while i < request.repetitions:
            j = 0
            while j < 4:
                move_square.linear.x = 2
                pub.publish(move_square)
                time.sleep(2)
                move_square.linear.x = 0
                pub.publish(move_square)
                time.sleep(1)
                move_square.angular.z = 0.9
                pub.publish(move_square)
                time.sleep(2)
                move_square.angular.z = 0.0
                pub.publish(move_square)
                time.sleep(1)
                j = j + 1
            i = i + 1
        
        
        rospy.loginfo("Finished big square ")

    
    else:
        pass

    move_square.linear.x = 0.0
    move_square.angular.z = 0.0
    pub.publish(move_square)
    rospy.loginfo("Finished service move_bb8_in_square_custom ")

    my_response = BB8CustomServiceMessageResponse()
    my_response.success = True
    return my_response
    
def main():
    rospy.init_node('service_move_bb8_in_square_custom_server')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    move_square = Twist()
    my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, my_callback)
    rate = rospy.Rate(1)
    rospy.loginfo("The service /move_bb8_in_square_custom is ready")
    rospy.spin()

if __name__ == '__main__':
    main()
