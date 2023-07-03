_A=None
from PiicoDev_Unified import*
compat_str='\nUnified PiicoDev library out of date.  Get the latest module: https://piico.dev/unified \n'
VL51L1X_DEFAULT_CONFIGURATION=bytes([0,0,0,1,2,0,2,8,0,8,16,1,1,0,0,0,0,255,0,15,0,0,0,0,0,32,11,0,0,2,10,33,0,0,5,0,0,0,0,200,0,0,56,255,1,0,8,0,0,1,219,15,1,241,13,1,104,0,128,8,184,0,0,0,0,15,137,0,0,0,0,0,0,0,1,15,13,14,14,0,0,2,199,255,155,0,0,0,1,1,64])
class PiicoDev_VL53L1X:
	def __init__(self,bus=_A,freq=_A,sda=_A,scl=_A,address=41):
		try:
			if compat_ind>=1:0
			else:print(compat_str)
		except:print(compat_str)
		self.i2c=create_unified_i2c(bus=bus,freq=freq,sda=sda,scl=scl);self.addr=address;self.status=_A;self.reset();sleep_ms(1)
		if self.read_model_id()!=60108:raise RuntimeError('Failed to find expected ID register values. Check wiring!')
		self.i2c.writeto_mem(self.addr,45,VL51L1X_DEFAULT_CONFIGURATION,addrsize=16);sleep_ms(100);self.writeReg16Bit(30,self.readReg16Bit(34)*4);sleep_ms(200)
	def writeReg(self,reg,value):return self.i2c.writeto_mem(self.addr,reg,bytes([value]),addrsize=16)
	def writeReg16Bit(self,reg,value):return self.i2c.writeto_mem(self.addr,reg,bytes([value>>8&255,value&255]),addrsize=16)
	def readReg(self,reg):return self.i2c.readfrom_mem(self.addr,reg,1,addrsize=16)[0]
	def readReg16Bit(self,reg):data=self.i2c.readfrom_mem(self.addr,reg,2,addrsize=16);return(data[0]<<8)+data[1]
	def read_model_id(self):return self.readReg16Bit(271)
	def reset(self):self.writeReg(0,0);sleep_ms(100);self.writeReg(0,1)
	def read(self):
		A='SignalFail'
		try:data=self.i2c.readfrom_mem(self.addr,137,17,addrsize=16)
		except:print(i2c_err_str.format(self.addr));return float('NaN')
		range_status=data[0];stream_count=data[2];dss_actual_effective_spads_sd0=(data[3]<<8)+data[4];ambient_count_rate_mcps_sd0=(data[7]<<8)+data[8];final_crosstalk_corrected_range_mm_sd0=(data[13]<<8)+data[14];peak_signal_count_rate_crosstalk_corrected_mcps_sd0=(data[15]<<8)+data[16];status=_A
		if range_status in(17,2,1,3):self.status='HardwareFail'
		elif range_status==13:self.status='MinRangeFail'
		elif range_status==18:self.status='SynchronizationInt'
		elif range_status==5:self.status='OutOfBoundsFail'
		elif range_status==4:self.status=A
		elif range_status==6:self.status=A
		elif range_status==7:self.status='WrapTargetFail'
		elif range_status==12:self.status='XtalkSignalFail'
		elif range_status==8:self.status='RangeValidMinRangeClipped'
		elif range_status==9:
			if stream_count==0:self.status='RangeValidNoWrapCheckFail'
			else:self.status='OK'
		return final_crosstalk_corrected_range_mm_sd0
	def change_addr(self,new_addr):self.writeReg(1,new_addr&127);sleep_ms(50);self.addr=new_addr