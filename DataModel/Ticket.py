import datetime
from DataModel.Product import Product
import POSEquipment.CustomerDisplay
import POSEquipment.TicketPrinter
from mx.DateTime.ISO import ParseDateTimeUTC

__author__ = 'dennis'

import sqlite3
import ini

paymentMethods = dict(Cash=1, Atos=2)

class Ticket:
    def __init__(self):
        self.no = 0
        self.eatInOut = "O"
        self.conn = sqlite3.connect(ini.DB_NAME)

    def AddTicketLine(self, productId, isOption):
        product = Product(productId)
        product.fill()

        if isOption:
            product.price = product.price - (product.price * (product.discountIfOption) / 100)

        val = (self.no, productId, product.name, product.price, self.eatInOut, isOption, datetime.datetime.now())

        cur = self.conn.cursor()

        cur.execute(
            "insert into ticketLine (ticketNo,productId,productName,price,eatInOut,isOption,dateRegistered) values (?,?,?,?,?,?,?)"
            , val)

        self.conn.commit()

        lines = self.GetTicketLines()
        totalAmt = self.GetTotalAmt()
        lastline = lines[len(lines) - 1]

        self._displayMessage("{0:s}".format(lastline[0]).ljust(15, ' ') + "{0:.2f}".format(lastline[1]).ljust(5, ' ') +
                             "Subtotaal:".ljust(15, ' ') + "{0:.2f}".format(totalAmt).ljust(5, ' '))

    def CreateNewTicket(self):
        cur = self.conn.cursor()
        cur.execute("select max(ticketNo) from ticketLine")
        line = cur.fetchone()
        if not line:
            self.no = 1
        else:
            self.no = line[0] + 1

        self.eatInOut = "O"

        self._displayMessage("                    " +
                             "       Welkom       ")

    def CancelTicket(self):
        cur = self.conn.cursor()

        cur.execute("delete from ticketLine where ticketNo=?", (self.no,))

        self.conn.commit()

        self._displayMessage("                    " +
                             "   Tot weerziens!   ")

    def PayTicket(self, paymentMethod, paidAmt, returnAmt):
        cur = self.conn.cursor()

        cur.execute("update ticketLine set paid=? where ticketNo=?", (paymentMethod, self.no,))

        self.conn.commit()
        self._printTicket(paymentMethod, paidAmt, returnAmt)
        self._printKitchen()

        self._displayMessage("                    " +
                             "   Tot weerziens!   ")

    def SetEatInOut(self, code):
        cur = self.conn.cursor()

        cur.execute("update ticketLine set eatInOut=? where ticketNo=?", (code, self.no,))

        self.conn.commit()

        self.eatInOut = code

    def GetTicketLines(self):
        cur = self.conn.cursor()
        cur.execute(
            #"select product.name, product.price, ticketLine.isOption, product.discountIfOption, product.id from ticketLine, product where ticketline.productId=product.id and ticketline.ticketNo=?"
            "select productName, price, isOption, productId from ticketLine where ticketline.ticketNo=?"
            , (self.no,))
        lines = cur.fetchall()

        result = []

        #        for line in lines:
        #            #ik kopieer de waardes want een tuple kan je niet wijzigen
        #            newline = []
        #            newline.append(line[0])
        #
        #            if line[2] == 1:
        #                #prijs uit opties halen, korting toepassen dus
        #                newline.append(line[1] - (line[1] * (line[3]) / 100))
        #            else:
        #                newline.append(line[1])
        #
        #            newline.append(line[2])
        #            newline.append(line[2])
        #            newline.append(line[3])
        #            newline.append(line[4])
        #
        #            result.append(newline)

        return lines

    def _displayMessage(self, message):
        POSEquipment.CustomerDisplay.Print(message)

    def _printTicket(self, paymentMethod, paidAmt, returnAmt):
        body = ""

        for line in self.GetTicketLines():
            body += "%s%s" % ("{0[0]:<30}{0[1]:>8.2f}".format(line), POSEquipment.TicketPrinter.escNewLine)

        POSEquipment.TicketPrinter.PrintBill(body, paymentMethod, self.GetTotalAmt(), paidAmt, returnAmt)

    def _printKitchen(self):
        body = ""

        for line in self.GetTicketLines():
            body += "%s%s" % (line[0], POSEquipment.TicketPrinter.escNewLine)

        POSEquipment.TicketPrinter.PrintKitchenBill(body)

    def GetTotalAmt(self):
        ticketLines = self.GetTicketLines()
        total = 0

        for line in ticketLines:
            total = total + line[1]

        return total

    def GetFirstOrderDate(self):
        cur = self.conn.cursor()
        cur.execute("select MIN(dateRegistered) from ticketLine")
        line = cur.fetchone()
        return ParseDateTimeUTC(line[0])

    def GetLastOrderDate(self):
        cur = self.conn.cursor()
        cur.execute("select MAX(dateRegistered) from ticketLine")
        line = cur.fetchone()
        return ParseDateTimeUTC(line[0])

