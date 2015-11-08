import requests
__author__ = 'Lei Yu'
# connection wrapper

class Error(Exception):
    def __init__(self,message):
        self.message=message

    def __str__(self):
        return repr(self.message)

class Connection:

    def __init__(self,host="api.coursera.org/api",version="catalog.v1"):
        self.host=host
        self.version=version

    def get(self,path):
        return self._do_call(path,"GET")

    def _do_call(self,path,method):
        url='https://{0}/{1}{2}'.format(self.host,self.version,path)
        response=requests.request(method,url)
        if(response.status_code==requests.codes.ok):
            json_body=response.json()
            return json_body
        raise Error(response.json())
    



   
        
        









