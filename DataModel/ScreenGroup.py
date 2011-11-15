from DataModel.DMBase import DMBase
__author__ = 'dennis'

class ScreenGroup(DMBase):
    def __init__(self, id=0, name="", screenOrder=0):
        DMBase.__init__(self)
        
        self.id = id
        self.name = name
        self.screenOrder = screenOrder
    
    def fetchOne(self, id=0, screenOrder=0):
        cur = self._conn.cursor()
        
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

        cur = self._conn.cursor()
        cur.execute("select * from screen_group order by screenOrder ASC")
        return cur.fetchall()
