from Server.BaronPOSServer import BaronPOSServer

__author__ = 'dennis'

server = BaronPOSServer(("localhost", 8000))
server.serve_forever()