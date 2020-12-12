#!/usr/bin/env python

import stretch_body.robot
import time
from pydub import AudioSegment
from pydub.playback import play
from threading import Thread, Timer

robot = stretch_body.robot.Robot()

bpm = 70.0

# BPM interval time
t = 60.0/bpm

# Twice BPM interval
t2 = t * 2

# Twice BPM interval
t4 = t * 4

# 1.5 times BPM interval
t15 = t * 1.5

# Three quarter of BPM interval
t34 = (3*t) / 4

# Half of BPM interval
t12 = t / 2

# Quarter of BPM interval
t14 = t / 4

# Eighth of BPM interval
t18 = t / 8

filename = "../audios/forest.wav"

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
head_tilt_fastvel = robot.robot_params['head_tilt']['motion']['fast']['vel']
head_tilt_fastacc = robot.robot_params['head_tilt']['motion']['fast']['accel']

#pan parameters
xpan=1
Vrpan=10
Arpan=10

#wrist parameters
#tilt parameters
wrist_fastvel = robot.robot_params['wrist_yaw']['motion']['fast']['vel']
wrist_fastacc = robot.robot_params['head_tilt']['motion']['fast']['accel']

#start

def head1(robot):
    current = time.time()
    robot.head.move_to('head_tilt', 0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
    print(t - (time.time() - current))
    time.sleep(t - (time.time() - current))

    # current = time.time()
    # robot.head.move_to('head_tilt', -0.1, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
    # print(t12 - (time.time() - current))
    # time.sleep(t12 - (time.time() - current))
    #
    # current = time.time()
    # robot.head.move_to('head_tilt', 0.1, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
    # print(t12 - (time.time() - current))
    # time.sleep(t12 - (time.time() - current))

    current = time.time()
    robot.head.move_to('head_tilt', -0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
    print(t - (time.time() - current))
    time.sleep(t - (time.time() - current))

    head1(robot)

def head2(robot):
    current = time.time()
    robot.head.move_to('head_tilt', 0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
    print(t - (time.time() - current))
    time.sleep(t - (time.time() - current))

    current = time.time()
    robot.head.move_to('head_tilt', -0.1, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
    print(t12 - (time.time() - current))
    time.sleep(t12 - (time.time() - current))

    current = time.time()
    robot.head.move_to('head_tilt', 0.1, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
    print(t12 - (time.time() - current))
    time.sleep(t12 - (time.time() - current))

    current = time.time()
    robot.head.move_to('head_tilt', -0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
    print(t - (time.time() - current))
    time.sleep(t - (time.time() - current))

    head1(robot)

def wrist1(robot):
    current = time.time()
    robot.end_of_arm.move_to('wrist_yaw', -0.5, v_r = wrist_fastvel, a_r = wrist_fastacc)
    print(t - (time.time() - current))
    time.sleep(t - (time.time() - current))

    current = time.time()
    robot.end_of_arm.move_to('wrist_yaw', 0.5, v_r = wrist_fastvel, a_r = wrist_fastacc)
    print(t - (time.time() - current))
    time.sleep(t - (time.time() - current))

    wrist1(robot)

def lift1(robot):

    current = time.time()
    robot.lift.move_to(0.55,Vmlift,amlift)
    robot.push_command()
    print(t - (time.time() - current))
    time.sleep(t - (time.time() - current))

    current = time.time()
    robot.lift.move_to(0.50,Vmlift,amlift)
    robot.push_command()
    print(t - (time.time() - current))
    time.sleep(t - (time.time() - current))

    lift1(robot)

def arm1(robot):

    current = time.time()
    robot.arm.move_to(x_m=0.2)
    robot.push_command()
    print(t2 - (time.time() - current))
    time.sleep(t2 - (time.time() - current))

    current = time.time()
    robot.arm.move_to(x_m=0.15)
    robot.push_command()
    print(t2 - (time.time() - current))
    time.sleep(t2 - (time.time() - current))

    arm1(robot)

    return

def base1(robot):

    current = time.time()
    robot.base.rotate_by(x_r=0.5)
    robot.push_command()
    print(t2 - (time.time() - current))
    time.sleep(t2 - (time.time() - current))

    current = time.time()
    robot.base.rotate_by(x_r=-0.5)
    robot.push_command()
    print(t2 - (time.time() - current))
    time.sleep(t2 - (time.time() - current))

    base1(robot)

    return

def audio():
    print("Playing sound...")
    sound = AudioSegment.from_file(filename)
    sound.apply_gain(512)
    play(sound)
    return


if __name__ == "__main__":
    robot.startup()

    # robot.stow()

    robot.head.move_to('head_tilt', -1)
    robot.lift.move_to(0.50, 10, 10)
    robot.end_of_arm.move_to('wrist_yaw', 1)
    robot.arm.move_to(x_m=0.1)
    robot.push_command()
    time.sleep(3)

    p1 = Thread(target=audio)
    p1.daemon = True
    p1.start()

    robot.head.move_to('head_tilt', 0)
    time.sleep(8*t)

    p2 = Thread(target=head1, args=(robot,))
    p2.daemon = True
    p2.start()

    time.sleep(4*t)

    p3 = Thread(target=wrist1, args=(robot,))
    p3.daemon = True
    p3.start()

    time.sleep(2*t)

    p4 = Thread(target=lift1, args=(robot,))
    p4.daemon = True
    p4.start()

    p5 = Thread(target=arm1, args=(robot,))
    p5.daemon = True
    p5.start()

    time.sleep(2*t)

    p6 = Thread(target=base1, args=(robot,))
    p6.daemon = True
    p6.start()


    time.sleep(2500)
    robot.stop()
