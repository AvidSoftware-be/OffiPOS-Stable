from DataModel.Customer import Customer
import GeneratedGui
import wx
from Gui.dlgCustomerEdit import dlgCustomerEdit

__author__ = 'dennis'

class frmKlantBeheer(GeneratedGui.frmKlantBeheerBase):
    def UpdateForm(self):
        grid = self.grdCustomer
        table = Customer().GetCustomerTable()
        grid.SetTable(table)
        rows = table.GetNumberRows()
        grid.MakeCellVisible(rows - 1, 1)
        grid.EnableEditing(False)
        grid.SetSelectionMode(wx.grid.Grid.SelectRows)
        grid.SetRowLabelSize(0)
        grid.AutoSizeColumns()
        self.Fit()

    def __init__( self, parent ):
        GeneratedGui.frmKlantBeheerBase.__init__(self, parent)

        self.UpdateForm()


    def btnNieuwOnButtonClick( self, event ):
        dlgBeheer = dlgCustomerEdit(self)
        dlgBeheer.ShowModal()

    def btnBewerkOnButtonClick( self, event ):

        row = self.grdCustomer.GetGridCursorRow()
        id = int(self.grdCustomer.GetCellValue(row,0))

        dlgBeheer = dlgCustomerEdit(self)
        dlgBeheer.SetCustomer(id)
        dlgBeheer.ShowModal()

        self.UpdateForm()


