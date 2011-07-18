from datetime import date, datetime
from wxPython._misc import wxDateTimeFromDMY
from DataModel.Customer import Customer
import GeneratedGui
import wx
import ini

__author__ = 'dennis'

class dlgCustomerEdit(GeneratedGui.dlgCustomerEditBase):
    def __init__( self, parent ):
        GeneratedGui.dlgCustomerEditBase.__init__(self, parent)
        self.customer = Customer()
        self.ClearValues()

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
        self.datePickerGeboorte.SetValue(
            wxDateTimeFromDMY(self.customer.birthDate.day, self.customer.birthDate.month - 1,
                              self.customer.birthDate.year))

    def btnOpslaanOnButtonClick( self, event ):
        self.SaveFormValues()
        self.Close()

    def btnOpslaanEnNieuwOnButtonClick( self, event ):
        self.SaveFormValues()
        self.ClearValues()

    def SaveFormValues(self):
        if not self.customer.id:
            #nieuwe klant
            self.customer.loyaltyPoints = ini.LOYALTYCARD_STARTING_POINTS

        birthdate = self.datePickerGeboorte.GetValue()

        self.customer.name = self.txtNaam.Value
        self.customer.firstName = self.txtVoornaam.Value
        self.customer.address = self.txtAdres.Value
        self.customer.postalCode = self.txtPostcode.Value
        self.customer.city = self.txtGemeente.Value
        self.customer.telephone = self.txtTelefoon.Value
        self.customer.emailAddress = self.txtEmailadres.Value
        self.customer.loyaltyCardNo = self.txtKlantkaart.Value
        self.customer.birthDate = date(birthdate.Year, birthdate.Month + 1, birthdate.Day)
        self.customer.Save()

    def ClearValues(self):
        self.txtNr.Value = ""
        self.txtNaam.Value = ""
        self.txtVoornaam.Value = ""
        self.txtAdres.Value = ""
        self.txtPostcode.Value = ""
        self.txtGemeente.Value = ""
        self.txtTelefoon.Value = ""
        self.txtEmailadres.Value = ""
        self.txtKlantkaart.Value = ""
        self.datePickerGeboorte.SetValue(wxDateTimeFromDMY(1,0,1900))

        self.customer = Customer()

