from DataModel.ScreenGroup import ScreenGroup
from DataModel.ProductScreen import ProductScreen
from DataModel.Product import Product
def fillGroupButtons(self):
#fill group buttons
    for name in ScreenGroup().fetchall():
        if name[2] == 1:
            self.pnlGroepen.btnGroupOne.SetLabel(name[1].replace(" ", "\n"))
        elif name[2] == 2:
            self.pnlGroepen.btnGroupTwo.SetLabel(name[1].replace(" ", "\n"))
        elif name[2] == 3:
            self.pnlGroepen.btnGroupThree.SetLabel(name[1].replace(" ", "\n"))
        elif name[2] == 4:
            self.pnlGroepen.btnGroupFour.SetLabel(name[1].replace(" ", "\n"))
        elif name[2] == 5:
            self.pnlGroepen.btnGroupFive.SetLabel(name[1].replace(" ", "\n"))
        elif name[2] == 6:
            self.pnlGroepen.btnGroupSix.SetLabel(name[1].replace(" ", "\n"))
        elif name[2] == 7:
            self.pnlGroepen.btnGroupSeven.SetLabel(name[1].replace(" ", "\n"))
        elif name[2] == 8:
            self.pnlGroepen.btnGroupSeven.SetLabel(name[1].replace(" ", "\n"))
            
        
def updateProductButtons(self, selectedGroup):
    clearButtonNames(self)

    productsInScreen = ProductScreen().GetProductsForScreen(selectedGroup)

    for productLine in productsInScreen:
        product = Product(id=productLine[2])
        product.fill()

        control = getattr(self.pnlProducten, "btnProduct%s" % (str(productLine[3])))

        caption = ""
        if productLine[2] == 9999:
            #speciaal!
            caption = productLine[5]
        else:
            caption = product.screenName

        control.SetLabel(caption.strip().replace(" ", "\n"))
        control.SetBackgroundColour(productLine[4])
        control.Refresh()

def clearButtonNames(self):
    r = 1
    c = 1
    for i in range(1, 43):
        buttonNo = c + r * 10
        control = getattr(self.pnlProducten, "btnProduct%s" % (str(buttonNo)))
        control.SetLabel("")
        control.SetBackgroundColour('0')
        control.Refresh()
        c = c + 1
        if c == 7:
            c = 1
            r = r + 1
            
def createButtonDict(self):
    return {
            self.pnlProducten.btnProduct11: 11,
            self.pnlProducten.btnProduct12: 12,
            self.pnlProducten.btnProduct13: 13,
            self.pnlProducten.btnProduct14: 14,
            self.pnlProducten.btnProduct15: 15,
            self.pnlProducten.btnProduct16: 16,
            self.pnlProducten.btnProduct21: 21,
            self.pnlProducten.btnProduct22: 22,
            self.pnlProducten.btnProduct23: 23,
            self.pnlProducten.btnProduct24: 24,
            self.pnlProducten.btnProduct25: 25,
            self.pnlProducten.btnProduct26: 26,
            self.pnlProducten.btnProduct31: 31,
            self.pnlProducten.btnProduct32: 32,
            self.pnlProducten.btnProduct33: 33,
            self.pnlProducten.btnProduct34: 34,
            self.pnlProducten.btnProduct35: 35,
            self.pnlProducten.btnProduct36: 36,
            self.pnlProducten.btnProduct41: 41,
            self.pnlProducten.btnProduct42: 42,
            self.pnlProducten.btnProduct43: 43,
            self.pnlProducten.btnProduct44: 44,
            self.pnlProducten.btnProduct45: 45,
            self.pnlProducten.btnProduct46: 46,
            self.pnlProducten.btnProduct51: 51,
            self.pnlProducten.btnProduct52: 52,
            self.pnlProducten.btnProduct53: 53,
            self.pnlProducten.btnProduct54: 54,
            self.pnlProducten.btnProduct55: 55,
            self.pnlProducten.btnProduct56: 56,
            self.pnlProducten.btnProduct61: 61,
            self.pnlProducten.btnProduct62: 62,
            self.pnlProducten.btnProduct63: 63,
            self.pnlProducten.btnProduct64: 64,
            self.pnlProducten.btnProduct65: 65,
            self.pnlProducten.btnProduct66: 66,
            self.pnlProducten.btnProduct71: 71,
            self.pnlProducten.btnProduct72: 72,
            self.pnlProducten.btnProduct73: 73,
            self.pnlProducten.btnProduct74: 74,
            self.pnlProducten.btnProduct75: 75,
            self.pnlProducten.btnProduct76: 76
        }
