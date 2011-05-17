__author__ = 'dennis'

import sqlite3
import ini

class ScreenGroup:
    def fetchall(self):
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        cur.execute("select * from screen_group order by screenOrder ASC")
        return cur.fetchall()