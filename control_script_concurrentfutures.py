from gesture_joy import joy_gesture, joy_audio
from gesture_fear import fear_gesture, fear_audio
from gesture_disgust import disgust_gesture, disgust_audio
from breathing import breathing_gesture, breathing_gesture_head, breathing_gesture_wrist, breathing_gesture_lift, breathing_gesture_base
from multiprocessing import Process, Queue
# from udp_server import udp
import numpy as np
import threading

import stretch_body.robot

print("Do Ctrl+c to exit the program.")
print("Send gesture number over UDP.")

robot = stretch_body.robot.Robot()
robot.startup()
robot.stow()

option = -1

# q = Queue()
# x = threading.Thread(target=udp(q), daemon=True)
# x.start()

# def stop_threads(p1, p2, p7, p8, p9):
#     p7.terminate()
#     p8.terminate()
#     p9.terminate()
#
#     return

try:
    c1 = -1
    c2 = -1
    c3 = -1
    c4 = -1

    l1 = [1, 2, 3, 4, 5, 6, 7]
    l2 = [1, 2, 3, 4]
    l3 = [1, 2, 3, 4]
    l4 = [0, 1]

    p7 = Process(target=breathing_gesture_head(robot, 0))
    p8 = Process(target=breathing_gesture_wrist(robot, 0))
    p9 = Process(target=breathing_gesture_lift(robot, 0))
    p10 = Process(target=breathing_gesture_base(robot, 1))

    while(True):
        c1 += 1
        c2 += 1
        c3 += 1
        c4 += 1

        choice1 = l1[c1]
        choice2 = l2[c2]
        choice3 = l3[c3]
        choice4 = l4[c4]

        if(option == 1):
            p7.terminate()
            print("Playing Joy gesture now...")
            p1 = Process(target=joy_audio)
            p1.start()
            p2 = Process(target=joy_gesture(robot))
            p2.start()

        elif(option==2):
            p7.terminate()
            print("Playing Disgust gesture now...")
            p3 = Process(target=disgust_audio)
            p3.start()
            p4 = Process(target=disgust_gesture(robot))
            p4.start()

        elif(option==3):
            p7.terminate()
            print("Playing Fear gesture now...")
            p5 = Process(target=fear_audio)
            p5.start()
            p6 = Process(target=fear_gesture(robot))
            p6.start()

        elif(option==0):
            robot.stop()

        else:
            if(not p7.is_alive()):
                p7 = Process(target=breathing_gesture_head(robot, choice1))
                p7.start()

            if (not p8.is_alive()):
                p8 = Process(target=breathing_gesture_wrist(robot, choice2))
                p8.start()

            if (not p9.is_alive()):
                p9 = Process(target=breathing_gesture_lift(robot, choice3))
                p9.start()

            if (not p10.is_alive()):
                p10 = Process(target=breathing_gesture_base(robot, choice4))
                p10.start()

            if(c1 == 6): c1 = -1
            if(c2 == 3): c2 = -1
            if(c3 == 3): c3 = -1
            if(c4 == 1): c4 = -1

except Exception as e:
    print(e)
    # p8.terminate()