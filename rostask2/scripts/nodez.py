#!/usr/bin/env python
import rospy
from rostask2.msg import num

def callback(n):
    rospy.loginfo(n)
    if (n.d==1):
    	print("Yes")
    else:
    	print("No")
def node3():
    rospy.Subscriber("random2", num, callback)
    rospy.init_node('node3', anonymous=True)
    rospy.spin()
if __name__ == '__main__':
    node3()
    
