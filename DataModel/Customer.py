from DataModel.DMBase import DMBase
from datetime import date, timedelta
from wx.grid import Grid
import ini
import sqlite3
import wx

__author__ = 'dennis'

class Customer(DMBase):
    def __init__(self):
        DMBase.__init__(self)
        self.id = 0
        self.name = ""
        self.firstName = ""
        self.address = ""
        self.postalCode = ""
        self.city = ""
        self.telephone = ""
        self.birthDate = ini.MINDATE
        self.emailAddress = ""
        self.loyaltyCardNo = ""
        self.loyaltyPoints = 0
        self.loyaltyDiscount = 0
        self.loyaltyDiscountDate = ini.MINDATE
        self.dateRegistered = ini.MINDATE
        self.remarks = [] ##TODO: opvullen en wegschrijven in customer_remarks tabel

    def GetCustomerFromLoyaltyCard(self, loyaltyCardNo):
        if loyaltyCardNo == "":
            return

        cur = self._conn.cursor()
        cur.execute(
            'select no, name,firstName,address,postalCode,city,telephone,birthDate,emailAddress,loyaltyCardNo,loyaltyPoints,loyaltyDiscount,loyaltyDiscountDate as "loyaltyDiscountDate [date]" from customer where loyaltyCardNo=?'
            , (loyaltyCardNo,))
        cust = cur.fetchone()

        if cust:
            self.id = cust[0]
            self.name = cust[1]
            self.firstName = cust[2]
            self.address = cust[3]
            self.postalCode = cust[4]
            self.city = cust[5]
            self.telephone = cust[6]
            self.birthDate = cust[7]
            self.emailAddress = cust[8]
            self.loyaltyCardNo = cust[9]
            self.loyaltyPoints = cust[10]
            self.loyaltyDiscount = cust[11]
            self.loyaltyDiscountDate = cust[12]
        else:
            self.loyaltyCardNo = loyaltyCardNo
            self.loyaltyPoints = ini.LOYALTYCARD_STARTING_POINTS
            self.Save()

    def AddLoyaltyPoints(self, ticketPoints):
        if not self.id:
            return
        
        if self.CanPayDiscount():
            self.PayLoyaltyPoints()
        else:
            if self.loyaltyPoints:
                newTotal = self.loyaltyPoints + ticketPoints
            else:
                newTotal = ticketPoints

            cur = self._conn.cursor()
            cur.execute("update customer set loyaltyPoints = ? where loyaltyCardNo=?",
                    (newTotal, self.loyaltyCardNo, ))

#            cur.execute("insert into loyaltyCardDetails (customerId, ticketPoints) values(?,?)",
#                    (self.id, ticketPoints))

            bonus = (newTotal - (newTotal % ini.LOYALTYCARD_POINTS_FOR_BONUS)) / ini.LOYALTYCARD_POINTS_FOR_BONUS
            cur.execute("update customer set loyaltyDiscount = ?, loyaltyDiscountDate = ? where loyaltyCardNo=?",
                    (ini.LOYALTYCARD_BONUS_AMOUNT * bonus, date.today(), self.loyaltyCardNo, ))

            self._conn.commit()

            self.loyaltyPoints = newTotal

    def GetPointsToDeductOnBonus(self):
        pointsToDeduct = (self.loyaltyDiscount / ini.LOYALTYCARD_BONUS_AMOUNT) * ini.LOYALTYCARD_POINTS_FOR_BONUS
        return pointsToDeduct

    def PayLoyaltyPoints(self):
        cur = self._conn.cursor()

        pointsToDeduct = self.GetPointsToDeductOnBonus()

        remainingPoints = self.loyaltyPoints - pointsToDeduct

        cur.execute("update customer set loyaltyPoints = ?, loyaltyDiscount = ? where loyaltyCardNo=?",
                (remainingPoints, 0, self.loyaltyCardNo, ))

        cur.execute("insert into loyaltyCardDetails (customerId, ticketPoints) values(?,?)",
                (self.id, pointsToDeduct * -1))

        self._conn.commit()

        self.loyaltyPoints = remainingPoints

    def CanPayDiscount(self):
        return self.loyaltyDiscount and (date.today() - self.loyaltyDiscountDate >= timedelta(days=1))

    def GetCustomerTable(self, sortingCol):
        return CustomerTable(sortingCol)

    def GetAll(self, sortingColumnName):
        cur = self._conn.cursor()
        cur.execute(
            'select no, firstName,name,address,postalCode,city,telephone,birthDate,emailAddress,loyaltyCardNo,loyaltyPoints from customer order by ' + sortingColumnName)
        customers = cur.fetchall()
        return customers

    def FillFromId(self, customerId):
        cur = self._conn.cursor()
        cur.execute(
            """select no,
                      name,
                      firstName,
                      address,
                      postalCode,
                      city,
                      telephone,
                      birthDate as "birthDate [date]",
                      emailAddress,
                      loyaltyCardNo,
                      loyaltyPoints,
                      loyaltyDiscount,
                      loyaltyDiscountDate as "loyaltyDiscountDate [date]",
                      dateRegistered
                from customer where no=?"""
            , (customerId,))
        cust = cur.fetchone()

        if cust:
            self.id = cust[0]
            self.name = cust[1]
            self.firstName = cust[2]
            self.address = cust[3]
            self.postalCode = cust[4]
            self.city = cust[5]
            self.telephone = cust[6]
            self.birthDate = cust[7]
            self.emailAddress = cust[8]
            self.loyaltyCardNo = cust[9]
            self.loyaltyPoints = cust[10]
            self.loyaltyDiscount = cust[11]
            self.loyaltyDiscountDate = cust[12]
            self.dateRegistered = cust[13]

    def Save(self):
        cur = self._conn.cursor()

        if not self.id:
            #invoegen
            cur.execute(
                """insert into customer (
                      name,
                      firstName,
                      address,
                      postalCode,
                      city,
                      telephone,
                      birthDate,
                      emailAddress,
                      loyaltyCardNo,
                      loyaltyPoints,
                      loyaltyDiscount,
                      loyaltyDiscountDate,
                      dateRegistered)
                                    values
                                        (?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                , (self.name,
                   self.firstName,
                   self.address,
                   self.postalCode,
                   self.city,
                   self.telephone,
                   self.birthDate,
                   self.emailAddress,
                   self.loyaltyCardNo,
                   self.loyaltyPoints,
                   self.loyaltyDiscount,
                   self.loyaltyDiscountDate,
                   self.dateRegistered))

            cur.execute("SELECT last_insert_rowid()")
            self.id = cur.fetchone()[0]
        else:
            #update
            cur.execute(
                """update customer set firstName = ?,
                                        name = ?,
                                        address = ?,
                                        postalCode = ?,
                                        city = ?,
                                        telephone = ?,
                                        birthDate = ?,
                                        emailAddress = ?,
                                        loyaltyCardNo=?,
                                         dateRegistered=?
                                         where no=?"""
                ,
                    (self.firstName,
                     self.name,
                     self.address,
                     self.postalCode,
                     self.city,
                     self.telephone,
                     self.birthDate,
                     self.emailAddress,
                     self.loyaltyCardNo,
                     self.dateRegistered,
                     self.id))

        self._conn.commit()

    def Delete(self):
        cur = self._conn.cursor()

        #invoegen
        cur.execute("delete from customer where no=?", (self.id,))

        self._conn.commit()

    def UpdateLoyaltyCardNo(self, newLoyaltyCardNo):
        cur = self._conn.cursor()

        cur.execute("update customer set loyaltyCardNo = ? where no = ?", (newLoyaltyCardNo, self.id))

        self._conn.commit()

        self.loyaltyCardNo = newLoyaltyCardNo


class CustomerTable(wx.grid.PyGridTableBase):
    def __init__(self, sortCol):
        wx.grid.PyGridTableBase.__init__(self)
        self.colLabels = ["Nr.", "Voornaam", "Naam", "Adres", "Postcode", "Gemeente", "Telefoon", "Geboortedatum",
                          "Emailadres", "Klantkaart", "Punten"]
        self.recordLabels = ["no", "firstName", "name", "address", "postalCode", "city", "telephone", "birthDate",
                             "emailAddress", "loyaltyCardNo", "loyaltyPoints"]

        self.customerLines = Customer().GetAll(self.recordLabels[sortCol])

    def GetNumberRows(self):
        return len(self.customerLines)

    def GetNumberCols(self):
        return len(self.colLabels)

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return self.customerLines[row][col]

    def SetValue(self, row, col, value):
        pass

    def GetColLabelValue(self, col):
        return self.colLabels[col]

    def GetRowLabelValue(self, row):
        return self.rowLabels[row]

