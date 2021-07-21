<<<<<<< HEAD

=======
from time import sleep, localtime
import serial

from Communication import *

hc12 = serial.Serial(port='/dev/ttyS0',
                    baudrate = 9600,
                    parity = serial.PARITY_NONE,
                    stopbits = serial.STOPBITS_ONE,
                    bytesize = serial.EIGHTBITS,
                    timeout = 1)

com = Communication(hc12)

while True:
    break
>>>>>>> 424d90a032e156253adaf8444393a96efbc1a219
