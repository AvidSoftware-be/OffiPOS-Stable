from datetime import date, datetime
from serial.serialutil import PARITY_NONE

__author__ = 'dennis'

import serial

escInitPrinter = "\x1b\x40\x0D\x0D"
escPrintNormal = "\x1B\x21\x00"
escPrintBig = "\x1B\x21\x30\x1B\x33\x50"
escPrintBold = "\x1B\x21\x08"
escNewLine = "\x0D\x0A"
escEndAndCut = "\x0D\x0A\x0D\x0A\x0D\x0A\x0D\x0A\x0D\x0A\x0D\x0A\x0D\x0A\x1B\x69\x1B\x70\x00\xFF\x0A\x0D\x0A"

def PrintBill(body, paymentMethod, totalAmt, paidAmt, returnAmt):
    try:
        s = serial.Serial(1,
                          baudrate=9600, # baudrate
                          bytesize=8, # number of databits
                          parity=PARITY_NONE, # enable parity checking
                          stopbits=1, # number of stopbits
                          timeout=3, # set a timeout value, None for waiting forever
                          xonxoff=0, # enable software flow control
                          rtscts=0, # enable RTS/CTS flow control
        )
        s.setRTS(1)
        s.setDTR(1)
        s.flushInput()
        s.flushOutput()

        s.close()
        s.open()

        s.write(escInitPrinter + escPrintBig)
        s.write('Frituur' + escNewLine)
        s.write('Den Baron' + escNewLine)
        s.write(escPrintNormal + '*****************************************' + escNewLine)
        s.write(escPrintBold + 'Rekening' + escNewLine)
        s.write(escPrintNormal + '*****************************************' + escNewLine)
        s.write(
            '{0}     {1}'.format(date.today().strftime('%d/%m/%Y'), datetime.today().strftime('%H:%M')) + escNewLine)
        s.write('-----------------------------------------' + escNewLine)
        s.write('{0}'.format(body))
        s.write('-----------------------------------------' + escNewLine)
        s.write(escPrintBig + u"Totaal: {0:>10.2f}".format(totalAmt) + escNewLine)
        s.write(u"Betaald:{0:>10.2f}".format(paidAmt) + escNewLine)
        s.write(u"Terug:  {0:>10.2f}".format(returnAmt) + escNewLine)
        s.write(escPrintNormal + 'Betalingswijze: %s' % ("Cash" if paymentMethod == 1 else "Atos") + escNewLine)
        s.write('*****************************************' + escNewLine)
        s.write(escPrintBold + 'Smakelijk!' + escPrintNormal + escNewLine)
        s.write(escEndAndCut)

        s.close()
    except serial.serialutil.SerialException:
        pass


def PrintKitchenBill(body):
    try:
        s = serial.Serial(1,
                          baudrate=9600, # baudrate
                          bytesize=8, # number of databits
                          parity=PARITY_NONE, # enable parity checking
                          stopbits=1, # number of stopbits
                          timeout=3, # set a timeout value, None for waiting forever
                          xonxoff=0, # enable software flow control
                          rtscts=0, # enable RTS/CTS flow control
        )
        s.setRTS(1)
        s.setDTR(1)
        s.flushInput()
        s.flushOutput()

        s.close()
        s.open()

        s.write(escInitPrinter + escPrintNormal)
        s.write('*****************************************' + escNewLine)
        s.write(escPrintBold + 'Keukenbon' + escNewLine)
        s.write(escPrintNormal + '*****************************************' + escNewLine)
        s.write(
            '{0}     {1}'.format(date.today().strftime('%d/%m/%Y'), datetime.today().strftime('%H:%M')) + escNewLine)
        s.write('-----------------------------------------' + escNewLine)
        s.write(escPrintBig + body)
        s.write(escPrintNormal + '-----------------------------------------' + escNewLine)
        s.write(escEndAndCut)

        s.close()
    except serial.serialutil.SerialException:
        pass


