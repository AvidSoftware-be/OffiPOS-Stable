import GeneratedGui
import wx

__author__ = 'dennis'

class dlgAskForPrice(GeneratedGui.dlgAskForPriceBase):
    def __init__( self, parent ):
        GeneratedGui.dlgAskForPriceBase.__init__(self, parent)
        self.Value = 0

    def btnOneOnButtonClick( self, event ):
        self.txtPrice.Value = self.txtPrice.Value + "1"

    def btnTwoOnButtonClick( self, event ):
        self.txtPrice.Value = self.txtPrice.Value + "2"

    def btnThreeOnButtonClick( self, event ):
        self.txtPrice.Value = self.txtPrice.Value + "3"

    def btnFourOnButtonClick( self, event ):
        self.txtPrice.Value = self.txtPrice.Value + "4"

    def btnFiveOnButtonClick( self, event ):
        self.txtPrice.Value = self.txtPrice.Value + "5"

    def btnSixOnButtonClick( self, event ):
        self.txtPrice.Value = self.txtPrice.Value + "6"

    def btnSevenOnButtonClick( self, event ):
        self.txtPrice.Value = self.txtPrice.Value + "7"

    def btnEightOnButtonClick( self, event ):
        self.txtPrice.Value = self.txtPrice.Value + "8"

    def btnNineOnButtonClick( self, event ):
        self.txtPrice.Value = self.txtPrice.Value + "9"

    def btnZeroOnButtonClick( self, event ):
        self.txtPrice.Value = self.txtPrice.Value + "0"

    def btnDotOnButtonClick( self, event ):
        self.txtPrice.Value = self.txtPrice.Value + "."

    def btnEnterOnButtonClick( self, event ):
        self.Value = float(self.txtPrice.Value)
        self.Close()

    def btnClearOnButtonClick( self, event ):
        self.txtPrice.Value = ""
