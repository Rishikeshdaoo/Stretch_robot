#!/usr/bin/env python
import stretch_body.robot
import time

robot=stretch_body.robot.Robot()
robot.startup()

print("Moving base now...")

robot.base.translate_by(-0.5, 1)

robot.push_command()

time.sleep(10)

robot.stop()
