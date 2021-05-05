#!/usr/bin/env python

##########################################################
# First prototype of a control script
# for OSC based communication with Stretch (osc_dancing.py)
##########################################################

import time
import OSC
from threading import Thread, Event
import stretch_body.robot
from osc_processing import osc_functionality
from osc_dancing import  audio, flag,    \
                                head1, headStart, head1alt, head2, head2alt, head3,    \
                                wrist1, wristalt1, \
                                lift1, lift2, liftalt1,  \
                                arm1,   \
                                base1, base2, base3, base4,    \
                                headflagStart,  \
                                getBPM, getTime


bpm = getBPM()
t = getTime()

robot = stretch_body.robot.Robot()
robot.startup()

# robot.stow()

robot.head.move_to('head_tilt', -1)
robot.head.move_to('head_pan', 0)
robot.lift.move_to(0.50, 10, 10)
robot.end_of_arm.move_to('wrist_yaw', 1)
robot.arm.move_to(x_m=0.1)
robot.push_command()
time.sleep(3)

pOSC = Thread(target=osc_functionality)
pOSC.daemon = True
pOSC.start()

# p1 = Thread(target=audio)
# p1.daemon = True
# p1.start()

pHeadStart = Thread(target=headStart, args=(robot,))
pHeadStart.daemon = True
#
# # pHead1 = Thread(target=head1, args=(robot,))
# # pHead1.daemon = True
# pHead1 = Thread(target=head1alt, args=(robot,))
# pHead1.daemon = True
#
# pWristAlt1 = Thread(target=wristalt1, args=(robot,))
# pWristAlt1.daemon = True
#
# pLiftAlt1 = Thread(target=liftalt1, args=(robot,))
# pLiftAlt1.daemon = True
#
# # pHead2 = Thread(target=head2, args=(robot,))
# # pHead2.daemon = True
# pHead2alt = Thread(target=head2alt, args=(robot,))
# pHead2alt.daemon = True
#
# pWrist1 = Thread(target=wrist1, args=(robot,))
# pWrist1.daemon = True
#
# pLift1 = Thread(target=lift1, args=(robot,))
# pLift1.daemon = True
#
# pArm1 = Thread(target=arm1, args=(robot,))
# pArm1.daemon = True
#
# pBase1 = Thread(target=base1, args=(robot,))
# pBase1.daemon = True
#
# pBase2 = Thread(target=base2, args=(robot,))
# pBase2.daemon = True
#
# pBase3 = Thread(target=base3, args=(robot,))
# pBase3.daemon = True
#
# pBase4 = Thread(target=base4, args=(robot,))
# pBase4.daemon = True
#
# pLift2 = Thread(target=lift2, args=(robot,))
# pLift2.daemon = True
#
# pHead3 = Thread(target=head3, args=(robot,))
# pHead3.daemon = True
#
# flagThread.start()
# pHeadStart.start()
# pHead1.start()
# pLiftAlt1.start()
# pWristAlt1.start()
# # pHead2.start()
# pHead2alt.start()
# pWrist1.start()
# pLift1.start()
# pArm1.start()
# # pBase1.start()
# # pBase2.start()
# pBase3.start()
# pBase4.start()
# pLift2.start()
# pHead3.start()
#
# time.sleep(2500)
# robot.stop()




##########################################

# robot.head.move_to('head_tilt', -1)
# robot.head.move_to('head_pan', 0)
# robot.lift.move_to(0.50, 10, 10)
# robot.end_of_arm.move_to('wrist_yaw', 1)
# robot.arm.move_to(x_m=0.1)
# robot.push_command()
# time.sleep(3)
#
#
# p1 = Thread(target=audio)
# p1.daemon = True
# p1.start()
#
# current = time.time()
# flagThread = Thread(target=flag)
# flagThread.daemon = True
# pHeadStart = Thread(target=headStart, args=(robot,))
# pHeadStart.daemon = True
# # pHead1 = Thread(target=head1, args=(robot,))
# # pHead1.daemon = True
# pHead1 = Thread(target=head1alt, args=(robot,))
# pHead1.daemon = True
#
# pWristAlt1 = Thread(target=wristalt1, args=(robot,))
# pWristAlt1.daemon = True
# pLiftAlt1 = Thread(target=liftalt1, args=(robot,))
# pLiftAlt1.daemon = True
#
# # pHead2 = Thread(target=head2, args=(robot,))
# # pHead2.daemon = True
# pHead2alt = Thread(target=head2alt, args=(robot,))
# pHead2alt.daemon = True
#
# pWrist1 = Thread(target=wrist1, args=(robot,))
# pWrist1.daemon = True
# pLift1 = Thread(target=lift1, args=(robot,))
# pLift1.daemon = True
# pArm1 = Thread(target=arm1, args=(robot,))
# pArm1.daemon = True
# pBase1 = Thread(target=base1, args=(robot,))
# pBase1.daemon = True
# pBase2 = Thread(target=base2, args=(robot,))
# pBase2.daemon = True
# pBase3 = Thread(target=base3, args=(robot,))
# pBase3.daemon = True
# pBase4 = Thread(target=base4, args=(robot,))
# pBase4.daemon = True
# pLift2 = Thread(target=lift2, args=(robot,))
# pLift2.daemon = True
# pHead3 = Thread(target=head3, args=(robot,))
# pHead3.daemon = True
#
#
# flagThread.start()
# pHeadStart.start()
# pHead1.start()
#
# pLiftAlt1.start()
# pWristAlt1.start()
#
# # pHead2.start()
# pHead2alt.start()
#
# pWrist1.start()
# pLift1.start()
# pArm1.start()
# # pBase1.start()
# # pBase2.start()
# pBase3.start()
# pBase4.start()
# pLift2.start()
# pHead3.start()
#
time.sleep(2500)
robot.stop()