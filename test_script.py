#!/usr/bin/env python
import stretch_body.robot
from stretch_body.hello_utils import ThreadServiceExit

robot=stretch_body.robot.Robot()
robot.startup()

x_move_base =0
x_move_arm =0
x_move_lift =0
x_move_head_pan =0
x_move_head_tilt =0
x_move_wrist_yaw =0
x_move_gripper =0

def update_my_behavior(status):
    #Update the joint commands based on the status data
    pass

try:
    while True:
        #Get a snapshot of the robot status data
        status=robot.get_status()

        #Compute new position targets based on sensor data
        update_my_behavior(status)

        #Queue new targets to devices
        robot.base.translate_by(x_move_base) #or robot.base.rotate_by()
        robot.arm.move_by(x_move_arm)
        robot.lift.move_by(x_move_lift)
        robot.head.move_by('head_pan',x_move_head_pan)
        robot.head.move_by('head_tilt',x_move_head_tilt)
        robot.end_of_arm.move_by('wrist_yaw',x_move_wrist_yaw)
        robot.end_of_arm.move_by('gripper',x_move_gripper)

        #Synchronized send of new position targets
        robot.push_command()

        #Wait for next control cycle
        time.sleep(0.1)
except (KeyboardInterrupt, SystemExit,ThreadServiceExit)
    pass

robot.stop()
