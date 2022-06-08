# PiicoDev® VL53L1X MicroPython Module

This is the firmware repo for the [Core Electronics PiicoDev® Distance Sensor VL53L1X](https://core-electronics.com.au/catalog/product/view/sku/CE07741)

This module depends on the [PiicoDev Unified Library](https://github.com/CoreElectronics/CE-PiicoDev-Unified). Place `PiicoDev_Unified.py` in the same directory.

See the Quickstart Guides for:
- [Micro:bit v2](https://core-electronics.com.au/tutorials/piicodev-distance-sensor-vl53l1x-micro-bit-guide.html)
- [Raspberry Pi Pico](https://core-electronics.com.au/tutorials/piicodev-distance-sensor-vl53l1x-raspberry-pi-pico-guide.html).
- [Raspberry Pi](https://core-electronics.com.au/tutorials/piicodev-raspberrypi/piicodev-distance-sensor-vl53l1x-raspberry-pi-guide.html)

# Usage
## Example
[main.py](https://github.com/CoreElectronics/CE-PiicoDev-VL53L1X-MicroPython-Module/blob/main/main.py) is a simple example to get started.
```
from PiicoDev_VL53L1X import PiicoDev_VL53L1X
from time import sleep

distSensor = PiicoDev_VL53L1X()

while True:
    dist = distSensor.read() # read the distance in millimetres
    print(str(dist) + " mm") # convert the number to a string and print
    sleep(0.1)
```
## Details
### PiicoDev_VL53L1X(bus=, freq=, sda=, scl=, address=0x29)
Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
bus | int | 0,1 | Raspberry Pi Pico: 0, Raspberry Pi: 1 | I2C Bus.  Ignored on Micro:bit
freq | int | 100-1000000 | Device dependent | I2C Bus frequency (Hz).  Ignored on Raspberry Pi
sda | Pin | Device Dependent | Device Dependent | I2C SDA Pin. Implemented on Raspberry Pi Pico only
scl | Pin | Device Dependent | Device Dependent | I2C SCL Pin. Implemented on Raspberry Pi Pico only
address | int | 0x29 | 0x29 | The VL53L1X Distance Sensor address can be set using the change_addr function.

### PiicoDev_VL53L1X.read()
Parameter | Type | Unit | Description
--- | --- | --- | ---
returned | int | mm | Range

### Using Multiple Sensors
Since the VL53L1X defaults to a single address, multiple sensors on the same bus will conflict. You can use the change_addr function to use something other than the default, but it will be lost on power down. You can use any spare GPIO on your microcontroller to drive the SHT (shutdown) pin low to disable all the sensors you are using, then bring them up one at a time to give them a unique address each time your code starts. Be sure to pick addresses that are at least 2 away from each other, as reading from the sensor uses your set address + 1.

# License
This project is open source - please review the LICENSE.md file for further licensing information.

If you have any technical questions, or concerns about licensing, please contact technical support on the [Core Electronics forums](https://forum.core-electronics.com.au/).

*\"PiicoDev\" and the PiicoDev logo are trademarks of Core Electronics Pty Ltd.*
