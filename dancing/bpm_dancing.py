#!/usr/bin/env python
import stretch_body.robot
import time
from pydub import AudioSegment
from pydub.playback import play
from multiprocessing import Process

bpm = input("Please enter BPM:")

# BPM interval time
t3= 60.0/bpm

# Twice BPM interval
t= t3 * 2

# 1.5 times BPM interval
t2= t3 * 1.5

if(bpm == 60): filename = "../audios/thiswillbe.wav"
if(bpm == 80): filename = "./audios/beat_80.wav"
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
    # robot.end_of_arm.move_by('wrist_yaw',-xwrist,Vrwrist,Arwrist)
    # robot.push_command()
    # time.sleep(t3)
    robot.lift.move_to(0.55,Vmlift,amlift)
    robot.end_of_arm.move_by('wrist_yaw',xwrist,Vrwrist,Arwrist)
    robot.push_command()
    # time.sleep(t3)

def dance2(robot):
    robot.lift.move_to(0.50,Vmlift,amlift)
    robot.end_of_arm.move_by('wrist_yaw',-xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance3(robot):
    robot.lift.move_to(0.55,Vmlift,amlift)
    robot.end_of_arm.move_by('wrist_yaw',xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance4(robot):
    robot.lift.move_to(0.50,Vmlift,amlift)
    robot.end_of_arm.move_by('wrist_yaw',-xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance5(robot):
    robot.lift.move_to(0.55,Vmlift,amlift)
    robot.end_of_arm.move_by('wrist_yaw',xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance6(robot):
    robot.lift.move_to(0.50,Vmlift,amlift)
    robot.end_of_arm.move_by('wrist_yaw',-xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance7(robot):
    robot.lift.move_to(0.55,Vmlift,amlift)
    robot.end_of_arm.move_by('wrist_yaw',xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance8(robot):
    robot.lift.move_to(0.50,Vmlift,amlift)
    robot.end_of_arm.move_by('wrist_yaw',-xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance8(robot):
    robot.lift.move_to(0.55,Vmlift,amlift)
    robot.end_of_arm.move_by('wrist_yaw',xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance9(robot):
    robot.lift.move_to(0.50,Vmlift,amlift)
    robot.end_of_arm.move_by('wrist_yaw',-xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance10(robot):
    robot.head.move_to('head_tilt',0,Vrtilt,Artilt)
    robot.lift.move_to(0.55,Vmlift,amlift)
    robot.end_of_arm.move_by('wrist_yaw',xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance11(robot):
    robot.lift.move_to(0.50,Vmlift,amlift)
    robot.end_of_arm.move_by('wrist_yaw',-xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance12(robot):
    robot.lift.move_to(0.6,Vmlift,amlift)
    robot.arm.move_to(0.3,Vmarm,amarm)
    robot.head.move_to('head_pan',xpan,Vrpan,Arpan)
    robot.end_of_arm.move_by('wrist_yaw',xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance13(robot):
    robot.arm.move_to(0.28,Vmarm,amarm)
    robot.head.move_to('head_pan',-xpan,Vrpan,Arpan)
    robot.end_of_arm.move_by('wrist_yaw',-xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance14(robot):
    robot.arm.move_to(0.3,Vmarm,amarm)
    robot.head.move_to('head_tilt',xtilt,Vrtilt,Artilt)
    robot.head.move_to('head_pan',xpan,Vrpan,Arpan)
    robot.end_of_arm.move_by('wrist_yaw',xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance15(robot):
    robot.head.move_to('head_pan',-xpan,Vrpan,Arpan)
    robot.end_of_arm.move_by('wrist_yaw',-xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance16(robot):
    robot.head.move_to('head_pan',xpan,Vrpan,Arpan)
    robot.end_of_arm.move_by('wrist_yaw',xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance17(robot):
    robot.head.move_to('head_pan',-xpan,Vrpan,Arpan)
    robot.end_of_arm.move_by('wrist_yaw',-xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance18(robot):
    robot.head.move_to('head_tilt',-xtilt,Vrtilt,Artilt)
    robot.head.move_to('head_pan',xpan,Vrpan,Arpan)
    robot.end_of_arm.move_by('wrist_yaw',xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance19(robot):
    robot.head.move_to('head_pan',-xpan,Vrpan,Arpan)
    robot.end_of_arm.move_by('wrist_yaw',-xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance20(robot):
    robot.head.move_to('head_pan',xpan,Vrpan,Arpan)
    robot.end_of_arm.move_by('wrist_yaw',xwrist,Vrwrist,Arwrist)
    robot.push_command()

def dance21(robot):
    robot.head.move_to('head_pan',-xpan,Vrpan,Arpan)
    robot.arm.move_to(0.5)
    robot.lift.move_to(0.9,Vmlift,amlift)
    robot.head.move_to('head_tilt',xtilt,Vrtilt,Artilt)
    robot.base.translate_by(0.2,Vmbasetranslate,ambasetranslate)
    robot.push_command()

def dance22(robot):
    robot.head.move_to('head_pan',-xpan,Vrpan,Arpan)
    robot.arm.move_to(0.30,Vmarm,amarm)
    robot.lift.move_to(0.7,Vmlift,amlift)
    # robot.base.rotate_by(xrotate,Vmrotation,amrotation)
    robot.push_command()

def dance23(robot):
    robot.head.move_to('head_tilt',0,Vrtilt,Artilt)
    robot.head.move_to('head_pan',xpan,Vrpan,Arpan)
    robot.arm.move_to(0.5,Vmarm,amarm)
    robot.lift.move_to(0.9,Vmlift,amlift)
    # robot.base.rotate_by(xrotate,Vmrotation,amrotation)
    robot.push_command()

def dance24(robot):
    robot.head.move_to('head_pan',-xpan,Vrpan,Arpan)
    robot.arm.move_to(0.30,Vmarm,amarm)
    robot.lift.move_to(0.7,Vmlift,amlift)
    # robot.base.rotate_by(xrotate,Vmrotation,amrotation)
    robot.push_command()

def dance25(robot):
    robot.head.move_to('head_pan',0,Vrpan,Arpan)
    robot.arm.move_to(0.25,Vmarm,amarm)
    robot.lift.move_to(0.50,Vmlift,amlift)
    # robot.base.rotate_by(xrotate,Vmrotation,amrotation)
    robot.push_command()

def audio():
    print("Playing sound...")
    sound = AudioSegment.from_file(filename)
    sound.apply_gain(100)
    play(sound)
    return


if __name__ == "__main__":
    robot = stretch_body.robot.Robot()
    robot.startup()

    robot.stow()

    robot.head.move_to('head_tilt', -1)
    robot.lift.move_to(0.50, 10, 10)
    robot.end_of_arm.move_to('wrist_yaw', 1)
    robot.push_command()
    time.sleep(3)

    p1 = Process(target=audio)
    p1.start()
    p2 = Process(target=dance1(robot))
    p2.start()
    time.sleep(t3)
    p3 = Process(target=dance2(robot))
    p3.start()
    time.sleep(t3)
    p4 = Process(target=dance3(robot))
    p4.start()
    time.sleep(t3)
    p5 = Process(target=dance4(robot))
    p5.start()
    time.sleep(t3)
    p6 = Process(target=dance5(robot))
    p6.start()
    time.sleep(t3)
    p7 = Process(target=dance6(robot))
    p7.start()
    time.sleep(t3)
    p8 = Process(target=dance7(robot))
    p8.start()
    time.sleep(t3)
    p26 = Process(target=dance8(robot))
    p26.start()
    time.sleep(t3)
    p9 = Process(target=dance9(robot))
    p9.start()
    time.sleep(t3)
    p10 = Process(target=dance10(robot))
    p10.start()
    time.sleep(t3)
    p11 = Process(target=dance11(robot))
    p11.start()
    time.sleep(t3)
    p12 = Process(target=dance12(robot))
    p12.start()
    time.sleep(t3)
    p13 = Process(target=dance13(robot))
    p13.start()
    time.sleep(t3)
    p14 = Process(target=dance14(robot))
    p14.start()
    time.sleep(t3)
    p15 = Process(target=dance15(robot))
    p15.start()
    time.sleep(t3)
    p16 = Process(target=dance16(robot))
    p16.start()
    time.sleep(t3)
    p17 = Process(target=dance17(robot))
    p17.start()
    time.sleep(t3)
    p18 = Process(target=dance18(robot))
    p18.start()
    time.sleep(t3)
    p19 = Process(target=dance19(robot))
    p19.start()
    time.sleep(t3)
    p20 = Process(target=dance20(robot))
    p20.start()
    time.sleep(t3)
    p21 = Process(target=dance21(robot))
    p21.start()
    time.sleep(t3)
    p22 = Process(target=dance22(robot))
    p22.start()
    time.sleep(t3)
    p23 = Process(target=dance23(robot))
    p23.start()
    time.sleep(t3)
    p24 = Process(target=dance24(robot))
    p24.start()
    time.sleep(t3)
    p25 = Process(target=dance25(robot))
    p25.start()
    time.sleep(t3)

    robot.stop()
