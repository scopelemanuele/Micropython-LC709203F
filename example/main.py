# This is your main script.
import machine
from LC709203F import BatteryMonitor
from time import sleep

i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=300000)
FuelGauge = BatteryMonitor(bus=i2c)
print("FuelGauge is Ready")
while True:
    battMon = FuelGauge.selfTest()
    sleep(2)
