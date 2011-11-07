from DataModel.Product import Product
from DataModel.ScreenGroup import ScreenGroup
import ini
import sqlite3

__author__ = 'dennis'


class ProductScreen:
    def __init__(self, entryNo=0):
        self._conn = sqlite3.connect(ini.DB_NAME)
        
        self.entryNo = entryNo
        self.screenCategoryId = 0
        self.productId = 0
        self.buttonNo = 0
        self.bgColor = ""
        self.productName = ""
        
    def save(self):
        cur = self._conn.cursor()
        ps = ProductScreen()
        ps.GetProductNoOnButton(self.buttonNo, self.screenCategoryId)
        
        if ps.entryNo: #this means an entry was found for this button/screen
            cur.execute("update product_screen set screenCategoryId=?, productId=?,buttonNo=?,bgColor=?,productName=? where entryNo=?",
                        (self.screenCategoryId, self.productId, self.buttonNo, self.bgColor, self.productName, ps.entryNo))
            self.entryNo = ps.entryNo
            
        else:
            cur.execute("insert into product_screen (screenCategoryId, productId, buttonNo, bgColor, productName) values (?,?,?,?,?)",
                        (self.screenCategoryId, self.productId, self.buttonNo, self.bgColor, self.productName))
    
            cur.execute("SELECT last_insert_rowid()")
            self.entryNo = cur.fetchone()[0]
            
        self._conn.commit()
    
    def deleteByProductId(self):
        cur=self._conn.cursor()
        cur.execute("delete from product_screen where productId=?",(self.productId,))
        self._conn.commit()
    
    def GetProductsForScreen(self, screenCategory):
        cur = self._conn.cursor()

        sg = ScreenGroup()
        sg.fetchOne(screenOrder=screenCategory)

        if sg.id:
            cur.execute("select * from product_screen where screenCategoryId=? order by buttonNo ASC", (sg.id,))
            return cur.fetchall()
        else:
            return None

    def GetProductNoOnButton(self, buttonNo, screenCategory):
        cur = self._conn.cursor()

        sg = ScreenGroup()
        sg.fetchOne(screenOrder=screenCategory)
        
        cur.execute("select * from product_screen where screenCategoryId=? and buttonNo=?",
                (sg.id, buttonNo))
        result = cur.fetchone()
        
        if result:
            self.entryNo = result[0]
            self.screenCategoryId = result[1]
            self.productId = result[2]
            self.buttonNo = result[3]
            self.bgColor = result[4]
            self.productName = result[5]
            
        return self.productId

    def GetCaption(self, buttonNo, screenCategory):
        cur = self._conn.cursor()

        sg = ScreenGroup()
        sg.fetchOne(screenOrder=screenCategory)

        cur.execute("select productName from product_screen where productId=? and screenCategoryId=? and buttonNo=?",
                (9999, sg.id, buttonNo))
        result = cur.fetchone()
        return result[0]

    def GetOptionProductNoOnButton(self, buttonNo, productId):
        cur = self._conn.cursor()
        cur.execute("select optionProductId from productOption where productId=? and buttonNo=?",
                (productId, buttonNo))
        result = cur.fetchone()
        return result[0]

    def GetOptionsForProduct(self, productNo):
        cur = self._conn.cursor()
        cur.execute("select * from productOption where productId = ?", (productNo,))
        return cur.fetchall()

    def GetCaptionForOption(self, parentProductId, buttonNo):
        cur = self._conn.cursor()
        cur.execute("select productName from productOption where productId=? and buttonNo=?",
                (parentProductId, buttonNo))
        result = cur.fetchone()
        return result[0]

    def GetNextScreenForOption(self, parentProductId, optionProductId, buttonNo):
        cur = self._conn.cursor()
        cur.execute("select nextScreenGroup from productOption where productId=? and optionProductId = ? and buttonNo=?",
                (parentProductId, optionProductId, buttonNo))
        result = cur.fetchone()
        return result[0]
    
    
