__author__ = 'dennis'

import sqlite3
import ini

class ScreenGroup:
    def __init__(self, id=0, name="", screenOrder=0):
        self.id = id
        self.name = name
        self.screenOrder = screenOrder
    
    def fetchOne(self, id=0, screenOrder=0):
        
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        
        if screenOrder:
            cur.execute("select * from screen_group where screenOrder=?", (screenOrder,))
        elif id:
            cur.execute("select * from screen_group where id=?", (id,))
        else:
            return
            
        res = cur.fetchone()
            
        self.id = res[0]
        self.name = res[1]
        self.screenOrder = res[2]
    
    def fetchall(self):
        conn = sqlite3.connect(ini.DB_NAME)
        cur = conn.cursor()
        cur.execute("select * from screen_group order by screenOrder ASC")
        return cur.fetchall()
