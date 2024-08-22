#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def call_back(data):
    rospy.loginfo(rospy.get_caller_id()+"message recieved :%s",data.data)

def function():
    pub=rospy.Publisher("topic",String,queue_size=10)
    sub=rospy.Subscriber("topic",String,call_back)
    rospy.init_node("P_S",anonymous=True)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        message=input("enter the message:")
        pub.publish(message)
        rate.sleep()
        rospy.sleep(1)

    
if _name=="main_":
    try:
        function()
    except rospy.ROSInterruptException:
        pass