#!/usr/bin/env python

import rospy
from shalaka_ros.srv import GetCalculator, GetCalculatorResponse

def get_answer_client(operation, operand1, operand2):
    rospy.wait_for_service("get_answer")
    try:
        get_answer = rospy.ServiceProxy("get_answer", GetCalculator)
        response = get_answer(operation, operand1, operand2)
        return response.result, response.verdict
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s"%e)

if __name__ == "__main__":
    rospy.init_node("random_client", anonymous=True)
    while not rospy.is_shutdown():
        try:
            operand1 = int(input("operant 1: "))
            operand2 = int(input("operant 2: "))
        except:
            print("Enter a valid number!")
            break
        operation = input("Operation: ")
        rospy.loginfo("Requesting calculation")
        rospy.loginfo("Results of the calculation: %.2f, %s"%get_answer_client(operation, operand1, operand2))
