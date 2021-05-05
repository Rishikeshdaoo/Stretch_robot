import time
from breathing import breathing_gesture_wrist, breathing_gesture_lift
import threading

import stretch_body.robot

robot = stretch_body.robot.Robot()
robot.startup()
time.sleep(0.3)
#robot.stow()

option = -1

p1 = threading.Thread(target=breathing_gesture_lift, args=(robot,))
p1.daemon=True
p1.start()
p2 = threading.Thread(target=breathing_gesture_wrist, args=(robot,))
p2.daemon=True
p2.start()

while True: time.sleep(100) # keep main thread alive bc daemons die when main thread dies and main thread should die when user does ctrl-c

