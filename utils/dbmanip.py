from datetime import date, datetime
from DataModel.Customer import Customer

__author__ = 'dennis'

import sqlite3
import ini

#conn = sqlite3.connect(ini.DB_NAME)
#cur = conn.cursor()
#
#def insertprod(fromid, toid, screenGroup):
#    r=1
#    c=1
#    for i in range(fromid, toid):
#        buttonNo = c+r*10
#        print buttonNo
#        cur.execute("insert into product_screen (screenCategoryId, productId, buttonNo, bgColor) values(?,?,?,?)",(screenGroup,i,buttonNo,0))
#        c=c+1
#        if c==7:
#            c=1
#            r=r+1
#
#
#
#
#insertprod(1,36,1)
#insertprod(36,52,4)
#insertprod(101,150,2)
#insertprod(230,244,4)
#insertprod(301,333,3)
#
#conn.commit()

#Customer().GetCustomerFromLoyaltyCard("t2tt")

datestring = ini.MINDATE.strftime("%d-%m-%Y")
print datestring
dateobj = datetime.strptime(datestring, "%d-%m-%Y")
print dateobj.strftime("%d-%m-%Y")