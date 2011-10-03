import DataModel
from DataModel.Ticket import Ticket
import POSEquipment
import sqlite3, ini
from datetime import datetime

__author__ = 'dennis'

def DoEndOfDay(withClear):
    dayparam = {'firstOrder': Ticket().GetFirstOrderDate(), 'lastOrder': Ticket().GetLastOrderDate()}

    dayparam['payedAmts'] = {'Cash': Ticket().GetPaymentTotal(DataModel.Ticket.paymentMethods['Cash']),
                             'Atos': Ticket().GetPaymentTotal(DataModel.Ticket.paymentMethods['Atos'])}

    dayparam['payedAmts']['Total'] = dayparam['payedAmts']['Cash'] + dayparam['payedAmts']['Atos']

    dayparam['VATLines'] = Ticket().GetVATLines()

    dayparam['VATTotals'] = [0,0,0]

    dayparam['offers'] = Ticket().GetOffers()

    for VATLine in dayparam['VATLines']:
        dayparam['VATTotals'][0] += VATLine[1]
        dayparam['VATTotals'][1] += VATLine[2]
        dayparam['VATTotals'][2] += VATLine[3]

    POSEquipment.TicketPrinter.PrintDayTotals(dayparam)

    if withClear: #afsluiten
        Ticket().ClearAll()
        WriteDayTotals(dayparam['VATLines'])

def PrintItemTotals():
    totals = Ticket().GetItemTotals()

    POSEquipment.TicketPrinter.PrintItemTotals(totals)
    
def WriteDayTotals(totals):
    conn = sqlite3.connect(ini.DB_NAME)
    cu = conn.cursor()
    
    for line in totals:
        cu.execute('insert into dayTotals (dateRegistered, vatCode, priceVatIn) values (?,?,?)',(datetime.now(), line[4],line[3]))
        
    conn.commit()