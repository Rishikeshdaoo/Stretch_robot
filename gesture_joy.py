#!/usr/bin/env python
import stretch_body.robot
import time
import pydub
from pydub import AudioSegment
from pydub.playback import play
from multiprocessing import Process


robot=stretch_body.robot.Robot()

def joy_audio():
    print("Playing sound...")
    sound = AudioSegment.from_file("./audios/Joy.wav")
    sound.apply_gain(-6)
    play(sound)

    return

def joy_gesture():
    print("Doing gestures now...")

    robot.startup()

    robot.base.translate_by(x_m=1)
    robot.lift.move_to(x_m=1)
    robot.arm.move_to(0.5)
    robot.push_command()
    time.sleep(3)
    robot.base.translate_by(x_m=0)
    robot.lift.move_to(x_m=0)
    robot.push_command()

    time.sleep(4)

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
