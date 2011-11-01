__author__ = 'dennis'

import sqlite3
import ini

class Product:
    def __init__(self, id):
        self.id = id
        self.name = ""
        self.price = 0
        self.discountIfOption = 0
        self.group = 0
        self.vatCodeIn = 0
        self.vatCodeOut = 0
        self.askForPrice = 0
        self.screenName = ""
        self.treatAsOption = 0

    def save(self):
        conn = sqlite3.connect(ini.DB_NAME)

        cur = conn.cursor()
        
        if not self.id:
            cur.execute("insert into product (name,price,groupId,vatCodeIn,vatCodeOut,askForPrice,screenName,treatAsOption,discountIfOption) values (?,?,?,?,?,?,?,?,?)", (self.name,
               self.price,
               self.group,
               self.vatCodeIn,
               self.vatCodeOut,
               self.askForPrice,
               self.screenName,
               self.treatAsOption,
               self.discountIfOption))
            
            cur.execute("SELECT last_insert_rowid()")
            self.id = cur.fetchone()[0]
        else:
            cur.execute("update product set name=?,price=?,groupId=?,vatCodeIn=?,vatCodeOut=?,askForPrice=?,screenName=?,treatAsOption=?,discountIfOption=? where id=?", (self.name,
               self.price,
               self.group,
               self.vatCodeIn,
               self.vatCodeOut,
               self.askForPrice,
               self.screenName,
               self.treatAsOption,
               self.discountIfOption,
               self.id))

        conn.commit()

    def fetchall(self):
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        cur.execute("select * from product")
        return cur.fetchall()

    def fill(self):
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        cur.execute("select * from product where id=?", (self.id,))
        prod = cur.fetchone()

        if prod:
            self.id = prod[0]
            self.name = prod[1]
            self.price = prod[2]
            self.discountIfOption = prod[3]
            self.group = prod[4]
            self.vatCodeIn = prod[5]
            self.vatCodeOut = prod[6]
            self.askForPrice = prod[7]
            self.screenName = prod[8]
            self.treatAsOption = prod[9]

