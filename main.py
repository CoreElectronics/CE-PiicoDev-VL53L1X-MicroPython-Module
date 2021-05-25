from PiicoDev_VL53L1X import PiicoDev_VL53L1X
from time import sleep

distSensor = PiicoDev_VL53L1X()

while True:
    dist = distSensor.read() # read the distance in millimetres
    print(str(dist) + " mm") # convert the number to a string and print
    sleep(0.1)
