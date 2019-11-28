
class HeaderFormat:
    def __init__(self):
        self.headerFormat = None

        #version+Type+TokenLength
        self.header1 = None

        #RR code
        self.response = None

        self.version = 0
        self.messageType = 0
        self.tokenLength = 0
        self.responseClass = 0
        self.responseCode = 0
        self.messageId = 0
        self.token = 0

    def SetHeaderFormat(self, msg):
        self.header = msg
        self.version = self.header[0:2]
        self.messageType = self.header[2:4]
        self.tokenLength = self.header[4:8]
        self.responseClass = self.header[8:11]
        self.responseCode = self.header[11:16]
        self.messageId = self.header[16:32]
        if(self.getTokenLength() > 0):
            self.tokenLength = self.header[32:32 + self.getTokenLength() * 8]
        else:
            self.token = None

    def setMessageId(self, a):
        self.messageId = format(a, '016b')

    def setToken(self, a):
        if(self.getTokenLength() > 0 and self.getTokenLength() < 8 ):
            self.token = format(a, '0' + str(self.getTokenLength() * 8) + 'b')

    def setHeader1(self, version, type, tkl):
        self.version = format(version, '02b')
        self.messageType = format(type, '02b')
        self.tokenLength = format(tkl, '04b')
        self.header1 = (version << 6)+(type << 4)+tkl
        self.header1 = format(self.header1, '08b')

    def setResponse(self, clas, code):
        self.responseClass = format(clas, '03b')
        self.responseCode = format(code, '05b')
        self.response = (clas << 5) + code
        self.response = format(self.response, '08b')

    def buildHeaderFormat(self):
        if(self.getTokenLength() > 0):
            self.headerFormat = "" + str(self.header1) + str(self.response) + str(self.messageId) + str(self.token)
        else:
            self.headerFormat = "" + str(self.header1) + str(self.response) + str(self.messageId)
        return self.headerFormat

    def getTokenLength(self):
        return int(str(self.tokenLength), 2)

    def getVersion(self):
        return int(str(self.version), 2)

    def getMessageType(self):
        return int(str(self.messageType), 2)

    def getMessageId(self):
        return int(str(self.messageId), 2)

    def getResponseCode(self):
        return int(str(self.responseCode), 2)

    def getResponseClass(self):
        return int(str(self.responseClass), 2)

    def getToken(self):
        return int(str(self.token), 2)

    def print(self):
        print("\nHeaderFormat: ")
        print("Version = " + str(self.getVersion()))
        print("Message Type= " + str(self.getMessageType()))
        print("Token Length=" + str(self.getTokenLength()))
        print("ResponseClass= " + str(self.getResponseClass()))
        print("ResponseCode= " + str(self.getResponseCode()))
        print("MessageId=" + str(self.getMessageId()))
        print("Token=" + str(self.getToken()))
        print("HeaderFormat-> " + str(self.headerFormat))
        print("HeaderFormat size->" + str(len(self.headerFormat)))







