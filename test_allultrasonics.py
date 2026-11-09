from gpiozero import DistanceSensor
from time import sleep

# Define each sensor with its respective Echo and Trigger pins
# (Make sure to match these with the pins you selected)
sensors = {
    "Front": DistanceSensor(echo=24, trigger=23),
    "Right": DistanceSensor(echo=25, trigger=8),
    "Rear":  DistanceSensor(echo=7,  trigger=1),
    "Left":  DistanceSensor(echo=16, trigger=20)
}

print("Scanning all 4 ultrasonic zones sequentially...")

try:
    while True:
        readings = {}
        for name, sensor in sensors.items():
            # Distance is read in meters; multiply by 100 for centimeters
            readings[name] = sensor.distance * 100
            # Brief pause between firing each sensor to avoid crosstalk
            sleep(0.05) 
            
        print(f"Front: {readings['Front']:.1f}cm | Right: {readings['Right']:.1f}cm | Rear: {readings['Rear']:.1f}cm | Left: {readings['Left']:.1f}cm")
        sleep(0.2)
        
except KeyboardInterrupt:
    print("\nScan stopped.")
