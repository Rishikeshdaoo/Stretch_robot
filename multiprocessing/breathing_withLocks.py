#!/usr/bin/env python
import stretch_body.robot

from multiprocessing import Lock
import time

lock = Lock()

def breathing_gesture_head(robot):

    lock.acquire()

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

    lock.release()

    time.sleep(3)
    return

def breathing_gesture_wrist(robot):

    arm_vel_slow_m = robot.arm.params['motion']['slow']['vel_m']
    arm_accel_slow_m = robot.arm.params['motion']['slow']['accel_m']

    lock.acquire()

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

    lock.release()

    time.sleep(3)

    return

def breathing_gesture_lift(robot):

    lift_vel_slow_m = robot.lift.params['motion']['slow']['vel_m']
    lift_accel_slow_m = robot.lift.params['motion']['slow']['accel_m']

    lock.acquire()

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

    lock.release()

    time.sleep(3)

    return