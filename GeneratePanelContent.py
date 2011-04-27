from DataModel.ProductConstants import BaronProducts

__author__ = 'dennis'

itemCount = 0
for group in BaronProducts:
    for product in BaronProducts[group]:
        print "{0}:{1}".format(product,BaronProducts[group][product].name)
        itemCount += 1
        if itemCount == 5:
            #new row
            pass