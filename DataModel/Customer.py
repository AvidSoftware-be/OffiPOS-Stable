from datetime import date
import sqlite3
import ini

__author__ = 'dennis'

class Customer:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.firstName = ""
        self.address = ""
        self.postalCode = ""
        self.city = ""
        self.telephone = ""
        self.birthDate = ""
        self.emailAddress = ""
        self.loyaltyCardNo = ""
        self.loyaltyPoints = 0
        self.loyaltyDiscount = 0
        self.loyaltyDiscountDate = date.today()

    def GetCustomerFromLoyaltyCard(self, loyaltyCardNo):
        conn = sqlite3.connect(ini.DB_NAME, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        cur = conn.cursor()
        cur.execute('select no, name,firstName,address,postalCode,city,telephone,birthDate,emailAddress,loyaltyCardNo,loyaltyPoints,loyaltyDiscount,loyaltyDiscountDate as "loyaltyDiscountDate [date]" from customer where loyaltyCardNo=?', (loyaltyCardNo,))
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

    def AddLoyaltyPoints(self, ticketPoints):
        newtotal = self.loyaltyPoints + ticketPoints

        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        cur.execute("update customer set loyaltyPoints = ? where loyaltyCardNo=?",
                (newtotal, self.loyaltyCardNo, ))

        bonus = (newtotal - (newtotal % 10)) / 10
        cur.execute("update customer set loyaltyDiscount = ?, loyaltyDiscountDate = ? where loyaltyCardNo=?",
                    (2.5 * bonus, date.today(), self.loyaltyCardNo, ))

        conn.commit()
