from Server.SimpleJSONRPCServer import SimpleJSONRPCServer
from DataModel.Ticket import paymentMethods
from DataModel.Ticket import Ticket

__author__ = 'dennis'

class BaronPOSServer(SimpleJSONRPCServer):
    def _dispatch(self, method, params):
        try:
            # We are forcing the 'export_' prefix on methods that are
            # callable through JSON-RPC to prevent potential security
            # problems
            func = getattr(self, 'export_' + method)
        except AttributeError:
            raise Exception('method "%s" is not supported' % method)
        else:
            return func(*params)

    def export_getDayTotal(self, param):
        total = 0
        try:
            total = Ticket().GetPaymentTotal(paymentMethods['Cash'])
            total += Ticket().GetPaymentTotal(paymentMethods['Atos'])
        except:
            if not total:
                total = 0

        return total

    def export_getItemTotals(self, param):
        return Ticket().GetItemTotals()
