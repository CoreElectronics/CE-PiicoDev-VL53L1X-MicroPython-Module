from PiicoDev_VL53L1X import PiicoDev_VL53L1X
from time import sleep

dist_sensor = PiicoDev_VL53L1X()

while True:
    # read the distance in millimetres and convert the number to a string and print
    print(str(dist_sensor.read()) + " mm")
    sleep(0.1)
