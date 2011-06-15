from DataModel.Product import Product

__author__ = 'dennis'

import sqlite3
import ini

class ProductScreen:
    def GetProductsForScreen(self, screenCategory):
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()

        cur.execute("select id from screen_group where screenOrder=?",(screenCategory,))
        res = cur.fetchone()
        
        cur.execute("select * from product_screen where screenCategoryId=? order by buttonNo ASC", (res[0],))
        return cur.fetchall()

    def GetProductNoOnButton(self, buttonNo, screenCategory):
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        cur.execute("select productId from product_screen where screenCategoryId=? and buttonNo=?",
                    (screenCategory, buttonNo))
        result = cur.fetchone()
        return result[0]

    def GetOptionProductNoOnButton(self, buttonNo, productId):
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        cur.execute("select optionProductId from productOption where productId=? and buttonNo=?",
                    (productId, buttonNo))
        result = cur.fetchone()
        return result[0]

    def GetOptionsForProduct(self, productNo):
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        cur.execute("select * from productOption where productId = ?", (productNo,))
        return cur.fetchall()