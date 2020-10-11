#!/usr/bin/env python
import stretch_body.robot
import time
import pydub
from pydub import AudioSegment
from pydub.playback import play
from multiprocessing import Process


robot=stretch_body.robot.Robot()

def disgust_audio():
    print("Playing sound...")
    sound = AudioSegment.from_file("./audios/Disgust_1.wav")
    sound.apply_gain(-6)
    play(sound)

    return

def disgust_gesture():
    print("Doing gestures now...")

    robot.startup()

    robot.base.rotate_by(x_r=1)
    robot.lift.move_to(x_m=1)
    robot.arm.move_to(0.8)
    robot.push_command()
    robot.head.move_to('head_pan', 1)
    time.sleep(4)
    robot.base.rotate_by(x_r=-1)
    robot.lift.move_to(x_m=0)
    robot.arm.move_to(0)
    robot.push_command()
    robot.head.move_to('head_pan', -1)
    time.sleep(4)

    robot.stop()

    return

# Create two threads as follows
try:
    p1 = Process(target=disgust_audio)
    p1.start()
    p2 = Process(target=disgust_gesture)
    p2.start()
except:
   print("Error: unable to start thread")
