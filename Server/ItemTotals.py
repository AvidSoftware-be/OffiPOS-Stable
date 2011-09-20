import cherrypy
import sys
from datetime import datetime
sys.path.append("c:\\BaronPOS")
from DataModel.Ticket import Ticket

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
               '<head>'+\
               '<style type="text/css">'+\
"""table.gridtable {
    font-family: verdana,arial,sans-serif;
    font-size:11px;
    color:#333333;
    border-width: 1px;
    border-color: #666666;
    border-collapse: collapse;
}
table.gridtable th {
    border-width: 1px;
    padding: 4px;
    border-style: solid;
    border-color: #666666;
    background-color: #dedede;
}
table.gridtable td {
    border-width: 1px;
    padding: 3px;
    border-style: solid;
    border-color: #666666;
    background-color: #ffffff;
}
table.gridtable td.total {
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #666666;
    background-color: #F5BCA9;
    font-weight:bold;
    }
table.gridtable td.grandtotal {
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #666666;
    background-color: #FA8258;
    font-weight:bold;
    }
body {
    font-family: verdana,arial,sans-serif;
    font-size:11px;
    }
</style>"""+\
               '<title>Item Totals</title>'+\
               '</head><body>'
        body += '<table class="gridtable">'
        chartData = {}
        for line in totals:
            body += '<tr><th colspan="4">{0:<}</th></tr>'.format(line[1]) #groepnaam
            itemQtyTotal = 0
            amountTotal = 0
            for itemLine in line[2]:
                body += '<tr><td>{0[0]:>3.0f}</td><td>{0[1]:>4d}</td><td>{0[2]:<21}</td><td align="right">{0[3]:>10.2f}</td></tr>'.format(
                    itemLine) #artikel
                itemQtyTotal += itemLine[0]
                amountTotal += itemLine[3]
                grandTotAmt += itemLine[3]

            body += '<tr><td class="total">{0:>.0f}</td><td colspan="3" align="right" class="total">{1:>.2f}</td></tr>'.format(itemQtyTotal,
                                                                                                   amountTotal) #totalen
            chartData[line[1]]=amountTotal

        body += '<tr><td colspan="4" align="right" class="grandtotal">{0:>.2f}</td></tr>'.format(grandTotAmt) #totalen
        
        params=[]
        for k, v in chartData.items():
            params.append("{0:>s}={1:.0f}".format(k.replace(" ","%20"),v))
            
        paramstr = "&".join(params)
        
        body += '<tr><td colspan="4" align="right"><img src="/Charting/GetTotalChart/?{0:>s}"></td></tr>'.format(paramstr) #chart

        body += '</table>'
        body += 'Gemaakt op {0:>s} om {1:>s}'.format(datetime.now().strftime('%d/%m/%Y'),
                                                                        datetime.now().strftime(
                                                                            '%H:%M'))
        body += '</body></html>'
        return body