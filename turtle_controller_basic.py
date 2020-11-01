#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def talker():

    # Create a publisher with topic and msgtype
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    
    # Initialise node
    rospy.init_node('turtle_controller', anonymous=True)

    rate = rospy.Rate(10)
    
    vel = Twist()

    # Static velocities
    # lin_vel = 2
    # ang_vel = 2

    # Dynamic velocities with parameters
    lin_vel = rospy.get_param("linear_vel", 2.0)
    ang_vel = rospy.get_param("angular_vel", 2.0)

    # While roscore is still running execute the following block of code
    while not rospy.is_shutdown():

        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0

        vel.angular.z = 0
        vel.angular.z = 0
        vel.angular.z = ang_vel

        # Publish the message with the publisher
        pub.publish(vel)
        rate.sleep()


if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass