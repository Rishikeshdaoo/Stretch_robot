import time
import random
import threading
from multiprocessing import Process, Lock


def solution_case():
    """
    In this case, we use a multiprocessing lock to ensure that each
    breathing_gesture_* function doesn't cause an RPC error by
    attempting a write at the same time as another process. Note that
    each process will start anew, meaning that the robot object won't
    be stateful. This doesn't matter for joint state since we poll
    the motor's microcontroller for this information, but other state
    information may be relevant.
    """

    robot = MockRobot()
    lock = Lock()
    p1 = Process(target=breathing_gesture_lift, args=(robot, 0, lock))
    p2 = Process(target=breathing_gesture_lift, args=(robot, 0, lock))
    p3 = Process(target=breathing_gesture_lift, args=(robot, 0, lock))

    while True:
        choice1 = random.randint(0, 4)
        choice2 = random.randint(0, 4)
        choice3 = random.randint(0, 4)

        # The processes are respawned when they are dead.
        if(not p1.is_alive()):
            p1 = Process(target=breathing_gesture_lift, args=(robot, choice1, lock))
            p1.start()

        if (not p2.is_alive()):
            p2 = Process(target=breathing_gesture_lift, args=(robot, choice2, lock))
            p2.start()

        if (not p3.is_alive()):
            p3 = Process(target=breathing_gesture_lift, args=(robot, choice3, lock))
            p3.start()

# ------------------------------------------------------
# Functions/Classes used in the above code

class MockRobot:
    """
    Simplified version of stretch_body.robot with only the
    relevant locks included.
    """
    def __init__(self):
        self.head = self.Head()
        self.end_of_arm = self.EndOfArm()
        self.lift = self.Lift()
        self.lock = threading.RLock()
        self.counter = 0

    def push_command(self):
        with self.lock:
            self.counter += 1
            print("push_command", self.counter)
            time.sleep(1)

    class Head:
        def __init__(self):
            self.pt_lock = threading.RLock()

        def move_to(self, joint, pos, v_r=0, a_r=0):
            with self.pt_lock:
                print("head", joint, pos, v_r, a_r)

    class EndOfArm:
        def __init__(self):
            self.pt_lock = threading.RLock()

        def move_to(self, joint, pos, v_r=0, a_r=0):
            with self.pt_lock:
                print("wrist", joint, pos, v_r, a_r)

    class Lift:
        def __init__(self):
            self.params = {'motion': {'slow': {'vel_m': 0.12, 'accel_m': 0.01}}}

        def move_to(self, x_m=0, v_m=0, a_m=0):
            print("lift", x_m, v_m, a_m)

# Gesture routine for camera for breathing
def breathing_gesture_head(robot, choice, lock):
    lock.acquire()
    if(choice == 0):
        print("head0")
        robot.head.move_to('head_pan', -0.6, v_r= 0.1, a_r=0.5)

    elif(choice==1):
        print("head1")
        robot.head.move_to('head_tilt', 0.5, v_r= 0.1, a_r=0.5)

    elif(choice==2):
        print("head2")
        robot.head.move_to('head_pan', 0.8, v_r= 0.1, a_r=0.5)

    elif(choice==3):
        print("head3")
        robot.head.move_to('head_tilt', -0.4, v_r= 0.1, a_r=0.5)

    elif(choice==4):
        print("head4")
        robot.head.move_to('head_pan', -0.6, v_r= 0.1, a_r=0.5)

    elif(choice==5):
        print("head5")
        robot.head.move_to('head_tilt', 0.5, v_r= 0.1, a_r=0.5)

    elif(choice==6):
        print("head6")
        robot.head.move_to('head_pan', 0.8, v_r= 0.1, a_r=0.5)

    elif(choice==7):
        print("head7")
        robot.head.move_to('head_tilt', -0.4, v_r= 0.1, a_r=0.5)
    lock.release()

    time.sleep(3)
    return

# Gesture routine for wrist for breathing
def breathing_gesture_wrist(robot, choice, lock):
    lock.acquire()
    if(choice == 0):
        print("wrist0")
        robot.end_of_arm.move_to('wrist_yaw', -0.5, v_r=0.5, a_r=0.5)

    elif(choice == 1):
        print("wrist1")
        robot.end_of_arm.move_to('wrist_yaw', 0.3, v_r=0.5, a_r=0.5)

    elif (choice == 2):
        print("wrist2")
        robot.end_of_arm.move_to('wrist_yaw', -0.3, v_r=0.5, a_r=0.5)

    elif (choice == 3):
        print("wrist3")
        robot.end_of_arm.move_to('wrist_yaw', 0.5, v_r=0.5, a_r=0.5)

    elif (choice == 4):
        print("wrist4")
        robot.end_of_arm.move_to('wrist_yaw', 0.1, v_r=0.5, a_r=0.5)
    lock.release()

    time.sleep(3)
    return

# Gesture routine for lift for breathing
def breathing_gesture_lift(robot, choice, lock):
    lift_vel_slow_m = robot.lift.params['motion']['slow']['vel_m']
    lift_accel_slow_m = robot.lift.params['motion']['slow']['accel_m']

    lock.acquire()
    if(choice == 0):
        print("lift0")
        robot.lift.move_to(x_m=0.8, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)

    elif(choice == 1):
        print("lift1")
        robot.lift.move_to(x_m=0.7, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)

    elif(choice == 2):
        print("lift2")
        robot.lift.move_to(x_m=0.5, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)

    elif(choice == 3):
        print("lift3")
        robot.lift.move_to(x_m=0.6, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)

    elif(choice == 4):
        print("lift4")
        robot.lift.move_to(x_m=0.7, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)
    robot.push_command()
    lock.release()

    # time.sleep(3)
    return

if __name__ == "__main__":
    solution_case()
