#!/usr/bin/env python

import rospy
from shalaka_ros.srv import GetRandomNumber, GetRandomNumberResponse

def get_random_number_client(start, stop):
    rospy.wait_for_service("get_random_number")
    try:
        get_random_number = rospy.ServiceProxy("get_random_number", GetRandomNumber)
        response = get_random_number(start, stop)
        return response.result
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s"%e)

if __name__ == "__main__":
    rospy.init_node("random_client", anonymous=True)
    while not rospy.is_shutdown():
        start = int(input("start: "))
        stop = int(input("stop: "))
        rospy.loginfo("Requesting a random int")
        rospy.loginfo("Random int: %s"%get_random_number_client(start, stop))
