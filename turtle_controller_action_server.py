#! /usr/bin/env python

''' http://wiki.ros.org/turtlesim/Tutorials/Go%20to%20Goal '''

import roslib
import rospy
import actionlib

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

from shalaka_ros.msg import TurtleGoalAction, TurtleGoalFeedback, TurtleGoalResult

class MoveTurtleServer():

    # Feedback
    feedback = TurtleGoalFeedback()

    # Result
    result = TurtleGoalResult()

    def __init__(self):

        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)

        #  Define Server
        self.server = actionlib.SimpleActionServer('move_turtle_to_goal', TurtleGoalAction, execute_cb=self.execute_cb, auto_start=False)

        # Start server
        self.server.start()

        self.pose = Pose()
        self.rate = rospy.Rate(10)
        self.r = rospy.Rate(1)

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def steering_angle(self, goal):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return atan2(goal.goal_x - self.pose.y, goal.goal_y - self.pose.x)
    
    def angular_vel(self, goal, constant=6):
        return constant * (self.steering_angle(goal) - self.pose.theta)

    def linear_vel(self, goal, constant=1.5):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * self.euclidean_distance(goal)

    def euclidean_distance(self, goal):
        "Euclidean distance between current pose and the goal"
        return sqrt(pow((goal.goal_x - self.pose.x), 2) +
                    pow((goal.goal_x - self.pose.y), 2))
    
    def execute_cb(self, goal):

        distance_tolerance = 0.01
        vel_msg = Twist()

        success = True

        while self.euclidean_distance(goal) >= distance_tolerance:

            # check for preempt request
            if self.server.is_preempt_requested():

                rospy.loginfo('Preempted')
                self.server.set_preempted()
                success = False

                # stop turtle
                vel_msg.linear.x = 0
                vel_msg.angular.z = 0
                self.velocity_publisher.publish(vel_msg)
                
                break

            vel_msg.linear.x = self.linear_vel(goal)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(goal)

            self.feedback.present_x = self.pose.x
            self.feedback.present_y = self.pose.y

            self.velocity_publisher.publish(vel_msg)

            self.server.publish_feedback(self.feedback)

            # self.r.sleep()

        # Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        
        self.velocity_publisher.publish(vel_msg)
        

        if success:
            self.result.final_x = self.pose.x
            self.result.final_y = self.pose.y
            self.server.set_succeeded(self.result)


if __name__ == "__main__":
    
    #  Initialise action server
    rospy.init_node("move_tutle_to_goal_server")

    # Call an instance of MoveTurtleServer class
    server = MoveTurtleServer()
    rospy.spin()
