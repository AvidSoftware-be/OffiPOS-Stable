import GeneratedGui
import wx
from Gui.dlgCustomerEdit import dlgCustomerEdit

__author__ = 'dennis'

class frmKlantBeheer(GeneratedGui.frmKlantBeheerBase):
    def __init__( self, parent ):
        GeneratedGui.frmKlantBeheerBase.__init__(self, parent)

    def btnNieuwOnButtonClick( self, event ):
        dlgBeheer = dlgCustomerEdit(self)
        dlgBeheer.ShowModal()
