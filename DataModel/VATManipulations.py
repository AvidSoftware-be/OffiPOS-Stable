from DataModel.Ticket import Ticket
import POSEquipment

__author__ = 'dennis'

def DoEndOfDay():
    dayparam['firstOrder'] = Ticket().GetFirstOrderDate()
    dayparam['lastOrder'] = Ticket().GetLastOrderDate()
    dayparam['payedAmts']['Cash'] = 0
    dayparam['payedAmts']['Atos'] = 0
    dayparam['VATLines'] = []

    dayparam['VATLines'].append(["21,00%","00.00","00.00","00.00"])
    dayparam['VATLines'].append(["12,00%","00.00","00.00","00.00"])
    dayparam['VATLines'].append([" 6,00%","00.00","00.00","00.00"])

    dayparam['VATLines']['totals']=["00.00","00.00","00.00"]

    POSEquipment.TicketPrinter.PrintDayTotals(dayparam)
  