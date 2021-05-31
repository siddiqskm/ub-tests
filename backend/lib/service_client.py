import json
from requests import Session


class ServiceClient():
    def __init__(self, url):
        """
        Constructor
        """
        self.url = url
        self.session = Session()
        self.headers = {'content-type': 'application/json'}

    def post(self, payload):
        """
        POST Request
        """
        print("Payload is: %s" % payload)
        return self.session.post(url=self.url, data=payload, headers=self.headers)
