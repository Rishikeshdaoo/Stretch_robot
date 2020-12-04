#!/usr/bin/env python

# Tried to work with OnsetProcessor, TempoProcessor.
# Both give probabilities of an onset/tempo.
# Using the highest probability value isnt giving a good beat-sync movement

import stretch_body.robot
import time
import pydub
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
from multiprocessing import Process
from madmom.features.tempo import TempoEstimationProcessor
from madmom.features.beats import RNNBeatProcessor

robot=stretch_body.robot.Robot()
robot.startup()

robot.stow()

filename = "./audios/forest.wav"
proc = TempoEstimationProcessor(fps=100)
act = RNNBeatProcessor()(filename)
tempo = proc(act)

tempo = tempo[0][0]
t= 60.0/tempo *4

# interonsets = np.ediff1d(onsets)
# interonsets = np.add.reduceat(interonsets, np.arange(0, len(interonsets), 8))

# print(interonsets)


xrotate=3.14
xtilt=0.5
xpan=1
xwrist=1.5
#start

def head_bob(robot):

    while(True):
        robot.head.move_to('head_tilt', -0.2)
        time.sleep(t)
        robot.head.move_to('head_tilt', 0.2)
        time.sleep(t)
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
    head_bob(robot)

except:
    print("some error")