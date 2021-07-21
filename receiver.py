from machine import Pin, UART
from utime import sleep

# from Communication import *

led = Pin(25, Pin.OUT)
led.value(1)

TX_PIN = const(16)
RX_PIN = const(17)

hc12 = UART(0,9600,parity=None,stop=1,bits=8,rx=Pin(RX_PIN),tx=Pin(TX_PIN),timeout=1)
# comm = Communication(hc12)


while True:
    # comm.waitHandshake()
    msg = hc12.read()
    print(msg)

    try:
        print(bin(msg[0]))
        date = int.from_bytes(msg[1:5],'big')
        time = int.from_bytes(msg[5:9],'big')
        print(date,time)
    except:
        pass
    sleep(1)

# UPD_TIME    = 0b11110000    # update timer
# x = UPD_TIME.to_bytes(1,'big')
# print(x)
# y = int.from_bytes(x,'big')
# print(y)
# print(bin(y))