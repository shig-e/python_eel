
import requests

class RakutenAPI(object):
    def __init__(self, url:str,params:dict):
        self.url = url
        self.params = params
        
    def get_params(self, params):
        self.params = params
        return self.params
    
    def get_requests(self, url, params):
        self.req = requests.get(url, params=params)
        return self.req
    
    def check_header(self, req):
        if "json" in req.headers.get("Content-type"):
            items = req.json()
            return items
        else:
            items = req.text
            return True
