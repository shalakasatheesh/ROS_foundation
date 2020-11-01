#! /usr/bin/env python

import roslib
import rospy
import actionlib

from shalaka_ros.msg import DoDishesAction, DoDishesGoal

def feedback_callback(msg):
    print('Feedback received:', msg)

def call_server():
    client = actionlib.SimpleActionClient('do_dishes', DoDishesAction)
    client.wait_for_server()
    
    # Set goal
    goal = DoDishesGoal()
    goal.number_of_minutes = int(input("Enter the total time available in seconds: "))

    # Send goal to server and ask for feedback
    client.send_goal(goal, feedback_cb=feedback_callback)

    # Wait for result
    client.wait_for_result()
    result = client.get_result()

    return result

if __name__ == '__main__':
    
    try:
        rospy.init_node('do_dishes_client')
    
        result = call_server()
        
        print('The result is:', result)

    except rospy.ROSInterruptException as e:
        print('Something went wrong:', e)
    
