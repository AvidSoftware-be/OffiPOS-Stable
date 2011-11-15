from DataModel.ProductOptionTable import ProductOptionTable
from DataModel.Product import Product
from DataModel.ProductGroup import ProductGroup
from DataModel.ProductScreen import ProductScreen
from DataModel.VatCode import VatCode
from Gui.dlgDeleteProduct import dlgDeleteProduct
from Gui.dlgSelectProduct import dlgSelectProduct
import GeneratedGui
import wx

__author__ = 'dennis'

class dlgProductEdit(GeneratedGui.dlgProductEditBase):

    def __init__(self, parent, buttonNo, selectedGroup):
        GeneratedGui.dlgProductEditBase.__init__(self, parent)
        self.product = Product(0)
        self._setGroups()
        self._setVatIn()
        self._setVatOut()
        
        self.product = Product(ProductScreen().GetProductNoOnButton(buttonNo, selectedGroup))
        #self.product.fill()
        self.buttonNo = buttonNo
        self.screenCategoryId = selectedGroup
        
        ps = ProductScreen()
        ps.GetProductNoOnButton(self.buttonNo, self.screenCategoryId)
        self.colourPicker.SetColour(ps.bgColor)
        
        self.UpdateForm()
    
    def btnOpslaanOnButtonClick(self, event):
        self.product.name = self.txtOmschrijving.GetValue()
        self.product.screenName = self.txtSchermOmschrijving.GetValue()
        self.product.price = float(self.txtPrijs.GetValue())
        self.product.discountIfOption = float(self.txtKorting.GetValue())
        self.product.group = self.chGroep.GetSelection() + 1
        self.product.vatCodeIn = self.chBTWIn.GetSelection() + 1
        self.product.vatCodeOut = self.chBTWOut.GetSelection() + 1
        self.product.askForPrice = self.chkAskForPrice.GetValue()
        if self.chkReverseSign.GetValue():
            self.product.askForPrice = 2
        self.product.treatAsOption = self.chkTreatAsOption.GetValue()
        
        self.product.save()
        
        ps = ProductScreen()
        ps.productId = self.product.id
        ps.buttonNo = self.buttonNo
        ps.screenCategoryId = self.screenCategoryId
        ps.bgColor = self.colourPicker.GetColour().GetAsString(wx.C2S_HTML_SYNTAX)
        ps.save()
        
        self.UpdateForm()
        
    def btnDeleteOnButtonClick(self, event):
        
        dp = dlgDeleteProduct(self)
        ret = dp.ShowModal()
        
        if ret == 1: #Delete
            self.product.delete()
            
            ps = ProductScreen() #todo: dubbele code vermijden
            ps.productId = self.product.id
            ps.deleteByProductId()
            
            self.product = Product(0)
            
            self.UpdateForm()
            
        elif ret == 2: #Uncouple
            ps = ProductScreen()
            ps.productId = self.product.id
            ps.deleteByProductId()
            
            
            
    def btnSearchOnButtonClick(self, event):
        sp = dlgSelectProduct(self)
        ret = sp.ShowModal()
        if ret:
            self.product = Product(ret)
        else:
            self.product = Product(0)
            
        self.UpdateForm()

    def UpdateForm(self):
        self.txtProductNo.SetValue(str(self.product.id))
        self.txtOmschrijving.SetValue(self.product.name)
        self.txtSchermOmschrijving.SetValue(self.product.screenName)
        self.txtPrijs.SetValue("{0:>.2f}".format(self.product.price))
        self.txtKorting.SetValue("{0:>.2f}".format(self.product.discountIfOption))
        if self.product.group:
            self.chGroep.SetSelection(self.product.group - 1)
        else:
            self.chGroep.SetSelection(0)
        if self.product.vatCodeIn:
            self.chBTWIn.SetSelection(self.product.vatCodeIn - 1)
        else:
            self.chBTWIn.SetSelection(0)
        if self.product.vatCodeOut:
            self.chBTWOut.SetSelection(self.product.vatCodeOut - 1)
        else:
            self.chBTWOut.SetSelection(0)
        self.chkTreatAsOption.SetValue(self.product.treatAsOption)
        self.chkAskForPrice.SetValue(self.product.askForPrice)
        if self.product.askForPrice == 2:
            self.chkReverseSign.SetValue(1)
            
        #opties updaten
        
        grid = self.m_grid4
        table = ProductOptionTable(self.product.id)
        grid.SetTable(table)
        rows = table.GetNumberRows()
        grid.MakeCellVisible(rows - 1, 1)
        grid.EnableEditing(False)
        grid.SetSelectionMode(wx.grid.Grid.SelectRows)
        grid.SetRowLabelSize(0)
            
    def _setGroups(self):
        groups = ProductGroup().fetchall()
        self.chGroep.Clear()
        for group in groups:
            self.chGroep.Append(group[1])
            
    def _setVatIn(self):
        vatcodes = VatCode().fetchall()
        self.chBTWIn.Clear()
        for vatcode in vatcodes:
            self.chBTWIn.Append(vatcode[1])
            
    def _setVatOut(self):
        vatcodes = VatCode().fetchall()
        self.chBTWOut.Clear()
        for vatcode in vatcodes:
            self.chBTWOut.Append(vatcode[1])
            
        
