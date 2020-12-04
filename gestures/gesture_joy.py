#!/usr/bin/env python
import stretch_body.robot
import time
import pydub
from pydub import AudioSegment
from pydub.playback import play
from multiprocessing import Process


# robot=stretch_body.robot.Robot()

def joy_audio():
    print("Playing sound...")
    sound = AudioSegment.from_file("../audios/Joy.wav")
    sound.apply_gain(100)
    play(sound)
    return

def joy_gesture(robot):
    base_vel_fast_m = robot.base.params['motion']['fast']['vel_m']
    base_accel_fast_m = robot.base.params['motion']['fast']['accel_m']

    print("Doing gestures now...")

    robot.head.move_to('head_pan', -1)
    robot.head.move_to('head_tilt', 0)
    robot.base.translate_by(x_m=0.2, v_m=base_vel_fast_m)
    robot.lift.move_to(x_m=0.8)
    robot.arm.move_to(0.3)
    robot.push_command()
    time.sleep(3)
    robot.head.move_to('head_pan', 0)
    robot.head.move_to('head_tilt', 0.5)
    robot.arm.move_to(0.1)
    robot.lift.move_to(x_m=0.6)
    robot.push_command()

    time.sleep(3)

    # robot.stow()
    # robot.stop()
    return


if __name__ == "__main__":
    # Create two threads as follows
    try:
        robot=stretch_body.robot.Robot()
        p1 = Process(target=joy_audio)
        p1.start()

        robot.startup()
        p2 = Process(target=joy_gesture(robot))
        p2.start()

        robot.stop()
    except:
       print("Error: unable to start thread")
