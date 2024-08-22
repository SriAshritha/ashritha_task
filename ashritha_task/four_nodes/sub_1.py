#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def call_back(data):
    rospy.loginfo(rospy.get_caller_id()+"the message got heard is %s",data.data)

def listener():
    sub=rospy.Subscriber("t1",String,call_back,queue_size=10)
    rospy.init_node("Subscriber_1",anonymous=True)
    rospy.spin()

if _name=="main_":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass