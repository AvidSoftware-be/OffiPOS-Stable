import sqlite3
import ini

__author__ = 'dennis'

def DoBackup(destinationFile):
    connsrc = sqlite3.connect(ini.DB_NAME)
    cursrc = connsrc.cursor()
    cursrc.execute("""SELECT
                      ticketLine.ticketNo,
                      ticketLine.productId,
                      ticketLine.productName,
                      ticketLine.price,
                      ticketLine.paid,
                      ticketLine.eatInOut,
                      ticketLine.isOption,
                      ticketLine.dateRegistered,
                      ticketLine.vatCode,
                      ticketLine.customerId,
                      ticketLine.discountType
                    FROM
                      ticketLine""")

    lines = cursrc.fetchall()

    connDest = sqlite3.connect(destinationFile)
    curDest = connDest.cursor()

    for line in lines:
        curDest.execute("INSERT INTO ticketLine (ticketNo, productId, productName, price, paid, eatInOut, isOption, dateRegistered, vatCode, customerId, discountType) values (?,?,?,?,?,?,?,?,?,?,?)",
                        line)

    connDest.commit()


