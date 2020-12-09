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
if(bpm == 80): filename = "./audios/drums_80.wav"
if(bpm == 90): filename = "../audios/drum_90.wav"
if(bpm == 100): filename = "../audios/beatbox_100.wav"

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
    robot.end_of_arm.move_by('wrist_yaw',-xwrist,Vrwrist,Arwrist)
    robot.push_command()
    time.sleep(t3)
    robot.lift.move_to(0.55,Vmlift,amlift)
    robot.end_of_arm.move_by('wrist_yaw',xwrist,Vrwrist,Arwrist)
    robot.push_command()
    time.sleep(t3)

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
    robot.base.rotate_by(xrotate,Vmrotation,amrotation)
    robot.push_command()

def dance23(robot):
    robot.head.move_to('head_tilt',0,Vrtilt,Artilt)
    robot.head.move_to('head_pan',xpan,Vrpan,Arpan)
    robot.arm.move_to(0.5,Vmarm,amarm)
    robot.lift.move_to(0.9,Vmlift,amlift)
    robot.base.rotate_by(xrotate,Vmrotation,amrotation)
    robot.push_command()

def dance24(robot):
    robot.head.move_to('head_pan',-xpan,Vrpan,Arpan)
    robot.arm.move_to(0.30,Vmarm,amarm)
    robot.lift.move_to(0.7,Vmlift,amlift)
    robot.base.rotate_by(xrotate,Vmrotation,amrotation)
    robot.push_command()

def dance25(robot):
    robot.head.move_to('head_pan',0,Vrpan,Arpan)
    robot.arm.move_to(0.25,Vmarm,amarm)
    robot.lift.move_to(0.50,Vmlift,amlift)
    robot.base.rotate_by(xrotate,Vmrotation,amrotation)
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
    time.sleep(t3)
    p3 = Thread(target=dance2, args=(robot,))
    p3.daemon = True
    p3.start()
    time.sleep(t3)
    p4 = Thread(target=dance3, args=(robot,))
    p4.daemon = True
    p4.start()
    time.sleep(t3)
    p5 = Thread(target=dance4, args=(robot,))
    p5.daemon = True
    p5.start()
    time.sleep(t3)
    p6 = Thread(target=dance5, args=(robot,))
    p6.daemon = True
    p6.start()
    time.sleep(t3)
    p7 = Thread(target=dance6, args=(robot,))
    p7.daemon = True
    p7.start()
    time.sleep(t3)
    p8 = Thread(target=dance7, args=(robot,))
    p8.daemon = True
    p8.start()
    time.sleep(t3)
    p9 = Thread(target=dance9, args=(robot,))
    p9.daemon = True
    p9.start()
    time.sleep(t3)
    p10 = Thread(target=dance10, args=(robot,))
    p10.daemon = True
    p10.start()
    time.sleep(t3)
    p11 = Thread(target=dance11, args=(robot,))
    p11.daemon = True
    p11.start()
    time.sleep(t3)
    p12 = Thread(target=dance12, args=(robot,))
    p12.daemon = True
    p12.start()
    time.sleep(t3)
    p13 = Thread(target=dance13, args=(robot,))
    p13.daemon = True
    p13.start()
    time.sleep(t3)
    p14 = Thread(target=dance14, args=(robot,))
    p14.daemon = True
    p14.start()
    time.sleep(t3)
    p15 = Thread(target=dance15, args=(robot,))
    p15.daemon = True
    p15.start()
    time.sleep(t3)
    p16 = Thread(target=dance16, args=(robot,))
    p16.daemon = True
    p16.start()
    time.sleep(t3)
    p17 = Thread(target=dance17, args=(robot,))
    p17.daemon = True
    p17.start()
    time.sleep(t3)
    p18 = Thread(target=dance18, args=(robot,))
    p18.daemon = True
    p18.start()
    time.sleep(t3)
    p19 = Thread(target=dance19, args=(robot,))
    p19.daemon = True
    p19.start()
    time.sleep(t3)
    p20 = Thread(target=dance20, args=(robot,))
    p20.daemon = True
    p20.start()
    time.sleep(t3)
    p21 = Thread(target=dance21, args=(robot,))
    p21.daemon = True
    p21.start()
    time.sleep(t3)
    p22 = Thread(target=dance22, args=(robot,))
    p22.daemon = True
    p22.start()
    time.sleep(t3)
    p23 = Thread(target=dance23, args=(robot,))
    p23.daemon = True
    p23.start()
    time.sleep(t3)
    p24 = Thread(target=dance24, args=(robot,))
    p24.daemon = True
    p24.start()
    time.sleep(t3)
    p25 = Thread(target=dance25, args=(robot,))
    p25.daemon = True
    p25.start()
    time.sleep(t3)
    p26 = Thread(target=dance8, args=(robot,))
    p26.daemon = True
    p26.start()
    time.sleep(t3)

    time.sleep(100)
    robot.stop()
