import DataModel

__author__ = 'dennis'

import GeneratedGui

class AdminDialog(GeneratedGui.AdminDialogBase):
    def __init__( self, parent ):
        GeneratedGui.AdminDialogBase.__init__(self, parent)

    def btnKasAfsluitenOnButtonClick( self, event ):
        DataModel.VATManipulations.DoEndOfDay()

  