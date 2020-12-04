#!/usr/bin/env python
import stretch_body.robot
import time
import pydub
from pydub import AudioSegment
from pydub.playback import play
from multiprocessing import Process

# robot=stretch_body.robot.Robot()

def disgust_audio():
    print("Playing sound...")
    sound = AudioSegment.from_file("../audios/Disgust_1.wav")
    sound.apply_gain(100)
    play(sound)
    return

def disgust_gesture(robot):
    arm_vel_slow_m = robot.arm.params['motion']['slow']['vel_m']
    arm_accel_slow_m = robot.arm.params['motion']['slow']['accel_m']
    arm_vel_default_m = robot.arm.params['motion']['default']['vel_m']
    arm_accel_default_m = robot.arm.params['motion']['default']['accel_m']
    arm_vel_fast_m = robot.arm.params['motion']['fast']['vel_m']
    arm_accel_fast_m = robot.arm.params['motion']['fast']['accel_m']

    print("Doing gestures now...")

    # robot.startup()

    robot.head.move_to('head_pan', 2.14)
    robot.end_of_arm.move_to('wrist_yaw', 0)
    robot.base.rotate_by(x_r=1)
    robot.lift.move_to(x_m=1)
    robot.arm.move_to(x_m=0.3, v_m=arm_vel_fast_m)
    robot.push_command()
    time.sleep(3.5)
    robot.head.move_to('head_pan', -1)
    robot.base.rotate_by(x_r=-1)
    robot.lift.move_to(x_m=0.7)
    robot.arm.move_to(x_m=0)
    robot.push_command()
    time.sleep(6)

    # robot.stow()
    # robot.stop()

    return

if __name__ == "__main__":
    # Create two threads as follows
    try:
        robot=stretch_body.robot.Robot()
        robot.startup()
        robot.stow()

        p1 = Process(target=disgust_audio)
        p1.start()
        p2 = Process(target=disgust_gesture(robot))
        p2.start()

        robot.stop()
    except:
       print("Error: unable to start thread")
