from wx._misc import MessageBox
from wxPython._core import wxSAVE, wxOVERWRITE_PROMPT, wxID_OK
from wxPython._windows import wxFileDialog
from DataModel.Ticket import Ticket
import DataModel.VATManipulations
from Gui.frmKlantBeheer import frmKlantBeheer
import utils.BackupTransactions

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

        MessageBox(u"Totaal: {0:>10.2f}\u20AC".format(total))

    def btnKlantKaartBeheerOnButtonClick( self, event ):
        kb = frmKlantBeheer(self)

        kb.Show()

    def btnBackTransOnButtonClick( self, event ):
        destinationFile = ""

        # Create a save file dialog
        dialog = wxFileDialog ( None, style = wxSAVE | wxOVERWRITE_PROMPT )

        # Show the dialog and get user input
        if dialog.ShowModal() == wxID_OK:
           destinationFile = dialog.GetPath()

        # Destroy the dialog

        dialog.Destroy()

        utils.BackupTransactions.DoBackup(destinationFile)

  