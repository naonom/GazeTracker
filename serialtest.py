import serial
import time

com = '/dev/tty.usbserial-3552041E93'
ser = serial.Serial(com, 9600, timeout=None)

while True:
    time.sleep(0.1)

    result = ser.read_all()
    print(result)
    if result == b'\r':	# <Enter>で終了
        break
print('program end')
 
ser.close()