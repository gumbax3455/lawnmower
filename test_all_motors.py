from gpiozero import Motor
from time import sleep

# Configure motors (right motor pins are swapped to invert direction)
left_motor = Motor(forward=13, backward=19)
right_motor = Motor(forward=18, backward=12)  # Swapped from (12, 18) to invert

print("Starting drivetrain test with inverted right motor...")

# --- 1. Test Left Motor Individually ---
print("\n--- Testing Left Motor ---")
print("Left motor FORWARD at 30% speed...")
left_motor.forward(0.3)
sleep(2)
left_motor.stop()
sleep(1)

print("Left motor BACKWARD at 60% speed...")
left_motor.backward(0.6)
sleep(2)
left_motor.stop()
sleep(1)

# --- 2. Test Right Motor Individually ---
print("\n--- Testing Right Motor ---")
print("Right motor FORWARD at 30% speed (now inverted)...")
right_motor.forward(0.3)
sleep(2)
right_motor.stop()
sleep(1)

print("Right motor BACKWARD at 60% speed...")
right_motor.backward(0.6)
sleep(2)
right_motor.stop()
sleep(1)

# --- 3. Test Both Motors Together ---
print("\n--- Testing Both Motors Together ---")
print("Both motors FORWARD at 40% speed...")
left_motor.forward(0.4)
right_motor.forward(0.4)
sleep(3)

print("Both motors BACKWARD at 40% speed...")
left_motor.backward(0.4)
right_motor.backward(0.4)
sleep(3)

# Stop completely
left_motor.stop()
right_motor.stop()
print("\nTest complete!")
