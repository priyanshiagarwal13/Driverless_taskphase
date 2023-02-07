#!/usr/bin/env python
import rospy
from rostask.msg import numbers
def callback(data):
    rospy.loginfo(data.a + data.b)
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", numbers, callback)
    rospy.spin()
if __name__ == '__main__':
    listener()
