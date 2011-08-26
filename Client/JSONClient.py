__author__ = 'dennis'

import urllib2,uuid,json,thread,base64

class Proxy():
    def __init__(self, service_url, auth_user = None, auth_password = None):
        self.service_url = service_url
        self.auth_user = auth_user
        self.auth_password = auth_password

    def call(self, method, params=None, success=None, failure=None):
        thread.start_new_thread(self._call,(method, params, success, failure))

    def _call(self, method, params=None, success=None, failure=None):
        try:
            id = str(uuid.uuid1())
            data = json.dumps({'method':method, 'params':params, 'id':id})
            req = urllib2.Request(self.service_url + '/' +method)
            if self.auth_user != None and self.auth_password != None:
                authString = base64.encodestring('%s:%s' % (self.auth_user, self.auth_password))[:-1]
                req.add_header("Authorization", "Basic %s" % authString)
            req.add_header("Content-type", "application/json")
            #f = urllib2.urlopen(req, data)
            f = urllib2.urlopen(req)
            response = f.read()
            data = json.loads(response)
        except IOError, (strerror):
            data = dict(result=None,error=dict(message='Network error. ' + str(strerror),code=None,data=None), id=id)
        except ValueError, (strerror):
            data = dict(result=None,error=dict(message='JSON format error. ' + str(strerror),code=None,data=None), id=id)

        if data.has_key('error') and data["error"] != None:# ZF workaround
            data['result'] = None
            if data['error'] != None and failure != None:
                failure(data['error'])
                return data
        else:
            data['error'] = None
        if success != None:
            success(data['result'])
        return data

#if __name__ == "__main__":
#    def onResult(result):
#        print 'success :-) : ' + str(result)
#
#    def onError(error):
#        print 'failure :-( : ' + error['message']
#
#    service = Proxy('http://www.desfrenes.com/service/hello')
#    #service = Proxy('http://apps.shozu.int/rpc/index/json/hello', 'admin', 'admin')
#
#    # threaded call with callbacks
#    #service.call('hello',{'name':'John Doe'},onResult,onError)
#
#    # non-threaded call with returned result
#    #result = service._call('ping',['John Doe'])
#    result = service._call('hello',{'name':'John Doe'})
#    print result
#
#    #while 1:pass