#!/usr/bin/env python
import stretch_body.robot
import time
import pydub
from pydub import AudioSegment
from pydub.playback import play
from multiprocessing import Process


robot=stretch_body.robot.Robot()

base_vel_fast_m = robot.base.params['motion']['fast']['vel_m']
base_accel_fast_m = robot.base.params['motion']['fast']['accel_m']

def joy_audio():
    print("Playing sound...")
    sound = AudioSegment.from_file("./audios/Joy.wav")
    sound.apply_gain(100)
    play(sound)

    return

def joy_gesture():
    print("Doing gestures now...")

    robot.startup()

    robot.head.move_to('head_pan', -1)
    robot.head.move_to('head_tilt', 0)
    robot.base.translate_by(x_m=0.5, v_m=base_vel_fast_m, a_m=base_accel_fast_m)
    robot.lift.move_to(x_m=0.8)
    robot.arm.move_to(0.3)
    robot.push_command()
    time.sleep(3)
    robot.head.move_to('head_pan', 0)
    robot.head.move_to('head_tilt', 0.5)
    robot.arm.move_to(0.3)
    robot.lift.move_to(x_m=0.6)
    robot.push_command()

    time.sleep(3)

    robot.stow()
    robot.stop()
    return

# Create two threads as follows
try:
    p1 = Process(target=joy_audio)
    p1.start()
    p2 = Process(target=joy_gesture)
    p2.start()
except:
   print("Error: unable to start thread")
