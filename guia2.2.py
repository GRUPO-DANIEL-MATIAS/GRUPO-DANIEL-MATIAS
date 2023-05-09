import time
import smbus
import struct

bus = smbus.SMBus(1)
address = 0x08

while True:
    temperatura = bus.read_i2c_block_data(8, 0, 4)
    temp = struct.unpack('<f', bytes(temperatura))[0]
    print(f"{temp:.2f}")
    time.sleep(30)