def PrintDayTotals(dayParam):
    try:
        s = serial.Serial(1,
                          baudrate=9600, # baudrate
                          bytesize=8, # number of databits
                          parity=PARITY_NONE, # enable parity checking
                          stopbits=1, # number of stopbits
                          timeout=3, # set a timeout value, None for waiting forever
                          xonxoff=0, # enable software flow control
                          rtscts=0, # enable RTS/CTS flow control
        )
        s.setRTS(1)
        s.setDTR(1)
        s.flushInput()
        s.flushOutput()

        s.close()
        s.open()

        s.write(escInitPrinter)
        s.write(escPrintNormal + '----------------------------------------' + escNewLine)
        s.write(escPrintNormal + 'Maatsch. :ML SOLUTIONS BVBA' + escNewLine)
        s.write(escPrintNormal + 'B.T.W. :BE0886.290.879' + escNewLine)
        s.write(escPrintNormal + 'Site : DEN BARON' + escNewLine)
        s.write(escPrintNormal + 'Kassa Nr : 1' + escNewLine)
        s.write(
            escPrintNormal + 'Eerste bestelling : ' + "%s" % dayParam['firstOrder'].strftime('%d/%m/%Y') + escNewLine)
        s.write(
            escPrintNormal + 'Laatste bestelling : ' + "%s" % dayParam['lastOrder'].strftime('%d/%m/%Y') + escNewLine)
        s.write(
            escPrintNormal + 'Eerste bestelling : ' + "%s" % dayParam['firstOrder'].strftime('%H:%M') + escNewLine)
        s.write(
            escPrintNormal + 'Laatste bestelling : ' + "%s" % dayParam['lastOrder'].strftime('%H:%M') + escNewLine)
        s.write(escPrintNormal + '----------------------------------------' + escNewLine)

        s.write(escPrintBig + '  BETALINGSBEWIJZEN' + escNewLine)
        s.write(escPrintBig + '  -----------------' + escNewLine + escPrintNormal + escNewLine)

        s.write(escPrintNormal + 'CASH' + "%s" % dayParam['payedAmts']["Cash"] + escNewLine)
        s.write(escPrintNormal + 'ATOS' + "%s" % dayParam['payedAmts']["Atos"] + escNewLine)
        s.write(escPrintNormal + '                              -----------' + escNewLine)
        s.write(escPrintNormal + 'TOTAAL' + "%s" % dayParam['payedAmts']["Total"] + escNewLine)
        s.write(escPrintNormal + '                              ===========' + escNewLine)
        s.write(escPrintNormal + 'Algemeen Totaal' + "%s" % dayParam['payedAmts']["Total"] + escNewLine + escNewLine)

        s.write(escPrintBig + '       B T W' + escNewLine)
        s.write(escPrintBig + '       -----' + escNewLine + escNewLine)
        s.write(escPrintNormal + '    %         EBTW       BTW      TOTAAL' + escNewLine)
        s.write(escPrintNormal + '----------------------------------------' + escNewLine)
        for VATLine in dayParam['VATLines']:
            s.write(escPrintNormal + '    %s         %s       %s      %s' % VATLine + escNewLine)
        s.write(escPrintNormal + '        ---------   -------   ---------' + escNewLine)
        s.write(escPrintNormal + '                   %s       %s      %s' % dayParam['VATTotals'] + escNewLine)
        s.write(escNewLine + escNewLine)
        s.write(escPrintNormal + '========================================' + escNewLine)
        s.write(escPrintNormal + '    AFDRUKKEN OP %s OM %s' % (
        datetime.now().strftime('%d/%m/%Y'), datetime.now().str('%H:%M')) + escNewLine)
        s.write(escPrintNormal + '========================================' + escNewLine)

        s.write(escEndAndCut)

        s.close()
    except serial.serialutil.SerialException:
        pass

