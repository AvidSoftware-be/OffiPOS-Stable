__author__ = 'dennis'

import serial

def Print(stringToPrint):
    s = serial.Serial(0,
         baudrate=19200,        # baudrate
         bytesize=EIGHTBITS,    # number of databits
         parity=PARITY_EVEN,    # enable parity checking
         stopbits=STOPBITS_ONE, # number of stopbits
         timeout=3,             # set a timeout value, None for waiting forever
         xonxoff=0,             # enable software flow control
         rtscts=0,              # enable RTS/CTS flow control
    )
    s.setRTS(1)
    s.setDTR(1)
    s.flushInput()
    s.flushOutput()

    s.open()

    s.write('\x01\x0b{0}'.format(stringToPrint))

    s.close()