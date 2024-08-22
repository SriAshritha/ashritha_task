#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
last_message = ""

def node1_callback(msg):
    if msg.data != last_message:
        rospy.loginfo("Node 1 received: %s", msg.data)

def node1():
    global last_message
    rospy.init_node('node1', anonymous=True)
    pub = rospy.Publisher('/chat_topic', String, queue_size=10)
    rospy.Subscriber('/chat_topic', String, node1_callback)
    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        message = input("enter the message in node 1:")
        rospy.loginfo("Node 1 sent: %s", message)
        pub.publish(message)
        last_message = message
        rospy.sleep(1)
        rate.sleep()

if _name_ == '_main_':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass