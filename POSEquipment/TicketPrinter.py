import DataModel
from datetime import date, datetime
from serial.serialutil import PARITY_NONE
import serial

escInitPrinter = "\x1b\x40\x0D\x0D"
escPrintNormal = "\x1B\x21\x00"
escPrintBig = "\x1B\x21\x30\x1B\x33\x50"
escPrintBold = "\x1B\x21\x08"
escNewLine = "\x0D\x0A"
escEndAndCut = "\x0D\x0A\x0D\x0A\x0D\x0A\x0D\x0A\x0D\x0A\x0D\x0A\x0D\x0A\x1B\x69\x1B\x70\x00\xFF\x0A\x0D\x0A"

def PrintBill(ticket, paymentMethod, totalAmt, paidAmt, returnAmt, customer):
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

    except serial.serialutil.SerialException:
        s = open("ticket.txt","w")

    s.write(escInitPrinter + escPrintBig)
    s.write("{0:^21}".format('Frituur') + escNewLine)
    s.write("{0:^21}".format('Den Baron') + escNewLine)
    s.write(escPrintNormal + '*****************************************' + escNewLine)
    s.write(escPrintBold + "{0:^40}".format('Rekening') + escNewLine)
    s.write(escPrintNormal + '*****************************************' + escNewLine)
    s.write(
        '{0}     {1}'.format(date.today().strftime('%d/%m/%Y'), datetime.today().strftime('%H:%M')) + escNewLine)
    s.write('-----------------------------------------' + escNewLine)

    body = ""
    for (k, v) in ticket.GetTicketLinesGrouped().iteritems():
        body += "{0[0]:<4.0f} {0[1]:<26}{0[2]:>8.2f}{1:>}".format(v, escNewLine)

    s.write('{0}'.format(body))
    s.write('-----------------------------------------' + escNewLine)
    s.write(escPrintBold + u"Totaal: {0:>10.2f}".format(totalAmt) + escNewLine)
    s.write(u"Betaald:{0:>10.2f}".format(paidAmt) + escNewLine)
    s.write(u"Terug:  {0:>10.2f}".format(returnAmt) + escNewLine)
    s.write(escPrintNormal + escNewLine + 'Betalingswijze: %s' % (
        "Cash" if paymentMethod == 1 else "Atos") + escNewLine)

    if customer.id:
        s.write('-----------------------------------------' + escNewLine)
        s.write('Klantkaart: {0:>s}'.format(customer.loyaltyCardNo) + escNewLine)
        s.write('Punten Ticket: {0:>.0f}'.format(ticket.GetLoyaltyCardPoints()) + escNewLine)
        s.write('Nieuw saldo: {0:>.0f}'.format(customer.loyaltyPoints) + escNewLine)

    s.write('*****************************************' + escNewLine)
    s.write(escPrintBold + "{0:^40}".format('Smakelijk!') + escPrintNormal + escNewLine + escNewLine)
    s.write("{0:^40}".format('Belgian Food Group bvba') + escNewLine)
    s.write("{0:^40}".format('Baron R. De Vironlaan 172') + escNewLine)
    s.write("{0:^40}".format('1700 Dilbeek') + escNewLine)
    s.write("{0:^40}".format('BTW BE0886.290.879') + escNewLine)
    s.write(escEndAndCut)

    s.close()

def PrintKitchenBill(body, eatInOut):
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

    except serial.serialutil.SerialException:
        s = open("kitchenBill.txt","w")

    s.write(escInitPrinter + escPrintNormal)
    s.write('*****************************************' + escNewLine)
    s.write(escPrintBold + "{0:^40}".format('Keukenbon') + escNewLine)
    s.write(escPrintNormal + '*****************************************' + escNewLine)
    s.write(
        '{0}     {1}'.format(date.today().strftime('%d/%m/%Y'), datetime.today().strftime('%H:%M')))

    if eatInOut == 'I':
        s.write(escPrintBold + "              EAT IN" + escNewLine)
    else:
        s.write(escPrintBold + "            TAKE OUT" + escNewLine)
    s.write(escPrintNormal + '-----------------------------------------' + escNewLine)
    s.write(escPrintBig + body)
    s.write(escPrintNormal + '-----------------------------------------' + escNewLine)
    s.write(escEndAndCut)

    s.close()


def PrintDayTotals(dayParam, printDate = datetime.today()):
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

    except serial.serialutil.SerialException:
        s = open("dayTotals.txt","w")

    s.write(escInitPrinter)
    s.write(escPrintNormal + '----------------------------------------' + escNewLine)
    s.write(escPrintNormal + 'Maatsch. :BELGIAN FOOD GROUP BVBA' + escNewLine)
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

    s.write(escPrintNormal + 'CASH' + "{0:>36.2f}".format(dayParam['payedAmts']["Cash"]) + escNewLine)
    s.write(escPrintNormal + 'ATOS' + "{0:>36.2f}".format(dayParam['payedAmts']["Atos"]) + escNewLine)
    s.write(escPrintNormal + '                              -----------' + escNewLine)
    s.write(escPrintNormal + 'TOTAAL' + "{0:>34.2f}".format(dayParam['payedAmts']["Total"]) + escNewLine)
    s.write(escPrintNormal + '                              ===========' + escNewLine)
    s.write(escPrintNormal + 'Algemeen Totaal' + "{0:>25.2f}".format(
        dayParam['payedAmts']["Total"]) + escNewLine + escNewLine)

    s.write(escPrintBig + '       B T W' + escNewLine)
    s.write(escPrintBig + '       -----' + escNewLine + escNewLine)
    s.write(escPrintNormal + '    %         EBTW       BTW      TOTAAL' + escNewLine)
    s.write(escPrintNormal + '----------------------------------------' + escNewLine)
    for VATLine in dayParam['VATLines']:
        s.write(
            escPrintNormal + '{0[0]:>10.2f}{0[1]:>10.2f}{0[2]:>10.2f}{0[3]:>10.2f}'.format(VATLine) + escNewLine)
    s.write(escPrintNormal + '        ---------   -------   ---------' + escNewLine)
    s.write(escPrintNormal + '{0[0]:>20.2f}{0[1]:>10.2f}{0[2]:>10.2f}'.format(dayParam['VATTotals']) + escNewLine)
    s.write(escNewLine)

    for dtype in DataModel.Ticket.discountTypes:
        if dtype != 'none':
            offers = dayParam['offers'][dtype]
            if offers:
                s.write(escPrintNormal + '----------------------------------------' + escNewLine)
                s.write(escPrintBold + dtype + escNewLine)
                s.write(escPrintNormal + '----------------------------------------' + escNewLine)
                if dtype == 'Commerciele korting':
                    s.write('{0[3]:<23}{0[4]:>10.2f}'.format(offers[0]) + escNewLine) #artikel
                else:
                    for offer in offers:
                        s.write('{0:}: {1[3]:<23}{1[4]:>10.2f}'.format(offer[8].strftime("%H:%M"), offer) + escNewLine) #artikel

    s.write(escPrintNormal + '========================================' + escNewLine)
    s.write(escPrintNormal + '    AFDRUKKEN OP %s OM %s' % (
        printDate.strftime('%d/%m/%Y'), printDate.strftime('%H:%M')) + escNewLine)
    s.write(escPrintNormal + '========================================' + escNewLine)

    s.write(escEndAndCut)

    s.close()

def PrintItemTotals(totals):
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

    except serial.serialutil.SerialException:
        s = open("itemTotals.txt","w")

    s.write(escInitPrinter)
    s.write(escPrintNormal + '----------------------------------------' + escNewLine)
    s.write('  Artikelen' + escNewLine)
    s.write('----------------------------------------' + escNewLine + escNewLine)

    grandTotAmt = 0
    for line in totals:
        s.write(escPrintBold + '{0:<}'.format(line[1]) + escPrintNormal + escNewLine) #groepnaam
        itemQtyTotal = 0
        amountTotal = 0
        for itemLine in line[2]:
            s.write('{0[0]:>3.0f} {0[1]:>4d} {0[2]:<21}{0[3]:>10.2f}'.format(itemLine) + escNewLine) #artikel
            itemQtyTotal += itemLine[0]
            amountTotal += itemLine[3]
            grandTotAmt += itemLine[3]

        s.write(
            escPrintBold + '{0:>3.0f}{1:>37.2f}'.format(itemQtyTotal, amountTotal) + escNewLine + escNewLine) #totalen

    s.write(
        escPrintBold + '{0:>40.2f}'.format(grandTotAmt) + escNewLine + escNewLine) #totalen

    s.write(escNewLine + escNewLine)
    s.write(escPrintNormal + '========================================' + escNewLine)
    s.write(escPrintNormal + '    AFDRUKKEN OP {0:>s} OM {1:>s}'.format(datetime.now().strftime('%d/%m/%Y'),
                                                                        datetime.now().strftime(
                                                                            '%H:%M')) + escNewLine)
    s.write(escPrintNormal + '========================================' + escNewLine)

    s.write(escEndAndCut)

    s.close()
