import sys
sys.path.append("c:\\BaronPOS")
import cherrypy
from DataModel.Ticket import Ticket
from ItemTotals import ItemTotals
from Charting import Charting

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


root = Root()
root.ItemTotals=ItemTotals()
root.DayTotal = DayTotal()
root.Charting = Charting()

userpassdict = {'dennis' : 'Marlboro001', }
checkpassword = cherrypy.lib.auth_basic.checkpassword_dict(userpassdict)
basic_auth = {'tools.auth_basic.on': True,
              'tools.auth_basic.realm': 'denbaron',
              'tools.auth_basic.checkpassword': checkpassword,
}
app_config = { '/' : basic_auth }

cherrypy.tree.mount(root,"",app_config)

cherrypy.server.start()
cherrypy.engine.start()
