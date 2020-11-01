#!/usr/bin/env python

import rospy
from shalaka_ros.srv import GetCalculator, GetCalculatorResponse

def handle_request(req):

    answer = 0
    possibility = False

    if (req.operation == '+'):
        try:
            answer = int(req.operand1) + int(req.operand2)
            possibility = True
        except:
            pass

    elif (req.operation == '-'):
        try:
            answer = int(req.operand1) - int(req.operand2)
            possibility = True
        except:
            pass
        
    elif (req.operation == '*'):
        try:
            answer = int(req.operand1) * int(req.operand2)
            possibility = True
        except:
            pass
        
    elif (req.operation == '/'):
        try:
            answer = int(req.operand1) / int(req.operand2)
            possibility = True
        except:
            pass

    rospy.loginfo("Returning result: %f" % answer)
    rospy.loginfo("Returning verdict: %s" % possibility)

    return GetCalculatorResponse(answer, possibility)
    

def server():
    rospy.init_node("calculator_server")
    rospy.Service('get_answer', GetCalculator, handle_request)
    rospy.loginfo("Server ready for calculation")

    rospy.spin()

if __name__=="__main__":
    server()