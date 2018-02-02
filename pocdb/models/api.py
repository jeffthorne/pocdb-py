"""
Created on Nov 3 2014
@author: Jeff Thorne
"""

import json
from typing import List, Dict
import sys
import urllib3


import requests
from requests.auth import HTTPBasicAuth

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
headers = {'Content-Type': 'application/json'}
host = "https://pocdb.com"

class API:

    def __init__(self, email: str, password: str, api_version:str = 'v1'):
        self.api_version = api_version
        self.verify = True

        try:
            self.auth_token = self.__authenticate(email, password)
            if self.auth_token is not None:
                print("Authentication successful")
            else:
                print("Authentication failure")
                sys.exit()


        except Exception as ex:
            print("Authentication error: ", ex)
            sys.exit()




    def __authenticate(self, email:str, password:str) -> bool:
        url = "{}/api/{}/login".format(host, self.api_version)
        data = dict(email=email, password=password)
        json_response = json.loads(requests.post(url, data=json.dumps(data), verify=self.verify, headers=headers).content)

        if 'error' in json_response:
            return None
        else:
            auth_token = json_response['token'] if 'token' in json_response else None
            return auth_token



    def pocs(self, region: str) -> List[str]:
        url = "{}/api/{}/pocs".format(host, self.api_version)
        data = dict(region=region)
        response = requests.post(url, data=json.dumps(data), verify=self.verify, headers=headers, auth=HTTPBasicAuth(self.auth_token, ''))
        json_response = json.loads(response.content)
        return json_response

    def salesreps(self) -> List[str]:
        url = "{}/api/{}/salesreps".format(host, self.api_version)
        response = requests.get(url, verify=self.verify, headers=headers, auth=HTTPBasicAuth(self.auth_token, ''))
        return json.loads(response.content)


    def pocs_by_product(self, product: str, region:str = 'all') -> List[str]:
        url = "{}/api/{}/pocs/product".format(host, self.api_version)
        data = dict(product=product, region=region)
        response = requests.post(url, data=json.dumps(data), verify=self.verify, headers=headers, auth=HTTPBasicAuth(self.auth_token, ''))
        json_response = json.loads(response.content)
        return json_response

