import wx
#===============================================================================
# from DataModel.ProductScreen import ProductScreen
# from DataModel.ScreenGroup import ScreenGroup
# from DataModel.Ticket import Ticket, priceModes, discountTypes
# from DataModel.Product import  Product
#===============================================================================
import GeneratedGui

class POSProgram(GeneratedGui.MainFrameBase):

    def __init__( self, parent ):
        GeneratedGui.MainFrameBase.__init__(self, parent)
        self.pnlFuncties.Hide()
        self.pnlRekening.Hide()