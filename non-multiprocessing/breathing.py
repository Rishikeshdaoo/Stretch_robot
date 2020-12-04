#!/usr/bin/env python
import stretch_body.robot
import time

def breathing_audio():
    # Placeholder for a possible audio later
    return

def breathing_gesture(robot, choice):

    if(choice == 1):
        print(1)
        robot.head.move_to('head_pan', -0.5)

    elif(choice==2):
        print(2)
        robot.head.move_to('head_tilt', 0.8)

    elif(choice==3):
        print(3)
        robot.lift.move_to(x_m=0.5)

    elif(choice==4):
        print(4)
        robot.head.move_to('head_pan', 0.8)

    elif(choice == 5):
        print(5)
        robot.head.move_to('head_tilt', -0.6)

    elif(choice == 6):
        print(6)
        robot.lift.move_to(x_m=0.4)

    elif(choice == 7):
        print(7)
        robot.end_of_arm.move_to('wrist_yaw', 0)

    elif(choice == 8):
        print(8)
        robot.end_of_arm.move_to('wrist_yaw', 0.5)

    elif(choice == 9):
        print(9)
        robot.arm.move_to(x_m=0.2)

    elif(choice == 10):
        print(9)
        robot.arm.move_to(x_m=0.15)

    robot.push_command()

    time.sleep(3)

    return

def breathing_gesture_head(robot, choice):

    if(choice == 0):
        print("head0")
        robot.head.move_to('head_pan', -0.6, v_r= 0.1, a_r=0.5)

    elif(choice==1):
        print("head1")
        robot.head.move_to('head_tilt', 0.5, v_r= 0.1, a_r=0.5)

    elif(choice==2):
        print("head2")
        robot.head.move_to('head_pan', 0.8, v_r= 0.1, a_r=0.5)

    elif(choice==3):
        print("head3")
        robot.head.move_to('head_tilt', -0.4, v_r= 0.1, a_r=0.5)

    elif(choice==4):
        print("head4")
        robot.head.move_to('head_pan', -0.6, v_r= 0.1, a_r=0.5)

    elif(choice==5):
        print("head5")
        robot.head.move_to('head_tilt', 0.5, v_r= 0.1, a_r=0.5)

    elif(choice==6):
        print("head6")
        robot.head.move_to('head_pan', 0.8, v_r= 0.1, a_r=0.5)

    elif(choice==7):
        print("head7")
        robot.head.move_to('head_tilt', -0.4, v_r= 0.1, a_r=0.5)

    time.sleep(3)
    return

def breathing_gesture_wrist(robot, choice):

    arm_vel_slow_m = robot.arm.params['motion']['slow']['vel_m']
    arm_accel_slow_m = robot.arm.params['motion']['slow']['accel_m']

    if(choice == 0):
        print("wrist1")
        robot.end_of_arm.move_to('wrist_yaw', -0.5, v_r=0.5, a_r=0.5)

    elif(choice == 1):
        print("wrist2")
        robot.end_of_arm.move_to('wrist_yaw', 0.3, v_r=0.5, a_r=0.5)

    elif (choice == 2):
        print("wrist3")
        robot.end_of_arm.move_to('wrist_yaw', -0.3, v_r=0.5, a_r=0.5)

    elif (choice == 3):
        print("wrist4")
        robot.end_of_arm.move_to('wrist_yaw', 0.5, v_r=0.5, a_r=0.5)

    elif (choice == 4):
        print("wrist5")
        robot.end_of_arm.move_to('wrist_yaw', 0.1, v_r=0.5, a_r=0.5)

    time.sleep(3)
    return

def breathing_gesture_lift(robot, choice):

    lift_vel_slow_m = robot.lift.params['motion']['slow']['vel_m']
    lift_accel_slow_m = robot.lift.params['motion']['slow']['accel_m']

    if(choice == 0):
        print("lift1")
        robot.lift.move_to(x_m=0.8, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)

    elif(choice == 1):
        print("lift2")
        robot.lift.move_to(x_m=0.7, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)

    elif(choice == 2):
        print("lift3")
        robot.lift.move_to(x_m=0.5, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)

    elif(choice == 3):
        print("lift4")
        robot.lift.move_to(x_m=0.6, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)

    elif(choice == 4):
        print("lift5")
        robot.lift.move_to(x_m=0.7, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)

    robot.push_command()

    time.sleep(3)

    return

def breathing_gesture_base(robot, choice):

    # base_vel_slow_m = robot.lift.params['motion']['slow']['vel_r']
    # base_accel_slow_m = robot.lift.params['motion']['slow']['accel_r']

    if(choice == 0):
        print("base1")
        robot.base.rotate_by(x_r=0.8, v_r=0.1, a_r=0.2)

    elif(choice == 1):
        print("base2")
        robot.base.rotate_by(x_r=-0.8, v_r=0.1, a_r=0.2)

    robot.push_command()

    time.sleep(3)
    return


if __name__ == "__main__":
    # Create two threads as follows
    try:
        robot=stretch_body.robot.Robot()
        robot.startup()
        robot.stow()

        breathing_gesture(robot)
        robot.stop()
    except:
       print("Error: unable to start thread")
