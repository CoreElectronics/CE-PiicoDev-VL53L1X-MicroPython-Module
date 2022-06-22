from PiicoDev_Unified import *


COMPAT_STRING = '\nUnified PiicoDev library out of date.  Get the latest module: https://piico.dev/unified \n'
EXPECTED_MODEL_ID = 0xEACC


VL53L1X_DEFAULT_CONFIGURATION = bytes([
0x00, # 0x2d : set bit 2 and 5 to 1 for fast plus mode (1MHz I2C), else don't touch */
0x00, # 0x2e : bit 0 if I2C pulled up at 1.8V, else set bit 0 to 1 (pull up at AVDD) */
0x00, # 0x2f : bit 0 if GPIO pulled up at 1.8V, else set bit 0 to 1 (pull up at AVDD) */
0x01, # 0x30 : set bit 4 to 0 for active high interrupt and 1 for active low (bits 3:0 must be 0x1), use SetInterruptPolarity() */
0x02, # 0x31 : bit 1 = interrupt depending on the polarity, use CheckForDataReady() */
0x00, # 0x32 : not user-modifiable (NUM)*/
0x02, # 0x33 : NUM */
0x08, # 0x34 : NUM */
0x00, # 0x35 : NUM */
0x08, # 0x36 : NUM */
0x10, # 0x37 : NUM */
0x01, # 0x38 : NUM */
0x01, # 0x39 : NUM */
0x00, # 0x3a : NUM */
0x00, # 0x3b : NUM */
0x00, # 0x3c : NUM */
0x00, # 0x3d : NUM */
0xff, # 0x3e : NUM */
0x00, # 0x3f : NUM */
0x0F, # 0x40 : NUM */
0x00, # 0x41 : NUM */
0x00, # 0x42 : NUM */
0x00, # 0x43 : NUM */
0x00, # 0x44 : NUM */
0x00, # 0x45 : NUM */
0x20, # 0x46 : interrupt configuration 0->level low detection, 1-> level high, 2-> Out of window, 3->In window, 0x20-> New sample ready , TBC */
0x0b, # 0x47 : NUM */
0x00, # 0x48 : NUM */
0x00, # 0x49 : NUM */
0x02, # 0x4a : NUM */
0x0a, # 0x4b : NUM */
0x21, # 0x4c : NUM */
0x00, # 0x4d : NUM */
0x00, # 0x4e : NUM */
0x05, # 0x4f : NUM */
0x00, # 0x50 : NUM */
0x00, # 0x51 : NUM */
0x00, # 0x52 : NUM */
0x00, # 0x53 : NUM */
0xc8, # 0x54 : NUM */
0x00, # 0x55 : NUM */
0x00, # 0x56 : NUM */
0x38, # 0x57 : NUM */
0xff, # 0x58 : NUM */
0x01, # 0x59 : NUM */
0x00, # 0x5a : NUM */
0x08, # 0x5b : NUM */
0x00, # 0x5c : NUM */
0x00, # 0x5d : NUM */
0x01, # 0x5e : NUM */
0xdb, # 0x5f : NUM */
0x0f, # 0x60 : NUM */
0x01, # 0x61 : NUM */
0xf1, # 0x62 : NUM */
0x0d, # 0x63 : NUM */
0x01, # 0x64 : Sigma threshold MSB (mm in 14.2 format for MSB+LSB), use SetSigmaThreshold(), default value 90 mm  */
0x68, # 0x65 : Sigma threshold LSB */
0x00, # 0x66 : Min count Rate MSB (MCPS in 9.7 format for MSB+LSB), use SetSignalThreshold() */
0x80, # 0x67 : Min count Rate LSB */
0x08, # 0x68 : NUM */
0xb8, # 0x69 : NUM */
0x00, # 0x6a : NUM */
0x00, # 0x6b : NUM */
0x00, # 0x6c : Intermeasurement period MSB, 32 bits register, use SetIntermeasurementInMs() */
0x00, # 0x6d : Intermeasurement period */
0x0f, # 0x6e : Intermeasurement period */
0x89, # 0x6f : Intermeasurement period LSB */
0x00, # 0x70 : NUM */
0x00, # 0x71 : NUM */
0x00, # 0x72 : distance threshold high MSB (in mm, MSB+LSB), use SetD:tanceThreshold() */
0x00, # 0x73 : distance threshold high LSB */
0x00, # 0x74 : distance threshold low MSB ( in mm, MSB+LSB), use SetD:tanceThreshold() */
0x00, # 0x75 : distance threshold low LSB */
0x00, # 0x76 : NUM */
0x01, # 0x77 : NUM */
0x0f, # 0x78 : NUM */
0x0d, # 0x79 : NUM */
0x0e, # 0x7a : NUM */
0x0e, # 0x7b : NUM */
0x00, # 0x7c : NUM */
0x00, # 0x7d : NUM */
0x02, # 0x7e : NUM */
0xc7, # 0x7f : ROI center, use SetROI() */
0xff, # 0x80 : XY ROI (X=Width, Y=Height), use SetROI() */
0x9B, # 0x81 : NUM */
0x00, # 0x82 : NUM */
0x00, # 0x83 : NUM */
0x00, # 0x84 : NUM */
0x01, # 0x85 : NUM */
0x01, # 0x86 : clear interrupt, use ClearInterrupt() */
0x40  # 0x87 : start ranging, use StartRanging() or StopRanging(), If you want an automatic start after VL53L1X_init() call, put 0x40 in location 0x87 */
])


