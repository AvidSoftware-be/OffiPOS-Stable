import wx
from DataModel.Ticket import Ticket
import DataModel.VATManipulations

__author__ = 'dennis'

import GeneratedGui

class AdminDialog(GeneratedGui.AdminDialogBase):
    def __init__( self, parent ):
        GeneratedGui.AdminDialogBase.__init__(self, parent)

    def btnKasAfsluitenOnButtonClick( self, event ):
        DataModel.VATManipulations.DoEndOfDay(True)

    def btnKasAfsluitenTestOnButtonClick( self, event ):
        DataModel.VATManipulations.DoEndOfDay(False)

    def btnTotalOnScreenOnButtonClick( self, event ):
        total = 0
        try:
            total = Ticket().GetPaymentTotal(DataModel.Ticket.paymentMethods['Cash'])
            total += Ticket().GetPaymentTotal(DataModel.Ticket.paymentMethods['Atos'])
        except:
            if not total:
                total = 0

        wx.MessageBox(u"Totaal: {0:>10.2f}\u20AC".format(total))

  