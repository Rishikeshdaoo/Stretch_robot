#!/usr/bin/env python
import stretch_body.robot
import time
import pydub
from pydub import AudioSegment
from pydub.playback import play
from multiprocessing import Process


# robot=stretch_body.robot.Robot()

def fear_audio():
    print("Playing sound...")
    sound = AudioSegment.from_file("../audios/Fear_1.wav")
    sound.apply_gain(100)
    play(sound)
    return

def fear_gesture(robot):
    base_vel_fast_m = robot.base.params['motion']['fast']['vel_m']
    base_accel_fast_m = robot.base.params['motion']['fast']['accel_m']

    print("Doing gestures now...")

    # robot.startup()

    robot.head.move_to('head_pan', 3.1)
    robot.base.translate_by(x_m=-0.5, v_m=base_vel_fast_m, a_m=base_accel_fast_m)
    robot.lift.move_to(x_m=0.8)
    robot.arm.move_to(x_m=0.5)
    robot.push_command()
    time.sleep(3)

    robot.base.translate_by(x_m=-0.2, v_m=base_vel_fast_m, a_m=base_accel_fast_m)
    robot.lift.move_to(x_m=0)
    robot.arm.move_to(x_m=0.2)
    robot.push_command()

    time.sleep(4)

    # robot.stow()
    # robot.stop()

    return

if __name__ == "__main__":
    # Create two threads as follows
    try:
        robot=stretch_body.robot.Robot()
        robot.startup()

        p1 = Process(target=fear_audio)
        p1.start()
        p2 = Process(target=fear_gesture)
        p2.start()

        robot.stop()
    except:
       print("Error: unable to start thread")
