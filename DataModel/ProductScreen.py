__author__ = 'dennis'

import sqlite3
import ini

class ProductScreen:
    def GetProductsForScreen(self,screenCategory):
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        cur.execute("select * from product_screen where screenCategoryId=? order by buttonNo ASC",(screenCategory,))
        return cur.fetchall()