#!/usr/bin/env python

import stretch_body.robot
import time
from multiprocessing import Process
from pydub import AudioSegment
from pydub.playback import play
import numpy as np

import essentia
import essentia.standard as es

robot=stretch_body.robot.Robot()
robot.startup()

robot.stow()

filename = "./audios/drum_60.wav"

# features, _ = es.MusicExtractor(lowlevelStats=['mean', 'stdev'],
#                                               rhythmStats=['mean', 'stdev'],
#                                               tonalStats=['mean', 'stdev'])(filename)

# tempo = np.round(features['rhythm.bpm'])
# print(tempo)
#
# t= 60.0/tempo * 2

audio = es.MonoLoader(filename= filename)()
rhythm_extractor = es.RhythmExtractor2013(method="multifeature")
bpm, beats, _, _, _ = rhythm_extractor(audio)

# interonset = np.ediff1d(beats)
# interonset = np.add.reduceat(interonset, np.arange(0, len(interonset), 2))
# interonset = np.round(interonset, decimals=3)

tempo = np.round(bpm)
t = 60/tempo * 2
t = np.round(t, decimals=2)

xrotate=3.14
xtilt=0.5
xpan=1
xwrist=1.5
#start

head_tilt = [-0.2 , 0.2]

def head_bob(robot):

    for n in range(len(beats)/2):
        print(t)
        robot.head.move_to('head_tilt', head_tilt[n%2])
        time.sleep(t)

    return

def play_audio():
    print("Playing sound...")
    sound = AudioSegment.from_file(filename)
    sound.apply_gain(150)
    play(sound)
    return


try:
    # p1 = Process(target=play_audio)
    # p1.start()
    head_bob(robot)

except Exception as e:
    print(e)