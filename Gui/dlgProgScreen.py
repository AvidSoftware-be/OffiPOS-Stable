from DataModel.ProductScreen import ProductScreen
from Gui.dlgProductEdit import dlgProductEdit
import GeneratedGui
import Gui.helpers
import wx

class dlgProgScreen(GeneratedGui.dlgProgScreenBase):
    _selectedGroup = 1
    
    def __init__(self, parent):
        GeneratedGui.dlgProgScreenBase.__init__(self, parent)
        
        self.pnlProducten = GeneratedGui.pnlProductenBase(self)
        self.sbProducten.Add(self.pnlProducten, 1, wx.EXPAND | wx.ALL, 1)
        
        self.pnlGroepen = GeneratedGui.pnlGroepenBase(self)
        self.sbGroepen.Add(self.pnlGroepen, 1, wx.EXPAND | wx.ALL, 1)
        
        self.Layout()
        self.fgSizer7.Fit(self)
        
        Gui.helpers.fillGroupButtons(self)
        Gui.helpers.updateProductButtons(self, self._selectedGroup)
        
        # Connect Events
        self.pnlProducten.btnProduct11.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct12.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct13.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct14.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct15.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct16.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct21.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct22.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct23.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct24.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct25.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct26.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct31.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct32.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct33.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct34.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct35.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct36.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct41.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct42.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct43.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct44.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct45.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct46.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct51.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct52.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct53.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct54.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct55.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct56.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct61.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct62.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct63.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct64.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct65.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct66.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct71.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct72.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct73.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct74.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct75.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        self.pnlProducten.btnProduct76.Bind(wx.EVT_BUTTON, self.btnProductOnButtonClick)
        
        # Connect Events
        self.pnlGroepen.btnGroupOne.Bind(wx.EVT_BUTTON, self.btnGroupOneOnButtonClick)
        self.pnlGroepen.btnGroupThree.Bind(wx.EVT_BUTTON, self.btnGroupThreeOnButtonClick)
        self.pnlGroepen.btnGroupFive.Bind(wx.EVT_BUTTON, self.btnGroupFiveOnButtonClick)
        self.pnlGroepen.btnGroupSeven.Bind(wx.EVT_BUTTON, self.btnGroupSevenOnButtonClick)
        self.pnlGroepen.btnGroupTwo.Bind(wx.EVT_BUTTON, self.btnGroupTwoOnButtonClick)
        self.pnlGroepen.btnGroupFour.Bind(wx.EVT_BUTTON, self.btnGroupFourOnButtonClick)
        self.pnlGroepen.btnGroupSix.Bind(wx.EVT_BUTTON, self.btnGroupSixOnButtonClick)
        self.pnlGroepen.btnGroupEight.Bind(wx.EVT_BUTTON, self.btnGroupEightOnButtonClick)
        
        #add product buttons to dictionary for later reference
        self.buttonDict = Gui.helpers.createButtonDict(self)
  
    def btnGroupOneOnButtonClick(self, event):
        self._selectedGroup = 1
        Gui.helpers.updateProductButtons(self, self._selectedGroup)

    def btnGroupTwoOnButtonClick(self, event):
        self._selectedGroup = 2
        Gui.helpers.updateProductButtons(self, self._selectedGroup)

    def btnGroupThreeOnButtonClick(self, event):
        self._selectedGroup = 3
        Gui.helpers.updateProductButtons(self, self._selectedGroup)
        
    def btnGroupFourOnButtonClick(self, event):
        self._selectedGroup = 4
        Gui.helpers.updateProductButtons(self, self._selectedGroup)

    def btnGroupFiveOnButtonClick(self, event):
        self._selectedGroup = 5
        Gui.helpers.updateProductButtons(self, self._selectedGroup)

    def btnGroupSixOnButtonClick(self, event):
        self._selectedGroup = 6
        Gui.helpers.updateProductButtons(self, self._selectedGroup)

    def btnGroupSevenOnButtonClick(self, event):
        self._selectedGroup = 7
        Gui.helpers.updateProductButtons(self, self._selectedGroup)

    def btnGroupEightOnButtonClick(self, event):
        self._selectedGroup = 8
        Gui.helpers.updateProductButtons(self, self._selectedGroup)

    def btnProductOnButtonClick(self, event):
        thisButton = event.GetEventObject()
        buttonNoPressed = self.buttonDict[thisButton]
        
        dlg = dlgProductEdit(self, buttonNoPressed, self._selectedGroup)

        dlg.ShowModal()
        
        Gui.helpers.updateProductButtons(self, self._selectedGroup)
        
