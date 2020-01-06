import serial
import sys
import datetime

# h = serial.Serial("/dev/tty.UM24C-Port",baudrate=9600,timeout=0.5)
# win用
h = serial.Serial("COM5",baudrate=9600,timeout=1.5)

def getPowerInfo(h):
  h.write(b"\xf0")
  rx = h.read(130)
  #raw data
  # print(f'0x{rx[2]:02x}{rx[3]:02x}')
  # print(f'0x{rx[4]:02x}{rx[5]:02x}')
  # 0x01ea,0x010dのように表示される
  v = float(rx[2]<<8|rx[3])/100.0
  i = float(rx[4]<<8|rx[5])/1000.0
  w = v * i

  t_now = datetime.datetime.now().time()
  print(t_now)
  print(f'V:{v:.4f} [V]')
  print(f'I:{i:.4f}[A]')
  print(f'W:{w:.4f} [W]')

i=1
while i<10:
  getPowerInfo(h)
  i += 1

h.close()