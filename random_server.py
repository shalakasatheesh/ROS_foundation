#!/usr/bin/env python

import rospy
import random
from shalaka_ros.srv import GetRandomNumber, GetRandomNumberResponse

def handle_request(req):
    random_int = random.randint(req.start, req.stop)
    rospy.loginfo("Returning random number: %s" % random_int)
    return GetRandomNumberResponse(random_int)

def server():
    rospy.init_node("random_number_server")
    srv = rospy.Service('get_random_number', GetRandomNumber, handle_request)
    rospy.loginfo("Server ready for request")

    rospy.spin()

if __name__=="__main__":
    server()