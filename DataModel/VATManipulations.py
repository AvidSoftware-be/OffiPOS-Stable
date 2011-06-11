from DataModel.Ticket import Ticket
import POSEquipment

__author__ = 'dennis'

def DoEndOfDay():
    dayparam ={'firstOrder' : Ticket().GetFirstOrderDate(),'lastOrder' : Ticket().GetLastOrderDate()}
    dayparam['payedAmts'] = {'Cash': 0, 'Atos': 0}
    dayparam['VATLines'] = (("21,00%", "00.00", "00.00", "00.00"),
                            ("12,00%", "00.00", "00.00", "00.00"),
                            (" 6,00%", "00.00", "00.00", "00.00"))

    dayparam['VATTotals'] = ("00.00", "00.00", "00.00")

    POSEquipment.TicketPrinter.PrintDayTotals(dayparam)
  