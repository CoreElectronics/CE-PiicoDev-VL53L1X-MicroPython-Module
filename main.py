from PiicoDev_VL53L1X import PiicoDev_VL53L1X

from utime import sleep_ms

laser = PiicoDev_VL53L1X()

while True:
    dist = laser.read() # read the distance in millimetres
    print("{:4d} | ".format(dist))
    sleep_ms(1000)
