from serial.serialutil import PARITY_NONE

__author__ = 'dennis'

import serial

def Print(stringToPrint):
    s = serial.Serial(0,
         baudrate=9600,        # baudrate
         bytesize=8,    # number of databits
         parity=PARITY_NONE,    # enable parity checking
         stopbits=1, # number of stopbits
         timeout=3,             # set a timeout value, None for waiting forever
         xonxoff=0,             # enable software flow control
         rtscts=0,              # enable RTS/CTS flow control
    )
    s.setRTS(1)
    s.setDTR(1)
    s.flushInput()
    s.flushOutput()

    s.close()

    s.open()

    s.write('\x01\x0b{0}'.format(stringToPrint))

    s.close()
