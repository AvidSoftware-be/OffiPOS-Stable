from wx._misc import MessageBox
from wxPython._core import wxSAVE, wxOVERWRITE_PROMPT, wxID_OK, wxOPEN
from wxPython._windows import wxFileDialog
from Client.JSONClient import Proxy
from DataModel.Ticket import Ticket
import DataModel.VATManipulations
from Gui.frmKlantBeheer import frmKlantBeheer
import ini
from utils.BackupDatabase import FILETYPES
import utils

import pprint

__author__ = 'dennis'

import GeneratedGui

class AdminDialog(GeneratedGui.AdminDialogBase):
    def __init__( self, parent ):
        GeneratedGui.AdminDialogBase.__init__(self, parent)
        self.JSONProxy = Proxy(ini.SERVICEURL+'/json/')

    def btnKasAfsluitenOnButtonClick( self, event ):
        DataModel.VATManipulations.DoEndOfDay(True)

    def btnKasAfsluitenTestOnButtonClick( self, event ):
        DataModel.VATManipulations.DoEndOfDay(False)

    '''
    def btnTotalOnScreenOnButtonClick( self, event ):
        total = self.JSONProxy._call('getDayTotal')
        if total["error"]:
            MessageBox(total["error"]["message"])
        else:
            MessageBox(u"Totaal: {0:>10.2f}\u20AC".format(total["result"]))

    def btnArtTotSchermOnButtonClick( self, event ):
        itemTotals = self.JSONProxy._call('getItemTotals')

        for totalLine in itemTotals:
            for itemLine in totalLine:
                pass

        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint()

    def btnArtikelTotalenOnButtonClick( self, event ):
        DataModel.VATManipulations.PrintItemTotals()
    '''

    def btnKlantKaartBeheerOnButtonClick( self, event ):
        kb = frmKlantBeheer(self)
        
        kb.Center()

        kb.ShowModal()

    def btnBackTransOnButtonClick( self, event ):
        destinationFile = ""
        sourceFile = ""

        # Create a save file dialog
        dialog = wxFileDialog(None, message="Bronbestand Kiezen", style=wxOPEN, wildcard="*.db")

        # Show the dialog and get user input
        if dialog.ShowModal() == wxID_OK:
            sourceFile = dialog.GetPath()

        # Destroy the dialog

        dialog.Destroy()

        # Create a save file dialog
        dialog = wxFileDialog(None, message="Doelbestand Kiezen", style=wxSAVE | wxOVERWRITE_PROMPT,
                              wildcard="SQL files (*.sql)|*.sql|SQLITE3 files (*.db)|*.db")

        # Show the dialog and get user input
        if dialog.ShowModal() == wxID_OK:
            destinationFile = dialog.GetPath()

        # Destroy the dialog

        dialog.Destroy()

        utils.BackupDatabase.BackupDB(sourceFile, destinationFile, FILETYPES[destinationFile.split(".")[1]])

  
