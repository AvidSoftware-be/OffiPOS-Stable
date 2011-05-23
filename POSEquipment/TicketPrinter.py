from serial.serialutil import PARITY_NONE

__author__ = 'dennis'

import serial

def Print(stringToPrint):
    s = serial.Serial(1,
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

    s.write('\x1b\x40\x0D\x0D\x1B\x21\x30\x1B\x33\x50')
    s.write('{0}'.format(stringToPrint))
    s.write('\x0D\x0A\x0D\x0A\x0D\x0A\x0D\x0A\x0D\x0A\x0D\x0A\x0D\x0A\x1B\x69\x1B\x70\x00\xFF\x0A\x0D\x0A')

    s.close()


#1B 40 0D 0D 1B 21 30 1B 33 50 0D 0D 0A 1B 21 00   .@...!0.3P....!.
#1B 32 0D 1B 21 00 1B 32 1D 42 00 0D 2A 2A 2A 2A   .2..!..2.B..****
#2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A   ****************
#0D 0A
