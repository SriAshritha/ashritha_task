#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
last_message = ""

def node2_callback(msg):
    if msg.data != last_message:
        rospy.loginfo("Node 2 received: %s", msg.data)

def node2():
    global last_message
    rospy.init_node('node2', anonymous=True)
    pub = rospy.Publisher('/chat_topic', String, queue_size=10)
    rospy.Subscriber('/chat_topic', String, node2_callback)
    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        message = input("enter the message in node 2:")
        rospy.loginfo("Node 2 sent: %s", message)
        pub.publish(message)
        last_message = message
        rospy.sleep(1)
        rate.sleep()

if _name_ == '_main_':
    try:
        node2()
    except rospy.ROSInterruptException:
        pass