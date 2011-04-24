__author__ = 'dennis'


import GeneratedGui
import wx
import logging
logger = logging.getLogger(__name__)


class MainFrame (GeneratedGui.MainFrame):
    def __init__( self, parent ):
        GeneratedGui.MainFrame.__init__(self, parent)

        self.sbProducten.Add( pnlFrieten( parent), 1, wx.EXPAND |wx.ALL, 5 )
        

class pnlFrieten (GeneratedGui.pnlFrieten):
    def __init__( self, parent ):
        GeneratedGui.pnlFrieten.__init__(self, parent)