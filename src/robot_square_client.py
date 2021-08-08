#! /usr/bin/env python

import rospkg
import rospy
from robot_square_pkg.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest
import time


rospy.init_node('service_move_bb8_in_square_custom_client')
rospy.wait_for_service('/move_bb8_in_square_custom')
move_bb8_in_square_service_client = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)
move_bb8_in_square_object = BB8CustomServiceMessageRequest()

move_bb8_in_square_object.side = 1
move_bb8_in_square_object.repetitions = 2

rospy.loginfo("Doing service call")
result = move_bb8_in_square_service_client(move_bb8_in_square_object)
rospy.loginfo(str(result))

move_bb8_in_square_object.side = 2
move_bb8_in_square_object.repetitions = 1

rospy.loginfo("Doing service call")
result = move_bb8_in_square_service_client(move_bb8_in_square_object)
rospy.loginfo(str(result))

rospy.loginfo("End of Service call..")

