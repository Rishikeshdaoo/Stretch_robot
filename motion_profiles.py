import time
import stretch_body.robot

r = stretch_body.robot.Robot()
r.startup()

if not r.is_calibrated():
    print("Run the homing script to calibrate the robot first.")
    exit()

print("WARNING: Base will move")
time.sleep(1)
r.stow()

print("move forward 0.2m default speed")
r.base.translate_by(0.2, r.base.params['motion']['default']['vel_m'])
r.push_command()
time.sleep(2)

print("move backward 0.2m slow speed")
r.base.translate_by(-0.2, r.base.params['motion']['slow']['vel_m'])
r.push_command()
time.sleep(2)

print("move forward 0.2m fast speed")
r.base.translate_by(0.2, r.base.params['motion']['fast']['vel_m'])
r.push_command()
time.sleep(2)

print("move backward 0.2m default speed")
r.base.translate_by(-0.2, r.base.params['motion']['default']['vel_m'])
r.push_command()
time.sleep(2)

print("move forward 0.2m custom 0.05m/s speed")
r.base.translate_by(0.2, 0.05)
r.push_command()
time.sleep(2)

print("move backward 0.2m custom 0.05m/s speed")
r.base.translate_by(-0.2, 0.05)
r.push_command()
time.sleep(2)

r.stop()
