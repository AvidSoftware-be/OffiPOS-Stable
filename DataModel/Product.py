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

    #    def save(self):
    #        conn = sqlite3.connect(ini.DB_NAME)
    #        val = (self.id, self.name, self.price, self.group, self.vatCodeIn, self.vatCodeOut)
    #
    #        cur = conn.cursor()
    #
    #        cur.execute("insert into product values (?,?,?,?,?,?)", val)
    #
    #        conn.commit()

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

