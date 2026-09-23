from gpiozero import Motor
from time import sleep

# Configure the motor with GPIO 13 as forward and GPIO 19 as backward
motor = Motor(forward=13, backward=19)

print("Starting single motor test...")

# Spin forward at 40% speed for 2 seconds
motor.forward(0.4)
sleep(2)

# Stop the motor
motor.stop()
sleep(1)

# Spin backward at 40% speed for 2 seconds
motor.backward(0.4)
sleep(2)

# Stop completely
motor.stop()
print("Motor test complete!")
