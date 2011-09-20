'''
Created on 20-sep.-2011

@author: dennis
'''
import cherrypy
import cairoplot
import cairo
import StringIO

class Charting(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    @cherrypy.expose
    def GetTotalChart(self,**args):
        cherrypy.response.headers['Content-Type']= 'image/png'
        
        surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, 600, 800)
        
        print args
        data = {}
        for k, v in args.items():
            data[k]=int(v)
        
        pc = cairoplot.PiePlot(surf,data, gradient=True,shadow=True)
        pc.render()
        response=StringIO.StringIO()
        pc.surface.write_to_png(response)

        return response.getvalue()

        