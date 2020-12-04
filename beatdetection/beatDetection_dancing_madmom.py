#!/usr/bin/env python

import stretch_body.robot
import time
import pydub
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
from multiprocessing import Process
from madmom.features.onsets import OnsetPeakPickingProcessor, RNNOnsetProcessor

robot=stretch_body.robot.Robot()
robot.startup()

robot.stow()

filename = "../audios/drum_90.wav"
proc = OnsetPeakPickingProcessor()
act = RNNOnsetProcessor()(filename)
onsets = proc(act)

interonsets = np.ediff1d(onsets)
interonsets = np.add.reduceat(interonsets, np.arange(0, len(interonsets), 4))

print(interonsets)

robot.head.move_to('head_tilt',-1)
robot.lift.move_to(0.50,10,10)
robot.end_of_arm.move_to('wrist_yaw',1)
robot.push_command()
time.sleep(3)

xrotate=3.14
xtilt=0.5
xpan=1
xwrist=1.5
#start

def head_bob(robot, times):

    c = 0

    while(True):
        robot.head.move_to('head_tilt', -0.2)
        time.sleep(times[c])
        robot.head.move_to('head_tilt', 0.2)
        time.sleep(times[c+1])

        c += 2

    return

def play_audio():
    print("Playing sound...")
    sound = AudioSegment.from_file(filename)
    sound.apply_gain(150)
    play(sound)
    return


try:
    p1 = Process(target=play_audio)
    p1.start()
    head_bob(robot, interonsets)

except:
    print("some error")