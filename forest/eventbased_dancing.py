#!/usr/bin/env python

import stretch_body.robot
import time
from pydub import AudioSegment
from pydub.playback import play
from threading import Thread, Event


headflag1 = Event()
headflag2 = Event()
headflag3 = Event()
wristflag1 = Event()
liftflag1 = Event()
liftflag2 = Event()
armflag1 = Event()
baseflag1 = Event()
baseflag2 = Event()

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
    headflag1.wait()
    while headflag1.is_set():
        current = time.time()
        robot.head.move_to('head_tilt', 0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        print(t2 - (time.time() - current))
        time.sleep(t2 - (time.time() - current))

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
        print(t2 - (time.time() - current))
        time.sleep(t2 - (time.time() - current))

    return

def head2(robot):
    headflag2.wait()
    while headflag2.is_set():
        current = time.time()
        robot.head.move_to('head_pan', 0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        print(t2 - (time.time() - current))
        time.sleep(t2 - (time.time() - current))

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
        robot.head.move_to('head_pan', -0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        print(t2 - (time.time() - current))
        time.sleep(t2 - (time.time() - current))

    return

def head3(robot):
    headflag3.wait()
    while headflag3.is_set():
        current = time.time()
        robot.head.move_to('head_tilt', 0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        print(t12 - (time.time() - current))
        time.sleep(t12 - (time.time() - current))

        # current = time.time()
        # robot.head.move_to('head_tilt', -0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        # print(t - (time.time() - current))
        # time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', -0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        # robot.head.move_to('head_tilt', -0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        print(t12 - (time.time() - current))
        time.sleep(t12 - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', 0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        # robot.head.move_to('head_tilt', 0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        print(t - (time.time() - current))
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', -0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        print(t12 - (time.time() - current))
        time.sleep(t12 - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', 0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        # robot.head.move_to('head_tilt', 0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        print(t12 - (time.time() - current))
        time.sleep(t12 - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', -0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        # robot.head.move_to('head_tilt', -0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        print(t - (time.time() - current))
        time.sleep(t - (time.time() - current))

    return

def wrist1(robot):
    wristflag1.wait()
    while wristflag1.is_set():
        current = time.time()
        robot.end_of_arm.move_to('wrist_yaw', -0.5, v_r = wrist_fastvel, a_r = wrist_fastacc)
        print(t - (time.time() - current))
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.end_of_arm.move_to('wrist_yaw', 0.5, v_r = wrist_fastvel, a_r = wrist_fastacc)
        print(t - (time.time() - current))
        time.sleep(t - (time.time() - current))

    return

def lift1(robot):
    liftflag1.wait()
    while liftflag1.is_set():
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

    return

def lift2(robot):
    liftflag2.wait()
    while liftflag2.is_set():
        current = time.time()
        robot.lift.move_to(0.70,Vmlift,amlift)
        robot.push_command()
        print(t - (time.time() - current))
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.lift.move_to(0.65,Vmlift,amlift)
        robot.push_command()
        print(t - (time.time() - current))
        time.sleep(t - (time.time() - current))

    return

def arm1(robot):
    armflag1.wait()
    while armflag1.is_set():
        current = time.time()
        robot.arm.move_to(x_m=0.25)
        robot.push_command()
        print(t2 - (time.time() - current))
        time.sleep(t2 - (time.time() - current))

        current = time.time()
        robot.arm.move_to(x_m=0.15)
        robot.push_command()
        print(t2 - (time.time() - current))
        time.sleep(t2 - (time.time() - current))

    return

def base1(robot):
    baseflag1.wait()
    while baseflag1.is_set():
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

    return

def base2(robot):
    baseflag2.wait()
    while baseflag2.is_set():
        current = time.time()
        robot.base.translate_by(x_m=0.2)
        robot.push_command()
        print(t2 - (time.time() - current))
        time.sleep(t2 - (time.time() - current))

        current = time.time()
        robot.base.translate_by(x_m=-0.2)
        robot.push_command()
        print(t2 - (time.time() - current))
        time.sleep(t2 - (time.time() - current))

    return

def audio():
    print("Playing sound...")
    sound = AudioSegment.from_file(filename)
    sound.apply_gain(512)
    play(sound)
    return

def flag():
    current = time.time()
    headflag1.set()
    print("Head Choreo 1 started...")
    time.sleep(8*t - (time.time() - current))
    headflag1.clear()

    current = time.time()
    headflag2.set()
    print("Head Choreo 2 started...")
    time.sleep(4*t - (time.time() - current))

    current = time.time()
    wristflag1.set()
    print("Wrist Choreo 1 started...")
    time.sleep(2*t - (time.time() - current))

    current = time.time()
    liftflag1.set()
    print("Lift Choreo 1 started...")

    current = time.time()
    armflag1.set()
    print("Arm Choreo 1 started...")
    time.sleep(2*t - (time.time() - current))

    current = time.time()
    baseflag1.set()
    print("Base Choreo 1 started...")
    time.sleep(8 * t - (time.time() - current))

    headflag2.clear()
    baseflag1.clear()
    liftflag1.clear()
    current = time.time()
    baseflag2.set()
    liftflag2.set()
    headflag3.set()
    print("Base and Lift Choreo 2 started...")
    time.sleep(8 * t - (time.time() - current))


if __name__ == "__main__":
    robot.startup()

    # robot.stow()

    robot.head.move_to('head_tilt', -1)
    robot.head.move_to('head_pan', 0)
    robot.lift.move_to(0.50, 10, 10)
    robot.end_of_arm.move_to('wrist_yaw', 1)
    robot.arm.move_to(x_m=0.1)
    robot.push_command()
    time.sleep(3)


    p1 = Thread(target=audio)
    p1.daemon = True
    p1.start()

    current = time.time()
    robot.head.move_to('head_tilt', 0)
    time.sleep(8*t - (time.time() - current))

    flagThread = Thread(target=flag)
    flagThread.daemon = True
    pHead1 = Thread(target=head1, args=(robot,))
    pHead1.daemon = True
    pHead2 = Thread(target=head2, args=(robot,))
    pHead2.daemon = True
    pWrist1 = Thread(target=wrist1, args=(robot,))
    pWrist1.daemon = True
    pLift1 = Thread(target=lift1, args=(robot,))
    pLift1.daemon = True
    pArm1 = Thread(target=arm1, args=(robot,))
    pArm1.daemon = True
    pBase1 = Thread(target=base1, args=(robot,))
    pBase1.daemon = True
    pBase2 = Thread(target=base2, args=(robot,))
    pBase2.daemon = True
    pLift2 = Thread(target=lift2, args=(robot,))
    pLift2.daemon = True
    pHead3 = Thread(target=head3, args=(robot,))
    pHead3.daemon = True
    flagThread.start()
    pHead1.start()
    pHead2.start()
    pWrist1.start()
    pLift1.start()
    pArm1.start()
    pBase1.start()
    pBase2.start()
    pLift2.start()
    pHead3.start()

    time.sleep(2500)
    robot.stop()
