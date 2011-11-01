import sqlite3
import ini

class ProductGroup:
    def fetchall(self):
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        cur.execute("select * from product_group")
        return cur.fetchall()