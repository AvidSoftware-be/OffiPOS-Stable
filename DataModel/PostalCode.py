
import sqlite3
import ini

__author__ = 'dennis'

class PostalCode:
    def __init__(self):
        self.conn = sqlite3.connect(ini.DB_NAME)

        self.Code = 0
        self.Name = ""

    def GetFromCode(self, code):
        cur = self.conn.cursor()
        cur.execute("select * from postalCode where Code=?",(code,))

        res = cur.fetchall()

        return res
