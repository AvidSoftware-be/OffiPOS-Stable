import datetime
from DataModel.Product import Product
import POSEquipment.CustomerDisplay
import POSEquipment.TicketPrinter
from mx.DateTime.ISO import ParseDateTimeUTC

__author__ = 'dennis'

import sqlite3
import ini

paymentMethods = dict(Cash=1, Atos=2)
priceModes = dict(pos=1, neg=2)

class Ticket:
    def __init__(self):
        self.no = 0
        self.eatInOut = "O"
        self.priceMode = priceModes["pos"]
        self.conn = sqlite3.connect(ini.DB_NAME)

    def AddTicketLine(self, productId, isOption, price=0):
        product = Product(productId)
        product.fill()

        if price:
            product.price = price #er werd een prijs meegegeven die de productprijs vervangt

        if isOption:
            product.price = product.price - (product.price * (product.discountIfOption) / 100)

        if self.priceMode == priceModes["neg"]:
            product.price = product.price * -1

        vatcode = 0
        if self.eatInOut == "O":
            vatcode = product.vatCodeOut
        elif self.eatInOut == "I":
            vatcode = product.vatCodeIn

        val = (
        self.no, productId, product.name, product.price, self.eatInOut, isOption, datetime.datetime.now(), vatcode)

        cur = self.conn.cursor()

        cur.execute(
            "insert into ticketLine (ticketNo,productId,productName,price,eatInOut,isOption,dateRegistered,vatCode) values (?,?,?,?,?,?,?,?)"
            , val)

        self.conn.commit()

        lines = self.GetTicketLines()
        totalAmt = self.GetTotalAmt()
        lastline = lines[len(lines) - 1]

        self._displayMessage("{0:<15s}".format(lastline[0]) + "{0:>5.2f}".format(lastline[1]) +
                             "Subtotaal:".ljust(15, ' ') + "{0:>5.2f}".format(totalAmt).ljust(5, ' '))

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
            "select productName, price, isOption, productId, entryNo from ticketLine where ticketline.ticketNo=?"
            , (self.no,))
        lines = cur.fetchall()

        return lines

    def GetTicketLinesGrouped(self):
        cur = self.conn.cursor()
        cur.execute(
            "SELECT count(productId) as qty, productName, sum(price) as lineAmt" +
            "FROM ticketLine" +
            "WHERE ticketNo = ?" +
            "GROUP BY productId", (self.no))

        lines = cur.fetchall()

        return lines

    def DeleteTickeLine(self, entryNo):
        cur = self.conn.cursor()

        cur.execute("delete from ticketLine where entryNo=?", (entryNo,))

        self.conn.commit()

    def _displayMessage(self, message):
        POSEquipment.CustomerDisplay.Print(message)

    def _printTicket(self, paymentMethod, paidAmt, returnAmt):
        body = ""

        for line in self.GetTicketLinesGrouped():
            body += "%s%s" % ("{0[0]:<30}{0[1]:>8.2f}".format(line), POSEquipment.TicketPrinter.escNewLine)

        POSEquipment.TicketPrinter.PrintBill(body, paymentMethod, self.GetTotalAmt(), paidAmt, returnAmt)

    def _printKitchen(self):
        body = ""

        lines = self.GetTicketLinesGrouped()

        for line in lines:
            body += "{0:>2s} {01:>s}{2:>s}".format(line[0], line[1], POSEquipment.TicketPrinter.escNewLine)

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

    def GetPaymentTotal(self, paymentType):
        cur = self.conn.cursor()
        cur.execute("select SUM(price) from ticketLine where paid=?", (paymentType,))
        line = cur.fetchone()
        return line[0]

    def GetVATLines(self):
        cur = self.conn.cursor()
        cur.execute("select * from vatCode")
        lines = cur.fetchall()

        VATLines = []

        for line in lines:
            vatPct = line[2]
            cur.execute("select SUM(price) from ticketLine where vatCode=?", (line[0],))
            totAmt = cur.fetchone()

            if totAmt[0]:
                vat = totAmt[0] * (vatPct / 100)
                evat = totAmt[0] - vat
                tot = totAmt[0]
            else:
                vat = 0
                evat = 0
                tot = 0

            VATLines.append([vatPct, evat, vat, tot])

        return VATLines