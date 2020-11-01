#! /usr/bin/env python

import roslib
import rospy
import actionlib

from shalaka_ros.msg import DoDishesAction, DoDishesFeedback, DoDishesResult

class DoDishesServer():

    def __init__(self):

        # Define server
        self.server = actionlib.SimpleActionServer('do_dishes', DoDishesAction, execute_cb=self.execute_cb, auto_start=False)

        # Start server
        self.server.start()

    # Define execute callback with goal
    def execute_cb(self, goal):

        success = True 
        last_dish_washed = '' # Feedback

        # Initialise feedback
        feedback = DoDishesFeedback()

        # Initialise result
        result = DoDishesResult()

        # Publish feedback every sec
        rate = rospy.Rate(1)

        # Give feedback for each iteration until goal is reached
        for i in range(1, goal.number_of_minutes+1):

            # Break loop when new goal recevied
            if self.server.is_preempt_requested():
                self.server.is_preempt_requested()
                success = False
                break
            
            # Define and publish feedback
            last_dish_washed = 'dish-' + str(i)
            feedback.last_dish_washed = last_dish_washed
            self.server.publish_feedback(feedback)
            rate.sleep()

        result.total_dishes_cleaned = i

        if success:
            self.server.set_succeeded(result)

if __name__ == '__main__':
    
    # Initialise action server 
    rospy.init_node('do_dishes_server')

    #  Call an instance of DoDishesServer class
    server = DoDishesServer()
    rospy.spin()
    

