import DataModel
from DataModel.Ticket import Ticket

__author__ = 'dennis'

import GeneratedGui

# Implementing MainFrameBase
from Gui import *

class PaymentFrame(GeneratedGui.PaymentFrameBase):
    def __init__( self, parent ):
        GeneratedGui.PaymentFrameBase.__init__(self, parent)

        self.ticket = Ticket()
        self.paymentMethod = 0
        self.cancelled = False

    def SetTicket(self, ticket):
        self.ticket = ticket

        self.txtTotalToPay.Value = "%.2f" % self.ticket.GetTotalAmt()

    def btnOneOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "1"

    def btnTwoOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "2"

    def btnThreeOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "3"

    def btnFourOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "4"

    def btnFiveOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "5"

    def btnSixOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "6"

    def btnSevenOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "7"

    def btnEightOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "8"

    def btnNineOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "9"

    def btnZeroOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "0"

    def btnDotOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "."

    def btnCashOnButtonClick( self, event ):
        payed = float(self.txtPayed.Value)
        toReturn = float(self.txtTotalToPay.Value) - payed

        self.txtReturn.Value = "%.2f" % toReturn

        self.paymentMethod = DataModel.Ticket.paymentMethodCash

    def btnAtosOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtTotalToPay.Value

        payed = float(self.txtPayed.Value)
        toReturn = float(self.txtTotalToPay.Value) - payed

        self.txtReturn.Value = "%.2f" % toReturn

        self.paymentMethod = DataModel.Ticket.paymentMethodAtos

        self.ticket.PayTicket(self.paymentMethod, payed, toReturn)

        self.Close()

    def btnEnterOnButtonClick( self, event ):
        payed = float(self.txtPayed.Value)
        toReturn = float(self.txtTotalToPay.Value) - payed

        self.ticket.PayTicket(self.paymentMethod, payed, toReturn)

        self.Close()

    def btnClrOnButtonClick( self, event ):
        self.txtReturn.Value = ""
        self.txtPayed.Value = ""

    def btnClsOnButtonClick( self, event ):
        self.cancelled = true



  