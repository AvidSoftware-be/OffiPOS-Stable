__author__ = 'dennis'

import sqlite3
import ini

class Product:
    def __init__(self, id, price, name, group, vatCodeIn, vatCodeOut):
        self.price = price
        self.id = id
        self.name = name
        self.group = group
        self.vatCodeIn = vatCodeIn
        self.vatCodeOut = vatCodeOut

    def save(self):
        conn = sqlite3.connect(ini.DB_NAME)
        val = (self.id, self.name, self.price, self.group, self.vatCodeIn, self.vatCodeOut)

        cur = conn.cursor()

        cur.execute("insert into product values (?,?,?,?,?,?)", val)

        conn.commit()

    def fetchall(self):
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        cur.execute("select * from product")
        return cur.fetchall()

    def fetch(self):
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        cur.execute("select * from product where id=?", (self.id,))
        return cur.fetchone()


