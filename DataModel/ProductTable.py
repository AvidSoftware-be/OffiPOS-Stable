from DataModel.Product import Product
import wx

class ProductTable(wx.grid.PyGridTableBase):
    def __init__(self):
        wx.grid.PyGridTableBase.__init__(self)
        self.colLabels = ["Nr.","Naam","Prijs"]
        
        self.productLines = Product(0).fetchall()
        
    def GetNumberRows(self):
        return len(self.productLines)

    def GetNumberCols(self):
        return len(self.colLabels)

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return self.productLines[row][col]

    def SetValue(self, row, col, value):
        pass

    def GetColLabelValue(self, col):
        return self.colLabels[col]

    def GetRowLabelValue(self, row):
        return str(row)
        
        