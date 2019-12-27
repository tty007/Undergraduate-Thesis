import serial
import sys
import time

h = serial.Serial("/dev/tty.Bluetooth-Incoming-Port",baudrate=9600,timeout=0.5)
h.flushInput()

# h.write(b"\xf0")
# rx = h.read(130)
# print(rx)

# while True:
#     time.sleep(1)
#     h.write(bytes([0xf0]))
#     s = h.read(33)
#     print(sys.getsizeof(s))
#     if (sys.getsizeof(s) < 33): continue
#     print(s)

buff = bytearray()

while len(buff) < 130:
    h.write(b"\xf0")
    buff += h.readline()

print(buff)

h.close()