import time
import smbus
import struct

class SensorTemperatura:
    def __init__(self, bus, address):
        self.bus = bus
        self.address = address

    def leer_temperatura(self):
        temperatura = self.bus.read_i2c_block_data(self.address, 0, 4)
        temp = struct.unpack('<f', bytes(temperatura))[0]
        return round(temp, 2)

if __name__ == '__main__':
    bus = smbus.SMBus(1)
    sensor = SensorTemperatura(bus, 0x08)

    while True:
        temp = sensor.leer_temperatura()
        print(f"{temp:.2f}")
        time.sleep(30)
