from DataModel.DMBase import DMBase

__author__ = 'dennis'


class ProductMenu(DMBase):
    def __init__(self, productId):
        DMBase.__init__(self)
        cur = self._conn.cursor()
        cur.execute('select * from menuComponent where productId=?',(productId,))

        self.menuComponents = cur.fetchall()