from DataModel.ProductTable import ProductTable
from Gui import GeneratedGui
import wx

class dlgSelectProduct(GeneratedGui.dlgSelectProductBase):
    def __init__(self, parent):
        GeneratedGui.dlgSelectProductBase.__init__(self, parent)

        self.UpdateForm()
        
        self.m_grid3.AutoSizeColumns(False)
        self.Fit()
        
        self.UpdateForm()
        
    def btnSelectOnButtonClick(self, event):
        row = self.m_grid3.GetGridCursorRow()
        no = int(self.m_grid3.GetCellValue(row, 0))
        self.EndModal(no)
    
    def UpdateForm(self):

        grid = self.m_grid3
        table = ProductTable()
        grid.SetTable(table)
        rows = table.GetNumberRows()
        grid.MakeCellVisible(rows - 1, 1)
        grid.EnableEditing(False)
        grid.SetSelectionMode(wx.grid.Grid.SelectRows)
        grid.SetRowLabelSize(0)
        
        #self.RestoreColSizes()
