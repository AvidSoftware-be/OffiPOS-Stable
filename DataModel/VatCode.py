import sqlite3
import ini
from DataModel.DMBase import DMBase

class VatCode(DMBase):
    def __init__(self):
        DMBase.__init__(self)
        
    def fetchall(self):
        cur = self._conn.cursor()
        cur.execute("select * from vatcode")
        return cur.fetchall()