#!/usr/bin/env python
 #license removed for brevity
import rospy
from rostask.msg import numbers
def talker():
    pub = rospy.Publisher('chatter', numbers, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
    	msg = numbers()
    	msg.a = 1
    	msg.b = 2
    	pub.publish(msg)
    	rate.sleep()
	
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
