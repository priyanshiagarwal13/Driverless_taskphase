#!/usr/bin/env python
import rospy
from rostask2.msg import num
from rostask2.msg import RT2String

rt2 = RT2String()
def isPalindrome(str):

    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return 0
    return 1
            
str = rt2.AABAA

ans = 0
pub = rospy.Publisher('random2', num, queue_size=10)
def callback(data):
    rospy.loginfo(isPalindrome(data.AABAA))
    ans = isPalindrome(data.AABAA)
    rt2 = data
    
    n = num()
    n.d = ans
    rospy.loginfo(n)
    pub.publish(n)

def node2():
    
    rospy.init_node('node2', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    rospy.Subscriber("random", RT2String, callback)
    rospy.spin()
    
    #while not rospy.is_shutdown():
        #rospy.loginfo(rt2)
        #n = num()
        #n.d = ans
        #if (isPalindrome(rt2.AABAA)==1):
         #   n.d = 1
        #else:
         #   n.d = 0
        #rospy.loginfo(n)
        #pub.publish(n)
        #rate.sleep()


if __name__ == '__main__':
    node2()

