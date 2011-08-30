import os
import sys
sys.path.append("c:\\BaronPOS")
import cherrypy
from DataModel.Ticket import Ticket

cherrypy.config.update({"server.socket_port": 8000, "server.socket_host":"0.0.0.0"})

class Root(object):
    @cherrypy.expose
    def index(self):
        return '''
            <p>Hi, this is the home page!</p>>'''


class DayTotal:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def json(self):
        return (Ticket().GetTotalAmt(True),)


class ItemTotals:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def json(self):
        return Ticket().GetItemTotals()

    @cherrypy.expose
    def html(self):
        totals = Ticket().GetItemTotals()
        grandTotAmt = 0
        body = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" ' +\
               '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">' +\
               '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"> '+\
               '<head><title>Item Totals</title></head><body>'
        body += '<table>'
        for line in totals:
            body += '<tr><td colspan="4">{0:<}</td></tr>'.format(line[1]) #groepnaam
            itemQtyTotal = 0
            amountTotal = 0
            for itemLine in line[2]:
                body += '<tr><td>{0[0]:>3.0f}</td><td>{0[1]:>4d}</td><td>{0[2]:<21}</td><td align="right">{0[3]:>10.2f}</td></tr>'.format(
                    itemLine) #artikel
                itemQtyTotal += itemLine[0]
                amountTotal += itemLine[3]
                grandTotAmt += itemLine[3]

            body += '<tr><td>{0:>.0f}</td><td colspan="3" align="right">{1:>.2f}</td></tr>'.format(itemQtyTotal,
                                                                                                   amountTotal) #totalen

        body += '<tr><td colspan="4" align="right">{0:>.2f}</td></tr>'.format(grandTotAmt) #totalen

        body += '</table></body></html>'
        return body

root = Root()
root.ItemTotals=ItemTotals()
root.DayTotal = DayTotal()
cherrypy.quickstart(root)
