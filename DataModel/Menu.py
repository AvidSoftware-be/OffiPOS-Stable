import sqlite3
import ini

__author__ = 'dennis'


class ProductMenu():
    def __init__(self, productId):
        conn = sqlite3.connect(ini.DB_NAME, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        conn.text_factory = str
        cur = conn.cursor()
        cur.execute('select * from menuComponent where productId=?',(productId,))

        self.menuComponents = cur.fetchall()