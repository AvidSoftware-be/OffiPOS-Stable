import cherrypy
import cairoplot
import cairo
import StringIO

class Charting(object):
    
    @cherrypy.expose
    def GetTotalChart(self, **args):
        width=320
        height=200
        cherrypy.response.headers['Content-Type'] = 'image/png'
        
        surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, height, width)
        data = {}
        for k, v in args.items():
            data[k] = int(v)
        
        pc = cairoplot.PiePlot(surf, data, width, height, gradient=True, shadow=True)
        pc.render()
        response = StringIO.StringIO()
        pc.surface.write_to_png(response)

        return response.getvalue()
    
    @cherrypy.expose
    def GetTimedChart(self):
        width=320
        height=200
        
        cherrypy.response.headers['Content-Type'] = 'image/png'
        
        surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, height, width)
        
        pc = cairoplot.DotLinePlot(surf, data, width, height, dots=False)
        pc.render()
        response = StringIO.StringIO()
        pc.surface.write_to_png(response)

        return response.getvalue()
        
