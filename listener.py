#!/usr/bin/env python


# listen to a topic and process the incoming data

import rospy
from std_msgs.msg import String, UInt16

def callback(data):
    
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener():
    rospy.init_node('listener', anonymous=True)

    # Callback is a function that'll be called whenever the listener receives a msg
    rospy.Subscriber('chatter', String, callback)

    # Asking ros to run this code adn wait until you receive a msg
    rospy.spin()

if __name__ == '__main__':
    listener()

