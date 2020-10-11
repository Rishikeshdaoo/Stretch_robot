#!/usr/bin/env python
import stretch_body.robot
import time
import playsound
import pydub
from pydub import AudioSegment
from pydub.playback import play


robot=stretch_body.robot.Robot()

print("Playing sound...")
sound = AudioSegment.from_file("./audios/Disgust.wav")
sound.apply_gain(-6)
play(sound)
playsound(wav_file)

print("Doing gestures now...")
disgust();

robot.stop()


def disgust():
    robot.startup()

    robot.base.translate_by(x_m=0.5)
    robot.push_command()
    time.sleep(4.0) #wait

    robot.base.set_rotational_velocity(v_r=0.1) #switch to velocity controller
    robot.push_command()
    time.sleep(4.0) #wait

    robot.base.set_rotational_velocity(v_r=0.0) #stop motion
    robot.push_command()
