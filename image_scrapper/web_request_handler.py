import requests

class WebRequestHandler:
    def __init__(self, requestUrl):
        self.requestUrl = requestUrl

    def getRequest(self):
        try:
            return requests.get(self.requestUrl)
        except Exception as e:
            print(str(e))
