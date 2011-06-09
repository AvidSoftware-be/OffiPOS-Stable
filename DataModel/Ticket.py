import POSEquipment.CustomerDisplay
import POSEquipment.TicketPrinter

__author__ = 'dennis'

import sqlite3
import ini

class Ticket:
    def __init__(self):
        self.no=0
        self.eatInOut="O"
        self.conn = sqlite3.connect(ini.DB_NAME)

    def AddTicketLine(self, productId):
        val = (self.no, productId, self.eatInOut)

        cur = self.conn.cursor()

        cur.execute("insert into ticketLine (ticketNo,productId,eatInOut) values (?,?,?)", val)

        self.conn.commit()

        self._display()

    def CreateNewTicket(self):
        cur = self.conn.cursor()
        cur.execute("select max(ticketNo) from ticketLine")
        line = cur.fetchone()
        if line is None:
            self.no=1
        else:
            self.no=line[0]+1

        self.eatInOut="O"

    def CancelTicket(self):
        cur = self.conn.cursor()

        cur.execute("delete from ticketLine where ticketNo=?",(self.no,))

        self.conn.commit()

    def PayTicket(self):
        cur = self.conn.cursor()

        cur.execute("update ticketLine set paid=1 where ticketNo=?",(self.no,))

        self.conn.commit()
        self._printTicket()

    def SetEatInOut(self, code):

        cur = self.conn.cursor()

        cur.execute("update ticketLine set eatInOut=? where ticketNo=?",(code, self.no,))

        self.conn.commit()

        self.eatInOut = code

    def GetTicketLines(self):
        cur = self.conn.cursor()
        cur.execute("select product.name, product.price from ticketLine, product where ticketline.productId=product.id and ticketline.ticketNo=?",(self.no,))
        lines = cur.fetchall()
        return lines

    def _display(self):
        lines = self.GetTicketLines()

        lastline = lines[len(lines)]

        POSEquipment.CustomerDisplay.Print("%s".format(lastline[0]).ljust(16,' ') + "%s".format(lastline[1]).ljust(4,' ') + "test".ljust(20,' '))

    def _printTicket(self):

        body = ""

        for line in self.GetTicketLines():
            body = "{0:>s}{1[0]:<30}{1[1]:>8.2}\x0D\x0A".format(body, line)

        POSEquipment.TicketPrinter.PrintBill(body, self.GetTotalAmt())

    def GetTotalAmt(self):

        ticketLines = self.GetTicketLines()
        total = 0

        for line in ticketLines:
            total = total + line[1]

        return total

