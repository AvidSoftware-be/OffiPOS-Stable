import cherrypy
from DataModel.Ticket import Ticket

class Root(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getrange(self, limit=4):
        return list(range(int(limit)))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getTest(self):
        return Ticket().GetItemTotals()

cherrypy.quickstart(Root())