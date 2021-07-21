from time import sleep, localtime
import serial

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
    )




while True:
    msg = b''

    UPD_TIME    = 0b11110000    # update timer
    UPD_TIME = UPD_TIME.to_bytes(1,'big')
    msg += UPD_TIME 

    dt = localtime()[0:6]
    d = dt[0] * 10000 + dt[1] * 100 + dt[2]
    t = dt[3] * 10000 + dt[4] * 100 + dt[5]

    # print(d,t)

    d = d.to_bytes(4, 'big')
    t = t.to_bytes(4, 'big')

    # print(d,t)


    msg += d+t
    print(msg)

    ser.write(msg)


    sleep(1)