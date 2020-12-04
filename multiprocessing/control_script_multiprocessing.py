from multiprocessing.breathing_withLocks import breathing_gesture_head, breathing_gesture_lift
from multiprocessing import Process, Lock

import stretch_body.robot

# print("Do Ctrl+c to exit the program.")
# print("Send gesture number over UDP.")

robot = stretch_body.robot.Robot()
lock = Lock()
robot.startup()
robot.stow()

option = -1

try:
    p1 = Process(target=breathing_gesture_lift, args=(robot,))
    p1.start()
    p2 = Process(target=breathing_gesture_head, args=(robot,))
    p2.start()

    while(True):
        if(not p1.is_alive()):
            p1 = Process(target=breathing_gesture_lift, args=(robot,))
            p1.start()

        if (not p2.is_alive()):
            p2 = Process(target=breathing_gesture_head, args=(robot,))
            p2.start()

except Exception as e:
    print(e)