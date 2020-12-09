#!/usr/bin/env python

from breathing import breathing_gesture_head, breathing_gesture_lift, breathing_gesture_base, breathing_gesture_wrist
import threading
import time

import stretch_body.robot

robot = stretch_body.robot.Robot()
robot.startup()
time.sleep(0.3)

try:
    p1 = threading.Thread(target=breathing_gesture_lift, args=(robot,))
    p1.daemon = True
    p1.start()
    p2 = threading.Thread(target=breathing_gesture_head, args=(robot,))
    p2.daemon = True
    p2.start()
    p3 = threading.Thread(target=breathing_gesture_base, args=(robot,))
    p3.daemon = True
    p3.start()
    p4 = threading.Thread(target=breathing_gesture_wrist, args=(robot,))
    p4.daemon = True
    p4.start()

    while(True):
        time.sleep(10)

except Exception as e:
    print(e)