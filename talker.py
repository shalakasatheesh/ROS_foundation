#!/usr/bin/env python


# publishing msgs into a topic

import rospy
from std_msgs.msg import String # only for prototype purposes

def talker():

    # Create a publisher with following parameters (topic name, topic type, queue_size)
    # queue size: how many msgs should be saved before dropping messages
    # latch: used when you have a publisher that's publishing msgs very slowly
    pub = rospy.Publisher('chatter', String, queue_size=10)
    
    # Register node. Node name is talker (HAS TO BE UNIQUE) here
    # If you want to launch multiple instances of the same node, set anonymous = true
    rospy.init_node('talker', anonymous=True)

    # To control the amount of time that passes b/w msgs that we're sending
    rate = rospy.Rate(10)

    # While roscore is still running execute the following block of code
    while not rospy.is_shutdown():
        message = "The time is: %s" % rospy.get_time() 

        # Recording log messages
        rospy.loginfo(message)

        # Publish the message with the publisher
        # Caveat:: ? 
        pub.publish(message)
        
        rate.sleep()





if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass