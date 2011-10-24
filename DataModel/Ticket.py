import datetime
from DataModel.Customer import Customer
from DataModel.Menu import ProductMenu
from DataModel.ProductScreen import ProductScreen
from DataModel.Product import Product
import POSEquipment.CustomerDisplay
import POSEquipment.TicketPrinter
from mx.DateTime.ISO import ParseDateTimeUTC

__author__ = 'dennis'

import sqlite3
import ini

paymentMethods = dict(Cash=1, Atos=2)
priceModes = dict(pos=1, neg=2)
discountTypes = {'none': 0, 'Aanbieding Directie': 1, 'Klantkaart': 2, 'Persoonlijk Gebruik': 3,
                 'Commerciele korting': 4}

class Ticket:
    def __init__(self):
        self.no = 0
        self.eatInOut = "O"
        self.priceMode = priceModes["pos"]
        self.conn = sqlite3.connect(ini.DB_NAME, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.customer = Customer()
        self.KitchenPrinted = False
        self.TicketPrinted = False
        self.parentEntryNo = 0

    def AddTicketLine(self, productId, isOption, parentProductId, buttonNo, screenCategory, price=0,
                      discountType=discountTypes["none"], qty=1):
        product = Product(productId)
        product.fill()
        
        isOption = isOption or product.treatAsOption

        if price or (discountType <> discountTypes["none"]):
            product.price = price #er werd een prijs meegegeven die de productprijs vervangt

        if isOption:
            product.price = product.price - (product.price * product.discountIfOption / 100)

            if productId == 9999:
                #speciaal!
                product.name = ProductScreen().GetCaptionForOption(parentProductId, buttonNo)
        else:
            if productId == 9999:
                #speciaal!
                product.name = ProductScreen().GetCaption(buttonNo, screenCategory)

        if self.priceMode == priceModes["neg"]:
            product.price = product.price * -1
            qty = qty * -1

        vatcode = 0
        if self.eatInOut == "O":
            vatcode = product.vatCodeOut
        elif self.eatInOut == "I":
            vatcode = product.vatCodeIn

        val = (
            self.no, productId, product.name.strip(), product.price, self.eatInOut, isOption, datetime.datetime.now(),
            vatcode, discountType, qty )

        cur = self.conn.cursor()

        cur.execute(
            "insert into ticketLine (ticketNo,productId,productName,price,eatInOut,isOption,dateRegistered,vatCode,discountType, quantity) values (?,?,?,?,?,?,?,?,?,?)"
            , val)

        #als dit artikel menuComponents heeft, ook opvullen
        pMenu = ProductMenu(product.id)
        if pMenu.menuComponents:
            parentEntryNo = cur.lastrowid
            for component in pMenu.menuComponents:
                if not component[3]: #name is leeg, begruik die van het gekoppeld product
                    prod = Product(component[2])
                    prod.fill()
                    name = prod.name
                else:
                    name = component[3]

                cur.execute(
                    "insert into ticketLine (ticketNo,productId,productName,price,eatInOut,isOption,dateRegistered,vatCode,discountType, quantity, parentEntryNo) values (?,?,?,?,?,?,?,?,?,?,?)"
                    , (self.no, component[2], name, component[4], self.eatInOut, isOption,
                       datetime.datetime.now(),
                       vatcode, component[5], qty, parentEntryNo ))

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
        if not line[0]:
            self.no = 1
        else:
            self.no = line[0] + 1

        self.eatInOut = "O"
        self.KitchenPrinted = False
        self.TicketPrinted = False

        self._displayMessage("                    " +
                             "       Welkom       ")


    def CancelTicket(self):
        cur = self.conn.cursor()

        cur.execute("update ticketLine set isCancelled = 1 where ticketNo=?", (self.no,))

        self.conn.commit()

        self._displayMessage("                    " +
                             "   Tot weerziens!   ")


    def PayTicket(self, paymentMethod, paidAmt, returnAmt):
        cur = self.conn.cursor()

        cur.execute("update ticketLine set paid=? where ticketNo=?", (paymentMethod, self.no,))

        self.conn.commit()
        
        if not self.TicketPrinted:
            self._printReceipt(paymentMethod, paidAmt, returnAmt)
            
        if not self.KitchenPrinted:
            self.PrintKitchen()

        self._displayMessage("                    " +
                             "   Tot weerziens!   ")


    def SetEatInOut(self, code):
        cur = self.conn.cursor()

        self.eatInOut = code

        #vatcodes en I/O updaten
        lines = self.GetTicketLines()
        for line in lines:

            if line[7]: #er is een parentEntryNo, dus komt het van een menucomponent
                parentLine = self.GetOneTicketLine(line[7])
                product = Product(parentLine[3])
            else:
                product = Product(line[3])

            product.fill()

            vatcode = 0
            if self.eatInOut == "O":
                vatcode = product.vatCodeOut
            elif self.eatInOut == "I":
                vatcode = product.vatCodeIn

            cur.execute("update ticketLine set vatCode = ?, eatInOut=? where entryNo = ?", (vatcode, code, line[4]))

        self.conn.commit()

    def GetTicketLines(self):
        cur = self.conn.cursor()
        cur.execute(
            #"select product.name, product.price, ticketLine.isOption, product.discountIfOption, product.id from ticketLine, product where ticketline.productId=product.id and ticketline.ticketNo=?"
            """select productName, price, isOption, productId, entryNo, isCancelled, discountType, parentEntryNo
                from ticketLine
                where ticketline.ticketNo=? and isCancelled=0"""
            , (self.no,))
        lines = cur.fetchall()

        return lines

    def GetOneTicketLine(self, entryNo):
        cur = self.conn.cursor()
        cur.execute(
            #"select product.name, product.price, ticketLine.isOption, product.discountIfOption, product.id from ticketLine, product where ticketline.productId=product.id and ticketline.ticketNo=?"
            "select productName, price, isOption, productId, entryNo, isCancelled, discountType, parentEntryNo from ticketLine where entryNo=?"
            , (entryNo,))
        line = cur.fetchone()

        return line


    def GetTicketLinesGrouped(self):
        cur = self.conn.cursor()
        cur.execute(
            """SELECT productId, productName, sum(price), isOption, discountType, sum(quantity) as qty FROM ticketLine
            WHERE ticketNo = ? and isCancelled=0 and isOption=0
            group by productId, discountType ORDER BY productId""", (self.no,))

        lines = cur.fetchall()
        groupedLines = {}

        for ticketLine in lines:
            if (ticketLine[0] != 9999) and (not ticketLine[3]) or(
                ticketLine[4]): #geen generieke en geen opties, wel kortingen
                groupedLines[ticketLine[0]] = [ticketLine[5], ticketLine[1], ticketLine[2],
                                               ticketLine[4]] #qty, naam, prijs, discountType

        return groupedLines


    def DeleteTickeLine(self, entryNo):
        cur = self.conn.cursor()

        cur.execute("update ticketLine set isCancelled = 1 where entryNo=?", (entryNo,))

        self.conn.commit()


    def SetCustomer(self, customer):
        self.customer = customer

        cur = self.conn.cursor()

        cur.execute("update ticketLine set customerId = ? where ticketNo=?", (customer.id, self.no,))

        self.conn.commit()


    def _displayMessage(self, message):
        POSEquipment.CustomerDisplay.Print(message)


    def _printReceipt(self, paymentMethod, paidAmt, returnAmt):
        POSEquipment.TicketPrinter.PrintBill(self, paymentMethod, self.GetTotalAmt(), paidAmt, returnAmt, self.customer)


    def PrintKitchen(self):
        body = ""

        #lines = self.GetTicketLinesGrouped()

        #overzicht
        for (k, v) in self.GetTicketLinesGrouped().iteritems():
            if (v[3]==0) or (v[3]==1) or (v[3]==3): #kortingen niet afdrukken
                body += "{0[0]:>2.0f} {0[1]:>}{1:>}".format(v, POSEquipment.TicketPrinter.escNewLine)

        body += "{2:>}{0:*>39}{1:>}".format('*', POSEquipment.TicketPrinter.escNewLine,
                                            POSEquipment.TicketPrinter.escPrintNormal) #lijntje

        #detail
        for line in self.GetTicketLines():
            if (line[6]==0)or(line[6]==1)or(line[6]==3): #kortingen hoeven niet op de bon
                indent = ""
                if (line[3] == 9999) or line[2]: #is generiek of optie
                    indent = "     "

                body += "{2}{0[0]:>2}{1:>}".format(line, POSEquipment.TicketPrinter.escNewLine, indent)

        POSEquipment.TicketPrinter.PrintKitchenBill(body, self.eatInOut)

        self.KitchenPrinted = True


    def GetTotalAmt(self, allTickets = False):
        if not allTickets:
            #only for current ticket!
            ticketLines = self.GetTicketLines()
            total = 0

            for line in ticketLines:
                total = total + line[1]

            return total
        else:
            cur = self.conn.cursor()
            cur.execute("select SUM(price) from ticketLine where paid<>0 and isCancelled=0")
            line = cur.fetchone()
            if line[0]:
                return line[0]
            else:
                return 0
                

    def GetLoyaltyCardPoints(self):
        totalAmt = self.GetTotalAmt()

        return (totalAmt - (totalAmt % ini.LOYALTYCARD_EURO_PER_POINT)) / ini.LOYALTYCARD_EURO_PER_POINT


    def GetFirstOrderDate(self):
        cur = self.conn.cursor()
        cur.execute("select MIN(dateRegistered) from ticketLine")
        line = cur.fetchone()
        if line:
            return ParseDateTimeUTC(line[0])
        else:
            return 0


    def GetLastOrderDate(self):
        cur = self.conn.cursor()
        cur.execute("select MAX(dateRegistered) from ticketLine")
        line = cur.fetchone()
        if line:
            return ParseDateTimeUTC(line[0])
        else:
            return 0


    def GetPaymentTotal(self, paymentType):
        cur = self.conn.cursor()
        cur.execute("select SUM(price) from ticketLine where paid=? and isCancelled=0", (paymentType,))
        line = cur.fetchone()
        if line[0]:
            return line[0]
        else:
            return 0


    def GetVATLines(self):
        cur = self.conn.cursor()
        cur.execute("select * from vatCode")
        lines = cur.fetchall()

        VATLines = []

        for line in lines:
            vatPct = line[2]
            cur.execute("select SUM(price) from ticketLine where vatCode=? and paid<>0 and isCancelled=0", (line[0],))
            totAmt = cur.fetchone()

            if totAmt[0]:
                tot = totAmt[0]
                evat = tot / (1 + (vatPct / 100))
                vat = tot - evat
            else:
                vat = 0
                evat = 0
                tot = 0

            VATLines.append([vatPct, evat, vat, tot, line[0]])

        return VATLines

    def GetItemTotals(self):
        outputLines = []

        cur = self.conn.cursor()

        cur.execute("select * from product_group")
        groups = cur.fetchall()

        for group in groups:
            cur.execute("""SELECT
                              vwItemTotals.qty,
                              vwItemTotals.productId,
                              vwItemTotals.productName,
                              vwItemTotals.total,
                              vwItemTotals.productGroupName,
                              vwItemTotals.groupId
                            FROM
                              vwItemTotals
                            WHERE
                              vwItemTotals.groupId=?""", (group[0],))
            lines = cur.fetchall()
            outputLines.append([group[0], group[1], lines])

        return outputLines

    def ClearAll(self):
        cur = self.conn.cursor()

        cur.execute("delete from ticketLine")

        self.conn.commit()

    def GetOffers(self):
        cur = self.conn.cursor()

        offers = {}

        for dtype in discountTypes:
            if dtype != 'none':
                if dtype == 'Commerciele korting':

                    cur.execute("""SELECT
                                      ticketLine.entryNo,
                                      ticketLine.ticketNo,
                                      ticketLine.productId,
                                      ticketLine.productName,
                                      sum(ticketLine.price) AS price,
                                      ticketLine.paid,
                                      ticketLine.eatInOut,
                                      ticketLine.isOption,
                                      ticketLine.dateRegistered,
                                      ticketLine.vatCode,
                                      ticketLine.customerId,
                                      ticketLine.discountType,
                                      ticketLine.isCancelled,
                                      ticketLine.quantity
                                    FROM
                                      ticketLine
                                    WHERE ticketLine.discountType=? and paid <> 0 and isCancelled=0
                                    GROUP BY
                                      ticketLine.productId""", (discountTypes[dtype],))
                else:
                    cur.execute("select * from ticketLine where discountType=? and isCancelled=0 and paid<>0", (discountTypes[dtype],))
                offers[dtype] = cur.fetchall()

        return offers

    def GetMaxTicketNo(self):
        
        cur = self.conn.cursor()

        cur.execute('select max(ticketNo) from ticketLine')

        res = cur.fetchone()
        
        if res[0]:
            return res[0]
        else:
            return 0
        

            

