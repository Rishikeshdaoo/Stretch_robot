#!/usr/bin/env python

#########################################################
# Script for Multithreaded, Event-based approach.
# Refer this code to see how the event-based implementation
# for Stretch moving around objects was done in a hand-designed manner.
#
# Choreography - Stretch moving around xArm, hand-designed movements

# x_m = 1 is the robot's left and x_m = -1 is the robot's right
#########################################################

import stretch_body.robot
import time
from pydub import AudioSegment
from pydub.playback import play
from threading import Thread, Event

headflagStart = Event()
headflag1 = Event()
headflag2 = Event()
headflag3 = Event()
headflag4 = Event()
wristflag1 = Event()
liftflag1 = Event()
liftflag2 = Event()
armflag1 = Event()
armflag2 = Event()
baseflag1 = Event()
baseflag2 = Event()
baseflag3 = Event()
baseflag4 = Event()

robot = stretch_body.robot.Robot()

BPM = 70.0

# BPM interval time
t = 60.0/BPM

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

#Book-keeping functions
def getBPM():
    return BPM

def getTime():
    return t

#start
def headStart(robot):
    headflagStart.wait()
    if headflagStart.is_set():
        current = time.time()
        robot.head.move_to('head_tilt', 0)
        time.sleep(2 * t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', 1, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        time.sleep(t12 - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', 0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        time.sleep(t12 - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', -0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        time.sleep(t12 - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', 0.0, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        time.sleep(t12 - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', 0, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        time.sleep(2 * t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', -0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        time.sleep(t12 - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', -0.5, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        time.sleep(t12 - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', 0.0, v_r = head_tilt_fastvel, a_r = head_tilt_fastacc)
        time.sleep(t - (time.time() - current))
    return

def head1(robot):
    headflag1.wait()
    while headflag1.is_set():
        current = time.time()

        robot.head.move_to('head_tilt', 0.5, v_r=0.25, a_r=0.3)
        robot.head.move_to('head_pan', 0.8, v_r=0.25, a_r=0.3)
        time.sleep(4 * t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', 0, v_r=0.3, a_r=0.3)
        robot.head.move_to('head_tilt', -0.5, v_r=0.3, a_r=0.3)
        time.sleep(5 * t - (time.time() - current))

    return


def head2(robot):
    headflag2.wait()
    while headflag2.is_set():
        current = time.time()
        robot.head.move_to('head_pan', -1, v_r=0.2, a_r=0.1)


        robot.head.move_to('head_tilt', 0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', -0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', 0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', -0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', 0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', -0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))
        current = time.time()

        robot.head.move_to('head_tilt', 0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', -0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))


        current = time.time()
        robot.head.move_to('head_pan', 1, v_r=0.4, a_r=0.1)

        robot.head.move_to('head_tilt', 0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', -0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', 0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', -0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', 0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', -0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', 0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_tilt', -0.2, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t2 - (time.time() - current))

    return

def head3(robot):
    headflag3.wait()
    while headflag3.is_set():
        current = time.time()
        robot.head.move_to('head_pan', 0, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', -0.4, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', 0, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', -0.4, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))


        current = time.time()
        robot.head.move_to('head_pan', 0, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', 0.4, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', 0, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', 0.4, v_r=head_tilt_fastvel, a_r=head_tilt_fastacc)
        time.sleep(t - (time.time() - current))

    return

def head4(robot):
    headflag4.wait()
    while headflag4.is_set():
        current = time.time()
        robot.head.move_to('head_pan', -1, v_r=0.4)
        time.sleep(2*t2 - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', 1, v_r=0.4)
        time.sleep(2*t2 - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', -1, v_r=0.4)
        time.sleep(2*t2 - (time.time() - current))

        current = time.time()
        robot.head.move_to('head_pan', 1, v_r=0.4)
        time.sleep(2*t2 - (time.time() - current))

    return



def wrist1(robot):
    arm_vel_slow_m = robot.robot_params['wrist_yaw']['motion']['slow']['vel']
    arm_accel_slow_m = robot.robot_params['wrist_yaw']['motion']['slow']['accel']

    wristflag1.wait()
    while wristflag1.is_set():
        current = time.time()
        robot.end_of_arm.move_to('wrist_yaw', -0.5, v_r=0.6, a_r=0.5)
        time.sleep(8 * t - (time.time() - current))

        # print("wrist2")
        # robot.end_of_arm.move_to('wrist_yaw', 0.3, v_r=0.5, a_r=0.5)
        # time.sleep(3)

    return


def lift1(robot):
    lift_vel_slow_m = robot.lift.params['motion']['slow']['vel_m']
    lift_accel_slow_m = robot.lift.params['motion']['slow']['accel_m']

    liftflag1.wait()
    while liftflag1.is_set():
        current = time.time()
        robot.lift.move_to(x_m=0.8, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)
        robot.push_command()
        time.sleep(8 * t - (time.time() - current))

    return


def lift2(robot):
    liftflag2.wait()
    while liftflag2.is_set():
        current = time.time()
        robot.lift.move_to(0.70,Vmlift,amlift)
        robot.push_command()
        time.sleep(t - (time.time() - current))

        current = time.time()
        robot.lift.move_to(0.65,Vmlift,amlift)
        robot.push_command()
        time.sleep(t - (time.time() - current))

    return


def arm1(robot):
    armflag1.wait()
    while armflag1.is_set():
        current = time.time()
        robot.arm.move_to(x_m=0.25, v_m=0.6)
        robot.push_command()
        time.sleep(t2 - (time.time() - current))

        current = time.time()
        robot.arm.move_to(x_m=0.15, v_m=0.6)
        robot.push_command()
        time.sleep(t2 - (time.time() - current))


        current = time.time()
        robot.arm.move_to(x_m=0.5, v_m=0.6)
        robot.push_command()
        time.sleep(t2 - (time.time() - current))

        current = time.time()
        robot.arm.move_to(x_m=0.15, v_m=0.6)
        robot.push_command()
        time.sleep(t2 - (time.time() - current))

    return

def arm2(robot):
    armflag2.wait()
    while armflag2.is_set():
        current = time.time()
        robot.arm.move_to(x_m=0.50, v_m=0.2)
        robot.push_command()
        time.sleep(2*t2 - (time.time() - current))

        current = time.time()
        robot.arm.move_to(x_m=0.10, v_m=0.2)
        robot.push_command()
        time.sleep(2*t2 - (time.time() - current))


        current = time.time()
        robot.arm.move_to(x_m=0.50, v_m=0.2)
        robot.push_command()
        time.sleep(2*t2 - (time.time() - current))

        current = time.time()
        robot.arm.move_to(x_m=0.10, v_m=0.2)
        robot.push_command()
        time.sleep(2*t2 - (time.time() - current))

    return


def base1(robot):
    baseflag1.wait()
    while baseflag1.is_set():
        current = time.time()
        robot.base.translate_by(x_m=1)
        robot.push_command()
        time.sleep(2*t2 - (time.time() - current))

        current = time.time()
        robot.base.rotate_by(x_r=-0.5)
        robot.push_command()
        time.sleep(2*t2 - (time.time() - current))

        current = time.time()
        robot.base.translate_by(x_m=1)
        robot.push_command()
        time.sleep(2*t2 - (time.time() - current))

    return


def base2(robot):
    baseflag2.wait()
    while baseflag2.is_set():
        current = time.time()
        robot.base.translate_by(x_m=0.2)
        robot.push_command()
        time.sleep(t2 - (time.time() - current))

        current = time.time()
        robot.base.translate_by(x_m=-0.2)
        robot.push_command()
        time.sleep(t2 - (time.time() - current))

    return

def base3(robot):
    baseflag3.wait()
    while baseflag3.is_set():
        current = time.time()
        robot.base.translate_by(x_m=2, v_m= 2, a_m = 1)
        robot.push_command()
        time.sleep(t2 - (time.time() - current))

        current = time.time()
        robot.base.rotate_by(x_r=1, v_r= 2, a_r = 1)
        robot.push_command()
        time.sleep(t2 - (time.time() - current))

    current = time.time()
    robot.base.rotate_by(x_r=-1, v_r=2, a_r=1)

    robot.push_command()
    time.sleep(t2 - (time.time() - current))

    return


def base4(robot):
    baseflag4.wait()
    while baseflag4.is_set():
        current = time.time()
        robot.base.translate_by(x_m=2, v_m= 2)
        robot.push_command()
        print("Straight 1")
        time.sleep(8*t2 - (time.time() - current))

        current = time.time()
        robot.base.rotate_by(x_r=-0.6, v_r= 1)
        robot.push_command()
        print("Turn 1")
        time.sleep(t2 - (time.time() - current))

        current = time.time()
        robot.base.translate_by(x_m=2, v_m= 2)
        robot.push_command()
        print("Straight 2")
        time.sleep(8*t2 - (time.time() - current))

        current = time.time()
        robot.base.rotate_by(x_r=-1, v_r=1)
        robot.push_command()
        print("Turn 2")
        time.sleep(t2 - (time.time() - current))

        current = time.time()
        robot.base.translate_by(x_m=2, v_m=2)
        robot.push_command()
        print("Straight 3")
        time.sleep(8 * t2 - (time.time() - current))

        current = time.time()
        robot.base.rotate_by(x_r=-1.5, v_r=1)
        robot.push_command()
        print("Turn 3")
        time.sleep(t2 - (time.time() - current))

        current = time.time()
        robot.base.translate_by(x_m=1, v_m=2)
        robot.push_command()
        print("Straight 4")
        time.sleep(t2 - (time.time() - current))

        current = time.time()
        robot.base.rotate_by(x_r=-1, v_r=1)
        robot.push_command()
        print("Turn 4")
        time.sleep(t2 - (time.time() - current))

        current = time.time()
        robot.base.translate_by(x_m=2, v_m=2)
        robot.push_command()
        print("Straight 5")
        time.sleep(t2 - (time.time() - current))


	# current = time.time()
	# robot.base.rotate_by(x_r=1, v_r=1, a_r=1)
	# robot.push_command()
	# time.sleep(t2 - (time.time() - current))

    return


def audio():
    print("Playing sound...")
    sound = AudioSegment.from_file(filename)
    sound.apply_gain(512)
    play(sound)
    return

def flag():
    current = time.time()
    headflagStart.set()
    print("Head Start started...")
    time.sleep(8*t - (time.time() - current))
    headflagStart.clear()

    current = time.time()
    headflag1.set()
    liftflag1.set()
    wristflag1.set()
    print("Head1, Lift1, Wrist1 started...")
    time.sleep(8*t  - (time.time() - current))
    headflag1.clear()
    liftflag1.clear()
    wristflag1.clear()

    current = time.time()
    headflag2.set()
    print("Head2 started...")
    time.sleep(4*t - (time.time() - current))

    current = time.time()
    wristflag1.set()
    print("Wrist1 started...")
    time.sleep(2*t - (time.time() - current))

    current = time.time()
    liftflag1.set()
    print("Lift1, Base1 started...")

    current = time.time()
    armflag1.set()
    print("Arm1 started...")
    time.sleep(10*t - (time.time() - current))
    headflag2.clear()
    liftflag1.clear()
    armflag1.clear()

    current = time.time()
    baseflag4.set()
    liftflag2.set()
    headflag3.set()
    print("Base4, Lift2, Head3 started...")
    time.sleep(12 * t - (time.time() - current))
    headflag3.clear()

    current = time.time()
    headflag4.set()
    armflag2.set()
    print("Head4, Arm2 started...")
    time.sleep(8 * t - (time.time() - current))

    return


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
    flagThread = Thread(target=flag)
    flagThread.daemon = True
    pHeadStart = Thread(target=headStart, args=(robot,))
    pHeadStart.daemon = True
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
    pArm2 = Thread(target=arm2, args=(robot,))
    pArm2.daemon = True
    pBase1 = Thread(target=base1, args=(robot,))
    pBase1.daemon = True
    pBase2 = Thread(target=base2, args=(robot,))
    pBase2.daemon = True
    pBase3 = Thread(target=base3, args=(robot,))
    pBase3.daemon = True
    pBase4 = Thread(target=base4, args=(robot,))
    pBase4.daemon = True
    pLift2 = Thread(target=lift2, args=(robot,))
    pLift2.daemon = True
    pHead3 = Thread(target=head3, args=(robot,))
    pHead3.daemon = True
    pHead4 = Thread(target=head4, args=(robot,))
    pHead4.daemon = True
    flagThread.start()
    pHeadStart.start()
    pHead1.start()
    pHead2.start()
    pWrist1.start()
    pLift1.start()
    pArm1.start()
    # pBase1.start()
    # pBase2.start()
    # pBase3.start()
    pBase4.start()
    pLift2.start()
    pHead3.start()
    pHead4.start()
    pArm2.start()


    time.sleep(2500)
    robot.stop()
