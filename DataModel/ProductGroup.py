from DataModel.DMBase import DMBase

class ProductGroup(DMBase):
    def __init__(self):
        DMBase.__init__(self)
        
    def fetchall(self):

        cur = self._conn.cursor()
        cur.execute("select * from product_group")
        return cur.fetchall()