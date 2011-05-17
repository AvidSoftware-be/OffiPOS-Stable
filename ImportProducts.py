from DataModel.Product import Product

__author__ = 'dennis'

from xml.etree import ElementTree

tree = ElementTree.parse("PLU.XML")
root = tree.getroot()
for plu in root.getiterator("PLU"):
    prndesc = plu.find("prn_desc").text
    if (prndesc is not None) and (prndesc.strip() != ""):
        prod = Product(id=int(plu.find("num").text),
                       price=float(plu.find("prix_1").text),
                       name=plu.find("prn_desc").text,
                       group=0,
                       vatCodeIn=int(plu.find("code_tva_in").text),
                       vatCodeOut=int(plu.find("code_tva_out").text))

        prod.save()

print prod.fetchall()

print Product(id=1,price=0,group=0,name="",vatCodeIn=0,vatCodeOut=0).fetch()
  