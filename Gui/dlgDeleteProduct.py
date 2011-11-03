from Gui import GeneratedGui
class dlgDeleteProduct(GeneratedGui.dlgDeleteProductBase):

    def __init__(self, parent):
        GeneratedGui.dlgDeleteProductBase.__init__(self, parent)
        
    def btnCancelOnButtonClick(self, event):
        self.EndModal(0)
        
    def btnDeleteOnButtonClick(self, event):
        self.EndModal(1)
        
    def btnUnCoupleOnButtonClick(self, event):
        self.EndModal(2)