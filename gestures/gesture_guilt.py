#!/usr/bin/env python
import stretch_body.robot
import time

# robot=stretch_body.robot.Robot()

def guilt_gesture(robot):
    arm_vel_slow_m = robot.arm.params['motion']['slow']['vel_m']
    arm_accel_slow_m = robot.arm.params['motion']['slow']['accel_m']
    arm_vel_default_m = robot.arm.params['motion']['default']['vel_m']
    arm_accel_default_m = robot.arm.params['motion']['default']['accel_m']
    arm_vel_fast_m = robot.arm.params['motion']['fast']['vel_m']
    arm_accel_fast_m = robot.arm.params['motion']['fast']['accel_m']

    robot.head.move_to('head_pan', 0)
    robot.head.move_to('head_tilt', 0)

    print("Doing guilt gestures now...")

    # robot.startup()

    robot.head.move_to('head_pan', 1)
    time.sleep(1)
    robot.head.move_to('head_pan', -1)
    time.sleep(2)
    robot.head.move_to('head_pan', 1)
    time.sleep(1)
    robot.head.move_to('head_pan', -1)
    time.sleep(2)
    robot.head.move_to('head_tilt', -0.5)
    time.sleep(1)

    robot.base.rotate_by(x_r=-3.14)
    time.sleep(3)
    robot.push_command()
    robot.base.translate_by(x_r=-1)
    time.sleep(3)
    robot.push_command()

    # robot.stow()
    # robot.stop()

    return

if __name__ == "__main__":
    try:
        robot=stretch_body.robot.Robot()
        robot.startup()
        robot.stow()

        guilt_gesture(robot)

        robot.stop()
    except:
       print("Error: something went wrong in the code")
