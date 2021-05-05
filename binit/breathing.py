import time
import stretch_body.robot

def breathing_gesture_wrist(robot):
    arm_vel_slow_m = robot.robot_params['wrist_yaw']['motion']['slow']['vel']
    arm_accel_slow_m = robot.robot_params['wrist_yaw']['motion']['slow']['accel']

    while True:
        print("wrist1")
        robot.end_of_arm.move_to('wrist_yaw', -0.5, v_r=arm_vel_slow_m, a_r=arm_accel_slow_m)
        time.sleep(1.5)

        print("wrist2")
        robot.end_of_arm.move_to('wrist_yaw', 0.3, v_r=arm_vel_slow_m, a_r=arm_accel_slow_m)
        time.sleep(1.5)

        print("wrist3")
        robot.end_of_arm.move_to('wrist_yaw', -0.3, v_r=arm_vel_slow_m, a_r=arm_accel_slow_m)
        time.sleep(1.5)

        print("wrist4")
        robot.end_of_arm.move_to('wrist_yaw', 0.5, v_r=arm_vel_slow_m, a_r=arm_accel_slow_m)
        time.sleep(1.5)

        print("wrist5")
        robot.end_of_arm.move_to('wrist_yaw', 0.1, v_r=arm_vel_slow_m, a_r=arm_accel_slow_m)
        time.sleep(1.5)

    return

def breathing_gesture_lift(robot):
    lift_vel_slow_m = robot.lift.params['motion']['slow']['vel_m']
    lift_accel_slow_m = robot.lift.params['motion']['slow']['accel_m']

    while True:
        print("lift1")
        robot.lift.move_to(x_m=0.8, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)
        robot.push_command()
        time.sleep(3)

        print("lift2")
        robot.lift.move_to(x_m=0.7, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)
        robot.push_command()
        time.sleep(3)

        print("lift3")
        robot.lift.move_to(x_m=0.5, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)
        robot.push_command()
        time.sleep(3)

        print("lift4")
        robot.lift.move_to(x_m=0.6, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)
        robot.push_command()
        time.sleep(3)

        print("lift5")
        robot.lift.move_to(x_m=0.7, v_m=lift_vel_slow_m, a_m=lift_accel_slow_m)
        robot.push_command()
        time.sleep(3)

    return
