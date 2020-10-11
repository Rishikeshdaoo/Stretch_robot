#!/usr/bin/env python
import stretch_body.robot
import time
import playsound

robot=stretch_body.robot.Robot()
robot.startup()


print("Playing sound...")
wav_file = input("audios/Joy.wav")
playsound(wav_file)

print("Moving base now...")
#robot.base.translate_by(-0.5, 1)

#robot.push_command()

time.sleep(10)

robot.stop()
