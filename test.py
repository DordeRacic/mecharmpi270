from pymycobot import MechArm270

# Connect to MechArm via USB0 on your Pi
mc = MechArm270('/dev/ttyUSB0')

# Power on all servos
mc.focus_all_servos()

# Define neutral angles for all 6 joints
neutral_angles = [0, 0, 0, 0, 0, 0]

# Send the angles to the arm at a moderate speed (20%)
mc.send_angles(neutral_angles, 20)

# Optional: Wait until arm finishes moving
mc.sync_send_angles(neutral_angles, 20, timeout=15)
#Should commit