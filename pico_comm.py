from machine import Pin, UART
from utime import sleep

from Communication import *

led = Pin(25, Pin.OUT)
led.value(1)

TX_PIN = const(16)
RX_PIN = const(17)

hc12 = UART(0,9600,parity=None,stop=1,bits=8,rx=Pin(RX_PIN),tx=Pin(TX_PIN),timeout=1)
com = Communication(hc12)


while True:
    msg = com.receive()
    # print(msg)
    sleep(1)
    