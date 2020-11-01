#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def turtle_node():

    # Create a publisher with /turtle1/cmd_vel as topic
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    displacement = Twist()

    # Initialize node
    rospy.init_node('turtle_node', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        # Read input
        instruction = input("Next input: ")

        # Log input
        rospy.loginfo(displacement)

        if instruction == "w":
            displacement.linear.y = 1

        elif instruction == "a":
            displacement.linear.x = -1
            
        elif instruction == "d":
            displacement.linear.x = 1
            
        elif instruction == "s":
            displacement.linear.y = -1
            

        # Publish input
        pub.publish(displacement)

        rate.sleep()

if __name__ == "__main__":
    try:
        turtle_node()
    except rospy.ROSInterruptException:
        pass

