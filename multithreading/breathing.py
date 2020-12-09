#!/usr/bin/env python
import time

def breathing_gesture_head(robot):

    while(True):
        print("head0")
        robot.head.move_to('head_pan', -0.6, v_r= 0.1, a_r=0.5)

        print("head1")
        robot.head.move_to('head_tilt', 0.5, v_r= 0.1, a_r=0.5)

        print("head2")
        robot.head.move_to('head_pan', 0.8, v_r= 0.1, a_r=0.5)
        time.sleep(3)

        print("head3")
        robot.head.move_to('head_tilt', -0.4, v_r= 0.1, a_r=0.5)
        time.sleep(3)

        print("head4")
        robot.head.move_to('head_pan', -0.6, v_r= 0.1, a_r=0.5)
        time.sleep(3)

        print("head5")
        robot.head.move_to('head_tilt', 0.5, v_r= 0.1, a_r=0.5)
        time.sleep(3)

        print("head6")
        robot.head.move_to('head_pan', 0.8, v_r= 0.1, a_r=0.5)
        time.sleep(3)

        print("head7")
        robot.head.move_to('head_tilt', -0.4, v_r= 0.1, a_r=0.5)
        time.sleep(3)

    return

def breathing_gesture_wrist(robot):

    arm_vel_slow_m = robot.robot_params['wrist_yaw']['motion']['slow']['vel']
    arm_accel_slow_m = robot.robot_params['wrist_yaw']['motion']['slow']['accel']

    while(True):
        print("wrist1")
        robot.end_of_arm.move_to('wrist_yaw', -0.5, v_r=0.5, a_r=0.5)
        time.sleep(3)

        print("wrist2")
        robot.end_of_arm.move_to('wrist_yaw', 0.3, v_r=0.5, a_r=0.5)
        time.sleep(3)

        print("wrist3")
        robot.end_of_arm.move_to('wrist_yaw', -0.3, v_r=0.5, a_r=0.5)
        time.sleep(3)

        print("wrist4")
        robot.end_of_arm.move_to('wrist_yaw', 0.5, v_r=0.5, a_r=0.5)
        time.sleep(3)

        print("wrist5")
        robot.end_of_arm.move_to('wrist_yaw', 0.1, v_r=0.5, a_r=0.5)
        time.sleep(3)

    return

def breathing_gesture_lift(robot):

    lift_vel_slow_m = robot.lift.params['motion']['slow']['vel_m']
    lift_accel_slow_m = robot.lift.params['motion']['slow']['accel_m']

    while(True):
        print("lift1")
        robot.lift.move_to(x_m=0.8, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)
        robot.push_command()
        time.sleep(3)

        print("lift2")
        robot.lift.move_to(x_m=0.7, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)
        robot.push_command()
        time.sleep(3)

        print("lift3")
        robot.lift.move_to(x_m=0.5, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)
        robot.push_command()
        time.sleep(3)

        print("lift4")
        robot.lift.move_to(x_m=0.6, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)
        robot.push_command()
        time.sleep(3)

        print("lift5")
        robot.lift.move_to(x_m=0.7, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)
        robot.push_command()
        time.sleep(3)

    return

def breathing_gesture_base(robot):

    # base_vel_slow_m = robot.lift.params['motion']['slow']['vel_r']
    # base_accel_slow_m = robot.lift.params['motion']['slow']['accel_r']

    while(True):
        print("base1")
        robot.base.rotate_by(x_r=0.8, v_r=0.1, a_r=0.2)
        robot.push_command()
        time.sleep(5)

        print("base2")
        robot.base.rotate_by(x_r=-0.8, v_r=0.1, a_r=0.2)
        robot.push_command()
        time.sleep(5)

    return