import sqlite3,os
import StringIO
import ini
import codecs

__author__ = 'dennis'

def DoBackup(sourceFile,destinationFile):
    connsrc = sqlite3.connect(sourceFile)
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

def DumpDB(sourceFile="..\\"+ini.DB_NAME,destinationFile='Backup.sql'):
    con = sqlite3.connect(sourceFile)
    file = codecs.open(destinationFile,'w','utf-8')

    for line in con.iterdump():
        file.write(u"{0:>s}\n".format(line))

if __name__ == '__main__':
    DumpDB()
    




