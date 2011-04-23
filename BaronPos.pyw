__author__ = 'dennis'

import wx
import gui

import logging

LOG_FILENAME = 'BFClient.log'

logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
log=logging.getLogger(__name__)

class BFClientApp(wx.App):
    def OnInit(self):
        self.frame = gui.mainFrame(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = BFClientApp(False)
    app.MainLoop()