class PiicoDev_VL53L1X:
    """
    The VL53L1X IC is used solely used for the PiicoDev
    laser-distance-measurement sensor. This class provides
    methods for an instance to properly initialise and take
    distance measurements
    """

    def __init__(self, bus=None, freq=None, sda=None, scl=None, addr=0x29):
        """
        On instantiation:
        - Check compatibilty with installed PiicoDev_Unified.py
        - Create the i2c instance for serial communication
        - Flip register 0x0 to reset the VL53L1X
        - Confirm the model ID is valid
        - Configure defaults and registers for VL53L1X to allow sensor reading
        """
        try:
            if compat_ind >= 1:
                pass
            else:
                print(COMPAT_STRING)
        except:
            print(COMPAT_STRING)
        self.i2c = create_unified_i2c(bus=bus, freq=freq, sda=sda, scl=scl)
        self.addr = addr
        self.reset()
        sleep_ms(1)
        if self.read_model_id() != EXPECTED_MODEL_ID:
            raise RuntimeError('Failed to find expected ID register values. Check wiring!')
        # write default configuration
        self.i2c.writeto_mem(self.addr, 0x2D, VL53L1X_DEFAULT_CONFIGURATION, addrsize=16)
        sleep_ms(100)
        # the API triggers this change in VL53L1_init_and_start_range() once a
        # measurement is started; assumes MM1 and MM2 are disabled
        self.write_reg_16_bit(0x001E, self.read_reg_16_bit(0x0022) * 4)
        sleep_ms(200)


    # ! Note for reviwer: please confirm that the precondition
    # ! in the docstring is correct
    def write_reg(self, reg, value):
        """
        Helper function to write an 8-bit value from the
        provided register

        Legal reg values: 0x0 through 0x5A
        """
        return self.i2c.writeto_mem(self.addr, reg, bytes([value]), addrsize=16)
   
   
    # ! Note for reviwer: please confirm that the precondition
    # ! in the docstring is correct
    def write_reg_16_bit(self, reg, value):
        """
        Helper function to write a 16-bit value from the
        provided register

        Legal reg values: 0x0 through 0x5A
        """
        return self.i2c.writeto_mem(self.addr, reg, bytes([(value >> 8) & 0xFF, value & 0xFF]), addrsize=16)
   
   
    # ! Note for reviwer: please confirm that the precondition
    # ! in the docstring is correct
    def read_reg(self, reg):
        """
        Helper function to read an 8-bit value from the
        provided register

        Legal reg values: 0x0 through 0x5A
        """
        return self.i2c.readfrom_mem(self.addr, reg, 1, addrsize=16)[0]
   
    # ! Note for reviwer: please confirm that the precondition
    # ! in the docstring is correct
    def read_reg_16_bit(self, reg):
        """
        Helper function to read a 16-bit value from the
        provided register

        Legal reg values: 0x0 through 0x5A
        """
        data = self.i2c.readfrom_mem(self.addr, reg, 2, addrsize=16)
        return (data[0]<<8) + data[1]
    
    
    def read_model_id(self):
        """
        Return the 16-bit value at register 0x010F
        which is the model ID (not the I2C address) of the VL53L1X
        """
        return self.read_reg_16_bit(0x010F) 
    
    
    def reset(self):
        """
        Resets the VL53L1X by setting register 0x0 to 0x0 (off)
        and after 100ms 0x1 (on)
        """
        self.write_reg(0x0000, 0x00)
        sleep_ms(100)
        self.write_reg(0x0000, 0x01)
    
    
    def read(self):
        """
        Return an integer in mm representing the
        distance from the sensor to the surface
        it reflected from

        This is the final crosstalk-corrected range
        (in mm) from sd0
        """
        try:
            data = self.i2c.readfrom_mem(self.addr, 0x0089, 17, addrsize=16) # RESULT__RANGE_STATUS
        except: # ! Note for reviewer: Typically best practice is to catch exceptions based on their name rather than loose except calls
            print(i2c_err_str.format(self.addr))
            return float('NaN')
        return (data[13]<<8) + data[14]


    def change_addr(self, new_addr):
        """
        See README.md for instructions on how to use this method appropriately
        """
        self.write_reg(0x0001, new_addr & 0x7F)
        sleep_ms(50)
        self.addr = new_addr
