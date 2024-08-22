# ashritha_task

The tasks given are actually interlinked.I think the main part lies in the concept of understanding the ros nodes and topics.The definition of ros is actually understood after completing the task. ROS is not an os but a framework which acts as a message broker between nodes.To have a communication between the nodes, topics are necessary.I came across the commands,for example rostopic list , rosnode list which checks and displays the current running list of topics and nodes respectively.I also used rqt_graph where I can visualize the graphical interactions between nodes and topics.I have also verified rqt_graph while using  turtlesim_node.

In this codes , I used rospy.sleep() so that there is a time gap between the messages sent by different nodes publishing or subscribing to the same topic.

The concepts I came across are the 
1. communication between multiple nodes,allowing data to be transferred between them using topics.
2. Creating a single node which can both publish as well as subscribe where the above task is performed by a single node.
3. upgradation of second task that is custom input is something called as chat application.This is what we see in our daily life.
4. some core concepts I got familiarized are node communication,topic handling,real time data exchange.
