#!/usr/bin/env python
import stretch_body.robot
import time
from pydub import AudioSegment
from pydub.playback import play
from threading import Thread

bpm = input("Please enter BPM:")

# BPM interval time
t3= 60.0/bpm

# Twice BPM interval
t= t3 * 2

# 1.5 times BPM interval
t2= t3 * 1.5

if(bpm == 60): filename = "../audios/thiswillbe.wav"
if(bpm == 80): filename = "../audios/drums_80.wav"
if(bpm == 90): filename = "../audios/drum_90.wav"
if(bpm == 100): filename = "../audios/beat_100.wav"

#basetranslations parameters
Vmbasetranslate=10
ambasetranslate=10

#lift parameters
Vmlift=10
amlift=10

#arm parameters
Vmarm=10
amarm=10

#baserotation parameters
xrotate=3.14
Vmrotation=10
amrotation=10

#tilt parameters
xtilt=0.5
Vrtilt=10
Artilt=10

#pan parameters
xpan=1
Vrpan=10
Arpan=10

#wrist parameters
xwrist=0.1
Vrwrist=10
Arwrist=10

#start

def dance1(robot):

    while(True):
        robot.head.move_to('head_tilt', 0.5)
        time.sleep(t)
        robot.head.move_to('head_tilt', -0.5)
        time.sleep(t)

def dance2(robot):

    while(True):
        robot.lift.move_to(0.50,Vmlift,amlift)
        robot.push_command()
        time.sleep(t2)
        robot.lift.move_to(-0.50,Vmlift,amlift)
        robot.push_command()
        time.sleep(t2)


def dance3(robot):

    while(True):
        robot.end_of_arm.move_to('wrist_yaw', -0.5)
        time.sleep(t3)
        robot.end_of_arm.move_to('wrist_yaw', 0.5)
        time.sleep(t3)

def dance4(robot):

    while(True):
        robot.base.rotate_by(x_r=0.8)
        robot.push_command()
        time.sleep(t)

        robot.base.rotate_by(x_r=-1.0)
        robot.push_command()
        time.sleep(t)

def audio():
    print("Playing sound...")
    sound = AudioSegment.from_file(filename)
    sound.apply_gain(100)
    play(sound)
    return


if __name__ == "__main__":
    robot = stretch_body.robot.Robot()
    robot.startup()

    # robot.stow()

    robot.head.move_to('head_tilt', -1)
    robot.lift.move_to(0.50, 10, 10)
    robot.end_of_arm.move_to('wrist_yaw', 1)
    robot.push_command()
    time.sleep(3)

    p1 = Thread(target=audio)
    p1.daemon = True
    p1.start()
    p2 = Thread(target=dance1, args=(robot,))
    p2.daemon = True
    p2.start()
    p3 = Thread(target=dance2, args=(robot,))
    p3.daemon = True
    p3.start()
    p4 = Thread(target=dance3, args=(robot,))
    p4.daemon = True
    p4.start()
    p5 = Thread(target=dance4, args=(robot,))
    p5.daemon = True
    p5.start()


    time.sleep(25)
    robot.stop()
