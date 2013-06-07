import serial

class Arduino(object):
    """ Class that handles acquiring the serial data 
        from the arduino for Data Acquisiton
        
        CH0 and CH1 on the arduino are reserved for
        serial so they are not part of the DAQ
    """
    def __init__(self, usbport, baud):
        self.ser = serial.Serial(
             port=usbport,
             baudrate=baud,
             bytesize=serial.EIGHTBITS,
             parity=serial.PARITY_NONE,
             stopbits=serial.STOPBITS_ONE,
             timeout=1,
             xonxoff=0,
             rtscts=0,
             interCharTimeout=None
            )
        #print "Serial Connected"

    def poll(self):
        self.ser.flush() #flush before sending signal
        self.ser.write('w') #send signal telling Arduino to send data
        
        # now read all lines sent by the Arduino
        data = []
        
        # read digital channels
        for i in range(2,13+1): # read channels 2 to 13, range stops 1 shorth thus plus 1
            data.append( int(self.ser.readline()[0:-2]) )
        
        # read analog channels
        for i in range(0,5+1): # now read the 6 analog channel
            data.append( int(self.ser.readline()[0:-2]) ) #this line will crash when running "test" because it sends strings not ints
        
        return data
