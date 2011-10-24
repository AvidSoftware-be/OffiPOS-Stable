from datetime import date, timedelta
import wx
import DataModel
from DataModel.Customer import Customer
from DataModel.Ticket import Ticket, discountTypes

from Gui.dlgAskForPrice import dlgAskForPrice
from Gui.frmKlantBeheer import frmKlantBeheer

__author__ = 'dennis'

import GeneratedGui

# Implementing MainFrameBase

class PaymentFrame(GeneratedGui.PaymentFrameBase):
    def __init__( self, parent ):
        GeneratedGui.PaymentFrameBase.__init__(self, parent)

        self.ticket = Ticket()
        self.paymentMethod = 0
        self.cancelled = False
        self.LoyaltyPayout = False

        self.btnEnter.Enabled=False

        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def SetTicket(self, ticket):
        self.ticket = ticket

        self.txtTotal.Value = "%.2f" % self.ticket.GetTotalAmt()
        self.txtTotalToPay.Value = self.txtTotal.Value

        self.txtPuntenTicket.Value = "{0:>.0f}".format(self.ticket.GetLoyaltyCardPoints())

    def btnOneOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "1"
        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def btnTwoOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "2"
        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def btnThreeOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "3"
        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def btnFourOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "4"
        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def btnFiveOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "5"
        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def btnSixOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "6"
        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def btnSevenOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "7"
        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def btnEightOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "8"
        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def btnNineOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "9"
        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def btnZeroOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "0"
        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def btnDotOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtPayed.Value + "."
        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def btnCashOnButtonClick( self, event ):
        if not self.txtPayed.Value:
            #correct bedrag gegeven
            self.txtPayed.Value = self.txtTotalToPay.Value

        payed = float(self.txtPayed.Value)
        toReturn = float(self.txtTotalToPay.Value) - payed

        self.txtReturn.Value = "%.2f" % toReturn

        self.paymentMethod = DataModel.Ticket.paymentMethods["Cash"]
        
        self.btnEnter.Enabled=True

        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def btnAtosOnButtonClick( self, event ):
        self.txtPayed.Value = self.txtTotalToPay.Value

        payed = float(self.txtPayed.Value)
        toReturn = float(self.txtTotalToPay.Value) - payed

        self.txtReturn.Value = "%.2f" % toReturn

        self.paymentMethod = DataModel.Ticket.paymentMethods["Atos"]

        cust = Customer()
        cust.GetCustomerFromLoyaltyCard(self.txtKantKaart.Value)
        if cust:
            cust.AddLoyaltyPoints(self.ticket.GetLoyaltyCardPoints())

        self.ticket.SetCustomer(cust)
        self.ticket.PayTicket(self.paymentMethod, payed, toReturn)

        self.Close()

    def btnEnterOnButtonClick( self, event ):
        payed = float(self.txtPayed.Value)
        toReturn = float(self.txtTotalToPay.Value) - payed
        cust = Customer()
        cust.GetCustomerFromLoyaltyCard(self.txtKantKaart.Value)
        if cust:
            cust.AddLoyaltyPoints(self.ticket.GetLoyaltyCardPoints())

        self.ticket.SetCustomer(cust)
        self.ticket.PayTicket(self.paymentMethod, payed, toReturn)

        self.Close()

    def btnClrOnButtonClick( self, event ):
        self.txtReturn.Value = ""
        self.txtPayed.Value = ""

        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def btnClsOnButtonClick( self, event ):
        self.cancelled = True
        self.Close()

    def ValidateLoyaltyCard(self):
        cust = Customer()
        cust.GetCustomerFromLoyaltyCard(self.txtKantKaart.Value)
        if cust.firstName:
            self.txtCustomerName.SetValue("{0:>s} {1:>s}".format(cust.firstName, cust.name))
        else:
            self.txtCustomerName.SetValue("")
        if cust.loyaltyPoints:
            self.txtPuntenKaart.SetValue("{0:>.0f}".format(cust.loyaltyPoints))
        else:
            self.txtPuntenKaart.SetValue("0")
        if cust.CanPayDiscount():
            newTotalPoints = cust.loyaltyPoints - cust.GetPointsToDeductOnBonus()
            self.txtKorting.SetValue("{0:>.2f}".format(cust.loyaltyDiscount))
            #self.txtTotalToPay.SetValue("{0:>.2f}".format(float(self.txtTotal.Value) - float(self.txtKorting.Value)))
            self.ticket.AddTicketLine(343, False, 0, 22, 5, cust.loyaltyDiscount * -1, discountTypes["Klantkaart"])
            cust.PayLoyaltyPoints()
            self.SetTicket(self.ticket)
        else:
            newTotalPoints = int(self.txtPuntenTicket.Value) + int(self.txtPuntenKaart.Value)
        self.txtNieuwSaldo.SetValue("{0:>.0f}".format(newTotalPoints))

    def txtKantKaartOnKillFocus( self, event ):
        self.ValidateLoyaltyCard()

    def txtPuntenTicketOnSetFocus( self, event ):
        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

    def btnAddLoyaltyPointsOnButtonClick( self, event ):
        askForPriceForm = dlgAskForPrice(self)
        askForPriceForm.ShowModal()
        
        cust = Customer()
        cust.GetCustomerFromLoyaltyCard(self.txtKantKaart.Value)
        if cust:
            cust.AddLoyaltyPoints(askForPriceForm.Value)

        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()

        self.ValidateLoyaltyCard()

    def btnPrintKitchenOnButtonClick( self, event ):
        self.ticket.PrintKitchen()
        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()
        
    def btnKlantOpzoekenOnButtonClick(self, event):
        klantBeheer = frmKlantBeheer(self)
        
        klantBeheer.Center()
        
        klantBeheer.ShowModal()
        
        self.txtKantKaart.Value = klantBeheer.customer.loyaltyCardNo
        
        self.txtKantKaart.SelectAll()
        self.txtKantKaart.SetFocus()
        
    def chkPrintKitchenOnCheckBox(self, event):
        self.ticket.KitchenPrinted = not self.chkPrintKitchen.Value
        
    def chkPrintTicketOnCheckBox(self,event):
        self.ticket.TicketPrinted = not self.chkPrintTicket.Value
  