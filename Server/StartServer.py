import os
from BaronPOSServer import BaronPOSServer

__author__ = 'dennis'

server = BaronPOSServer((os.getenv('COMPUTERNAME'), 8000))
server.serve_forever()
