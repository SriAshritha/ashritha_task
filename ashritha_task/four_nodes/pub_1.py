#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    pub=rospy.Publisher("t1",String,queue_size=10)
    rospy.init_node("publisher_1",anonymous=True)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown() :
        message=input("enter the message:")
        pub.publish(message)
        rate.sleep()

if _name=="main_":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass