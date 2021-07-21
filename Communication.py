from time import localtime

### MESSAGE TYPE ID DEFINITION
STR_COM     = 0b10101010    # start communication
END_COM     = 0b01010101    # end communication
UPD_TIME    = 0b11110000    # update timer
STR_TRANS   = 0b00001111    # start datalog transfer
MSG_OK      = 0b11001100    # confirmation of message received

### MESSAGE = msgID + N x databytes + msgChecksum
MSG_LEN     = 10        # number of bytes of message

class Communication:

    def __init__(self,ser):
        self.ser = ser
        self.started = False    # flag to check if communication has been stablished

    def send(self,msgID,data=[]):
        msg = bytearray(MSG_LEN)
        msg[0] = msgID
        for i in range(len(data)):
            msg[i+1] = data[i]
        for i in range(len(data)+1,MSG_LEN):
            msg[i] = 0b0
        print("Sent: ",end='')
        print(msg)
        #_msg[-1] = self.generateChecksum()
        self.ser.write(msg)

    def receive(self):
        msg = self.ser.read(MSG_LEN)
        print("Received: ",end='')
        print(msg)
#         if msg == None: # empty message
#             return
# #        if self.verifyChecksum(_msg):
# #            return _msg
#         if msg[0] == STR_COM: # answer handshake
#             self.send(STR_COM)
#             self.started = True
#         elif msg[0] == UPD_TIME: # update RTC
#             print("update time")
#             y = (msg[1] << 8) | msg[2]
#             m = msg[3]
#             d = msg[4]
#             h = msg[5]
#             min = msg[6]
#             s = msg[7]
#             datetime = (y,m,d,h,min,s)
#             print(datetime)

    def generateChecksum(self,msg):
        'Creates a 8 bits checksum.'
        msgSum = sum(msg)
        while (msgSum >> 8) > 255:
            msgSum += (msgSum >> 8)
        checksum = ~msgSum & 255
        return checksum

    def verifyChecksum(self,msg):
        'Verify the message 8 bits checksum.'
        if sum(msg) == 255:
            return True

    def sendHandshake(self):
        'Send start communication signal.'
        if not self.started:
            _msgID = STR_COM
            self.send(_msgID)
            self.receive()
    
    def waitHandshake(self):
        'Wait for communication signal.'
        if not self.started:
            self.receive()
            
    def checkCommunication(self):
        return self.started

    def sendDatetime(self,retry=5):
        dt = localtime()[0:6]
        d = dt[0] * 10000 + dt[1] * 100 + dt[2]
        t = dt[3] * 10000 + dt[4] * 100 + dt[5]
        
        msgID = UPD_TIME
        msg = []
        msg.append(d)
        msg.append(t)
        print(msg)
        
        


    def endCommunication(self):
        if self.started:
            self.started = False
            
    def __del__(self):
        print("Communication finished.")