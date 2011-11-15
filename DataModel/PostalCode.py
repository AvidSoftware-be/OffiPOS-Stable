
from DataModel.DMBase import DMBase
__author__ = 'dennis'

class PostalCode(DMBase):
    def __init__(self):

        self.Code = 0
        self.Name = ""

    def GetFromCode(self, code):
        cur = self._conn.cursor()
        cur.execute("select * from postalCode where Code=?",(code,))

        res = cur.fetchall()

        return res
