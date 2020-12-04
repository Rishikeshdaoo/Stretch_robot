import pyaudio
import sys
from aubio import source, onset
import numpy as np


def interonset_time(filename):
    win_s = 512                 # fft size
    hop_s = win_s // 2          # hop size

    samplerate = 44100

    s = source(filename, samplerate, hop_s)
    samplerate = s.samplerate

    o = onset("default", win_s, hop_s, samplerate)

    # list of onsets, in samples
    onsets = []

    # total number of frames read
    total_frames = 0
    while True:
        samples, read = s()
        if o(samples):
            onsets.append(o.get_last())
        total_frames += read
        if read < hop_s: break

    time = [float(x)/samplerate for x in onsets]

    times = [x - time[i-1] for i,x in enumerate(time)][1:]

    print(times)

    return time


