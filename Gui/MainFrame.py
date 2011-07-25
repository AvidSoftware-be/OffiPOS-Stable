"""Subclass of MainFrameBase, which is generated by wxFormBuilder."""

import wx
from DataModel.ProductScreen import ProductScreen
from DataModel.ScreenGroup import ScreenGroup
from DataModel.Ticket import Ticket, priceModes, discountTypes
from DataModel.Product import  Product
import GeneratedGui

# Implementing MainFrameBase
from Gui import *
from Gui.AdminDialog import AdminDialog
from Gui.PaymentFrame import PaymentFrame
from Gui.dlgAskForPrice import dlgAskForPrice

from datetime import date, datetime
import utils.dbmanip

class MainFrame(GeneratedGui.MainFrameBase):
    _selectedGroup = 1

    def __init__( self, parent ):
        GeneratedGui.MainFrameBase.__init__(self, parent)

        utils.dbmanip.CreateDB() #test of db bestaat en zo niet wordt hij aangemaakt

        self.ticket = Ticket()

        #add product buttons to dictionary for later reference
        self.buttonDict = {
            self.btnProduct11: 11,
            self.btnProduct12: 12,
            self.btnProduct13: 13,
            self.btnProduct14: 14,
            self.btnProduct15: 15,
            self.btnProduct16: 16,
            self.btnProduct21: 21,
            self.btnProduct22: 22,
            self.btnProduct23: 23,
            self.btnProduct24: 24,
            self.btnProduct25: 25,
            self.btnProduct26: 26,
            self.btnProduct31: 31,
            self.btnProduct32: 32,
            self.btnProduct33: 33,
            self.btnProduct34: 34,
            self.btnProduct35: 35,
            self.btnProduct36: 36,
            self.btnProduct41: 41,
            self.btnProduct42: 42,
            self.btnProduct43: 43,
            self.btnProduct44: 44,
            self.btnProduct45: 45,
            self.btnProduct46: 46,
            self.btnProduct51: 51,
            self.btnProduct52: 52,
            self.btnProduct53: 53,
            self.btnProduct54: 54,
            self.btnProduct55: 55,
            self.btnProduct56: 56,
            self.btnProduct61: 61,
            self.btnProduct62: 62,
            self.btnProduct63: 63,
            self.btnProduct64: 64,
            self.btnProduct65: 65,
            self.btnProduct66: 66,
            self.btnProduct71: 71,
            self.btnProduct72: 72,
            self.btnProduct73: 73,
            self.btnProduct74: 74,
            self.btnProduct75: 75,
            self.btnProduct76: 76
        }

        self.pnlGroepen.Enabled = False
        self.pnlProducten.Enabled = False
        self.pnlRekening.Enabled = False
        self.pnlRekening.Enabled = False
        self.btnNieuwTicket.Enabled = True

        #Empty out Group Buttons
        self.btnGroupOne.Enabled = False
        self.btnGroupOne.SetLabel("")
        self.btnGroupTwo.Enabled = False
        self.btnGroupTwo.SetLabel("")
        self.btnGroupThree.Enabled = False
        self.btnGroupThree.SetLabel("")
        self.btnGroupFour.Enabled = False
        self.btnGroupFour.SetLabel("")
        self.btnGroupFive.Enabled = False
        self.btnGroupFive.SetLabel("")
        self.btnGroupSix.Enabled = False
        self.btnGroupSix.SetLabel("")
        self.btnGroupSeven.Enabled = False
        self.btnGroupSeven.SetLabel("")
        self.btnGroupEight.Enabled = False
        self.btnGroupEight.SetLabel("")

        #fill group buttons
        for name in ScreenGroup().fetchall():
            if name[2] == 1:
                self.btnGroupOne.SetLabel(name[1].replace(" ", "\n"))
            elif name[2] == 2:
                self.btnGroupTwo.SetLabel(name[1].replace(" ", "\n"))
            elif name[2] == 3:
                self.btnGroupThree.SetLabel(name[1].replace(" ", "\n"))
            elif name[2] == 4:
                self.btnGroupFour.SetLabel(name[1].replace(" ", "\n"))
            elif name[2] == 5:
                self.btnGroupFive.SetLabel(name[1].replace(" ", "\n"))
            elif name[2] == 6:
                self.btnGroupSix.SetLabel(name[1].replace(" ", "\n"))
            elif name[2] == 7:
                self.btnGroupSeven.SetLabel(name[1].replace(" ", "\n"))
            elif name[2] == 8:
                self.btnGroupSeven.SetLabel(name[1].replace(" ", "\n"))

        self._updateProductButtons()

        self.btnRetour.SetValue(0)
        self.btnAanbDirToggle.SetValue(0)

        if self.ticket.eatInOut == "O":
            self.btnInOutToggle.SetValue(0)
        else:
            self.btnInOutToggle.SetValue(1)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updateClock, self.timer)
        self.timer.Start(1000)

    def updateClock(self,event):
        self.SetStatusText("{0} {1}".format(date.today().strftime('%d/%m/%Y'), datetime.today().strftime('%H:%M:%S')))


    # Handlers for MainFrameBase events.
    def btnNieuwTicketOnButtonClick( self, event ):
        self.pnlGroepen.Enabled = True
        self.pnlProducten.Enabled = True
        self.pnlRekening.Enabled = True
        self.btnNieuwTicket.Enabled = False

        self.ticket.CreateNewTicket()

        if self.ticket.eatInOut == "O":
            self.btnInOutToggle.SetValue(0)
        else:
            self.btnInOutToggle.SetValue(1)

        self.btnRetour.SetValue(0)

        self.ticket.priceMode = priceModes["pos"]
        self.btnAanbDirToggle.SetValue(0)

        self._selectedGroup = 1
        self._updateProductButtons()

        self._updateGrid()

    def btnAnnulerenOnButtonClick( self, event ):
        self.pnlGroepen.Enabled = False
        self.pnlProducten.Enabled = False
        self.pnlRekening.Enabled = False
        self.btnNieuwTicket.Enabled = True

        self.ticket.CancelTicket()

        self._updateGrid()

    def btnAfrekekenOnButtonClick( self, event ):
        self.pnlGroepen.Enabled = False
        self.pnlProducten.Enabled = False
        self.pnlRekening.Enabled = False
        self.btnNieuwTicket.Enabled = True

        #self.ticket.PayTicket()
        frmPayment = PaymentFrame(self)
        frmPayment.SetTicket(self.ticket)
        frmPayment.ShowModal()

        if frmPayment.cancelled:
            self.pnlGroepen.Enabled = True
            self.pnlProducten.Enabled = True
            self.pnlRekening.Enabled = True
            self.btnNieuwTicket.Enabled = False

        self.btnRetour.Value = 0

    def btnGroupOneOnButtonClick( self, event ):
        self._selectedGroup = 1
        self._updateProductButtons()

    def btnGroupTwoOnButtonClick( self, event ):
        self._selectedGroup = 2
        self._updateProductButtons()

    def btnGroupThreeOnButtonClick( self, event ):
        self._selectedGroup = 3
        self._updateProductButtons()

    def btnGroupFourOnButtonClick( self, event ):
        self._selectedGroup = 4
        self._updateProductButtons()

    def btnGroupFiveOnButtonClick( self, event ):
        self._selectedGroup = 5
        self._updateProductButtons()

    def btnGroupSixOnButtonClick( self, event ):
        self._selectedGroup = 6
        self._updateProductButtons()

    def btnGroupSevenOnButtonClick( self, event ):
        self._selectedGroup = 7
        self._updateProductButtons()

    def btnGroupEightOnButtonClick( self, event ):
        self._selectedGroup = 8
        self._updateProductButtons()

    def btnProductOnButtonClick( self, event ):
        thisButton = event.GetEventObject()
        buttonNoPressed = self.buttonDict[thisButton]

        productNo = 0
        isOption = False
        parentProductId = 0
        mydiscountType = discountTypes["none"]

        if not self._selectedGroup:
            #dit is een optie
            ticketLines = self.ticket.GetTicketLines()
            parentProductId = ticketLines[len(ticketLines) - 1][3]
            productNo = ProductScreen().GetOptionProductNoOnButton(buttonNoPressed,
                                                                   parentProductId)
            isOption = True
        else:
            productNo = ProductScreen().GetProductNoOnButton(buttonNoPressed, self._selectedGroup)

        product = Product(productNo)
        product.fill()
        prodPrice = 0
        if product.askForPrice:
            #prijs ophalen
            askForPriceForm = dlgAskForPrice(self)
            askForPriceForm.ShowModal()

            if product.askForPrice == 2:
                prodPrice = askForPriceForm.Value * -1 #teken omdraaien, bvb in geval van korting
            else:
                prodPrice = askForPriceForm.Value

        if self.btnAanbDirToggle.Value:
            prodPrice = 0
            mydiscountType = discountTypes["Aanbieding Directie"]

        self.ticket.AddTicketLine(productNo, isOption, parentProductId, buttonNoPressed, self._selectedGroup, prodPrice,
                                  mydiscountType)

        options = ProductScreen().GetOptionsForProduct(productNo)

        if options:
            self._updateProductButtonsForOption(productNo, options)

        if isOption:
            self._selectedGroup = ProductScreen().GetNextScreenForOption(parentProductId, productNo, buttonNoPressed)
            self._updateProductButtons()

        self._updateGrid()

    def btnInOutToggleOnToggleButton( self, event ):
        button = event.GetEventObject()
        if button.GetValue():
            self.ticket.SetEatInOut("I")
        else:
            self.ticket.SetEatInOut("O")

    def btnAdminOnButtonClick( self, event ):
        adminMenu = AdminDialog(self)
        adminMenu.ShowModal()

    def btnRetourOnToggleButton( self, event ):
        button = event.GetEventObject()
        if button.GetValue():
            self.ticket.priceMode = priceModes["neg"]
        else:
            self.ticket.priceMode = priceModes["pos"]

    def btnQtyMinOnButtonClick( self, event ):
        rowNo = self.gOrder.GetGridCursorRow()

        ticketLines = self.ticket.GetTicketLines()

        entryNo = ticketLines[rowNo][4]

        self.ticket.DeleteTickeLine(entryNo)

        self._updateGrid()


    def _updateProductButtonsForOption(self, productId, options):
        self._clearButtonNames()

        for option in options:
            product = Product(id=option[2])
            product.fill()

            if product.id == 9999:
                #speciaal!
                caption = option[7]
            else:
                caption = product.screenName

            control = getattr(self, "btnProduct%s" % (str(option[3])))
            control.SetLabel(caption.strip().replace(" ", "\n"))
            control.SetBackgroundColour(option[5])
            control.Refresh()

        self._selectedGroup = 0


    def _updateProductButtons(self):
        self._clearButtonNames()

        productsInScreen = ProductScreen().GetProductsForScreen(self._selectedGroup)

        for productLine in productsInScreen:
            product = Product(id=productLine[2])
            product.fill()

            control = getattr(self, "btnProduct%s" % (str(productLine[3])))

            caption = ""
            if productLine[2] == 9999:
                #speciaal!
                caption = productLine[5]
            else:
                caption = product.screenName

            control.SetLabel(caption.strip().replace(" ", "\n"))
            control.SetBackgroundColour(productLine[4])
            control.Refresh()

    def _clearButtonNames(self):
        r = 1
        c = 1
        for i in range(1, 43):
            buttonNo = c + r * 10
            control = getattr(self, "btnProduct%s" % (str(buttonNo)))
            control.SetLabel("")
            control.SetBackgroundColour('0')
            control.Refresh()
            c = c + 1
            if c == 7:
                c = 1
                r = r + 1

    def _updateGrid(self):
        grid = self.gOrder
        table = OrderTable(ticket=self.ticket)
        grid.SetTable(table)
        rows=table.GetNumberRows()
        grid.MakeCellVisible(rows-1,1)
        grid.EnableEditing(False)
        grid.SetSelectionMode(wx.grid.Grid.SelectRows)
        grid.SetRowLabelSize(0)
        grid.AutoSizeColumns()

        self._updateTotal()

    def _updateTotal(self):
        total = self.ticket.GetTotalAmt()

        self.lblTotal.SetLabel(u"\u20AC %.2f" % total)


class OrderTable(wx.grid.PyGridTableBase):
    def __init__(self, ticket):
        wx.grid.PyGridTableBase.__init__(self)
        self.colLabels = ["#", "Product", "Prijs"]

        self.ticketLines = ticket.GetTicketLines()

    def GetNumberRows(self):
        return len(self.ticketLines)

    def GetNumberCols(self):
        return len(self.colLabels)

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        if col == 0:
            return "%s" % (row + 1)
        elif col == 2:
            return "%.2f" % self.ticketLines[row][col - 1]
        else:
            return "%s" % self.ticketLines[row][col - 1]

    def SetValue(self, row, col, value):
        pass

    def GetColLabelValue(self, col):
        return self.colLabels[col]

    def GetRowLabelValue(self, row):
        return self.rowLabels[row]
        

