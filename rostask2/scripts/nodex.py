#!/usr/bin/env python
# license removed for brevity
import rospy
from rostask2.msg import RT2String
def node1():
    pub = rospy.Publisher('random', RT2String, queue_size=10)
    rospy.init_node('node1', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    rt2 = RT2String()
    rt2.AABAA = input("Enter the string: ")
    while not rospy.is_shutdown():
        rospy.loginfo(rt2.AABAA)
        pub.publish(rt2.AABAA)
        rate.sleep()
if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass
