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

    def GetCustomerFromLoyaltyCard(self, loyaltyCardNo):
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        cur.execute("select * from customer where loyaltyCardNo=?", (loyaltyCardNo,))
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