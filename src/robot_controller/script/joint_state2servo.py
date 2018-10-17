#!/usr/bin/env python

import roslib
import rospy
from sensor_msgs.msg import JointState
import time
from std_msgs.msg import UInt16MultiArray
from std_msgs.msg import MultiArrayDimension
import numpy as np
import copy
import serial
import time

class JointState2Servo(object):
    def __init__(self,joint_state_topic):
        self.joint_position=np.zeros((0))
        self.servo_status_send=serial.Serial('/dev/ttyUSB0',9600)
        self.joint_state_sub = rospy.Subscriber(joint_state_topic,
                                                JointState,
                                                self.callback,
                                                queue_size=1)
        self.previous_joint_position=np.zeros((0))

    def run(self):
        while not rospy.is_shutdown():
            time.sleep(0.05)
            if np.all(self.previous_joint_position==0):
                self.previous_joint_position=copy.deepcopy(self.joint_position)
                continue
            if np.all(self.joint_position==self.previous_joint_position):
                continue
            else:
                position=copy.deepcopy(self.joint_position)
            command_string=''
            for i in xrange(self.previous_joint_position.shape[0]):
                if self.previous_joint_position[i]==position[i]:
                    continue
                # if i==1 or i==4:
                #     servo_angle=int(position[i]/1.57)
                servo_angle=int(position[i]/1.57*1000+1500)
                command_string+=str(i)+'_'+str(servo_angle)+','
            command_string+='|'
            self.servo_status_send.write(command_string)
            self.previous_joint_position=copy.deepcopy(position)



    def callback(self,joint_state):
        self.joint_position=np.asarray(joint_state.position)
        # print type(self.joint_position)
        # print self.joint_position


if __name__ == '__main__':
    joint_state_topic='/joint_states'
    rospy.init_node('joint_state2servo', anonymous=True)
    jointstate2servo=JointState2Servo(joint_state_topic)
    jointstate2servo.run()