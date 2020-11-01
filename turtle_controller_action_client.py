#! /usr/bin/env python

import roslib
import rospy
import actionlib

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

from shalaka_ros.msg import TurtleGoalAction, TurtleGoalGoal

def feedback_call(msg):
    print("Turtle is now at position: ", msg)

def call_server():
    client = actionlib.SimpleActionClient('move_turtle_to_goal', TurtleGoalAction)
    client.wait_for_server()

    # Set goal
    goal = TurtleGoalGoal()
    goal.goal_x = int(input("Enter target x-coord: "))
    goal.goal_y = int(input("Enter target y-coord: "))
    
    # Send goal to server and ask for feedback
    client.send_goal(goal, feedback_cb=feedback_call)

    # Wait for result
    client.wait_for_result()
    result = client.get_result()
    
    return result

if __name__ == '__main__':
    
    try:
        rospy.init_node('move_tutle_to_goal_client')
    
        result = call_server()
        
        print('The result is:', result)

    except rospy.ROSInterruptException as e:
        print('Something went wrong:', e)
