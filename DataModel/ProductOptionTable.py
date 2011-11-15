from DataModel.ProductScreen import ProductScreen
import wx

class ProductOptionTable(wx.grid.PyGridTableBase):
    def __init__(self, parentProductId):
        wx.grid.PyGridTableBase.__init__(self)
        self.colLabels = ["OptieNr.", "Naam", "Knop"]
        
        self.productOptions = ProductScreen().GetOptionsForProduct(parentProductId)
        
    def GetNumberRows(self):
        return len(self.productOptions)

    def GetNumberCols(self):
        return len(self.colLabels)

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        if col == 0:
            return self.productOptions[row][2]
        elif col == 1:
            return self.productOptions[row][7]
        elif col == 2:
            return self.productOptions[row][3]

    def SetValue(self, row, col, value):
        pass

    def GetColLabelValue(self, col):
        return self.colLabels[col]

    def GetRowLabelValue(self, row):
        return str(row)
        
        
