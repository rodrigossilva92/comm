from time import sleep, localtime, time

### MESSAGE TYPE ID DEFINITION
STR_COM     = 0b10101010    # start communication
END_COM     = 0b01010101    # end communication
UPD_TIME    = 0b11110000    # update time
STR_TRANS   = 0b00001111    # start datalog transfer
MSG_OK      = 0b11001100    # confirmation of message received


MSG_FIELDS  = 5
### MESSAGE = msgID + N x databytes + msgChecksum
MSG_BYTES   = 1 + MSG_FIELDS*4 + 1        # number of bytes of message

class Communication:

    def __init__(self,ser):
        self.ser = ser
        self.started = False    # flag to check if communication has been stablished

    def send(self,msgID,data=[]):
        msg = b''
        msgID = msgID.to_bytes(1,'big')
        msg += msgID

        for i in range(len(data)):
            data_bytes = data[i].to_bytes(4,'big')
            msg += data_bytes

        for i in range(len(data),MSG_FIELDS):
            x = 0
            data_bytes = x.to_bytes(4,'big')
            msg += data_bytes

        ### generate checksum
        ### dummy checksum
        x = 0b11111111
        data_bytes = x.to_bytes(1,'big')
        msg += data_bytes

        print(len(msg),msg)
        self.ser.write(msg)
        sleep(1)

    def receive(self):
        msg = self.ser.read(MSG_BYTES)
        print(msg)
        # try:
        #     print(len(msg),msg)
        # except:
        #     # print(msg)
        #     pass
        
        if msg == None: # empty message
            return False
        if len(msg) != MSG_BYTES:
            return False
        # ### verify checksum

        msgID = msg[0]
        if msgID == STR_COM:
            print("start communication")
            self.send(MSG_OK)
        # elif msgID == UPD_TIME:
        #     print("update time")
        # elif msgID == STR_TRANS:
        #     print("start transfer")
        # if msgID == MSG_OK:
        #     return MSG_OK
        # elif msgID == STR_TRANS:
        #     print("start communication")
        #     self.send(MSG_OK)
        # elif msgID == UPD_TIME:
        #     print("update time")
        #     date    = msg[1:5]
        #     time    = msg[5:9]
        #     date = int.from_bytes(date,'big')
        #     time = int.from_bytes(time,'big')
        #     print(date,time)


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

    def checkCommunication(self):
        return self.started

    def waitReply(self):
        dt = 10
        now = time()
        while time() - now <= 10:
            self.receive()
            # print("waiting")
            # sleep(.5)



    def sendHandshake(self):
        'Send start communication signal.'
        msgID = STR_COM
        # print("send handshake")
        self.send(msgID)
        # self.receive()
            

    def sendDatetime(self,retry=5):
        dt = localtime()[0:6]
        d = dt[0] * 10000 + dt[1] * 100 + dt[2]
        t = dt[3] * 10000 + dt[4] * 100 + dt[5]
        
        msgID = UPD_TIME
        
        data = []
        data.append(d)
        data.append(t)
        
        self.send(msgID,data)
        self.receive()
        
    
    def requestLogTransfer(self):
        msgID = STR_TRANS
        self.send(msgID)
        self.receive()


    def endCommunication(self):
        if self.started:
            self.started = False
            
    def __del__(self):
        print("Communication finished.")