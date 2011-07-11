from DataModel.Customer import Customer
import GeneratedGui
import wx

__author__ = 'dennis'

class dlgCustomerEdit(GeneratedGui.dlgCustomerEditBase):
    def __init__( self, parent ):
        GeneratedGui.dlgCustomerEditBase.__init__(self, parent)
        self.customer = Customer()

    def SetCustomer(self, customerId):
        self.customer.FillFromId(customerId)
        self.UpdateForm()

    def UpdateForm(self):
        self.txtNr.Value = str(self.customer.id) if self.customer.id else ""
        self.txtNaam.Value = self.customer.name if self.customer.name else ""
        self.txtVoornaam.Value = self.customer.firstName if self.customer.firstName else ""
        self.txtAdres.Value = self.customer.address if self.customer.address else ""
        self.txtPostcode.Value = self.customer.postalCode if self.customer.postalCode else ""
        self.txtGemeente.Value = self.customer.city if self.customer.city else ""
        self.txtTelefoon.Value = self.customer.telephone if self.customer.telephone else ""
        self.txtEmailadres.Value = self.customer.emailAddress if self.customer.emailAddress else ""
        self.txtKlantkaart.Value = self.customer.loyaltyCardNo if self.customer.loyaltyCardNo else ""

    def btnOpslaanOnButtonClick( self, event ):
        self.SaveFormValues()
        self.Close()

    def btnOpslaanEnNieuwOnButtonClick( self, event ):
        self.SaveFormValues()
        self.ClearValues()

    def SaveFormValues(self):
        pass

    def ClearValues(self):
        pass

