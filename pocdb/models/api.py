"""
Created on Nov 3 2014
@author: Jeff Thorne
"""

import json
from datetime import datetime
import time
from typing import List, Dict
import urllib3
import ssl
import sys
import logging

import requests
from requests.auth import HTTPBasicAuth


headers = {'Content-Type': 'application/json'}
host = "http://127.0.0.1:5000"

class API:

    def __init__(self, email: str, password: str, api_version: str):
        self.api_version = api_version

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
        json_response = json.loads(requests.post(url, data=json.dumps(data), verify=False, headers=headers).content)

        if 'error' in json_response:
            return None
        else:
            auth_token = json_response['token'] if 'token' in json_response else None
            return auth_token



    def pocs_by_region(self, region: str) -> List[str]:
        url = "{}/api/{}/pocs".format(host, self.api_version)
        data = dict(region=region)
        response = requests.post(url, data=json.dumps(data), verify=False, headers=headers, auth=HTTPBasicAuth(self.auth_token, ''))
        json_response = json.loads(response.content)
        print(json_response)
        return json_response
