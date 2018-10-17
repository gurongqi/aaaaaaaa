#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import time

class RobotController(object):
    def __init__(self):
        rospy.init_node('robot_controller',
                        anonymous=True)
        self.robot_controller=moveit_commander.RobotCommander()

    def run(self):
        group_names=self.robot_controller.get_group_names()
        print 'all groups: ',group_names
        controll_groups = []
        for group_name in group_names:
            group = moveit_commander.MoveGroupCommander(group_name)
            controll_groups.append(group)
        print 'robot state: ',self.robot_controller.get_current_state()
        # print controll_groups[0].get_planning_frame()
        joint_value = controll_groups[0].get_current_joint_values()
        joint_value[0] = -1.0
        controll_groups[0].go(joint_value,wait=False)

if __name__=='__main__':
    robot_contoller=RobotController()
    robot_contoller.run()