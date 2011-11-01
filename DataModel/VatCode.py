import sqlite3
import ini

class VatCode:
    def fetchall(self):
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        cur.execute("select * from vatcode")
        return cur.fetchall()