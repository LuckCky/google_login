import json
import httplib2
from googleapiclient.discovery import build

class auth:
    def __init__(self, json_key=json.load(open(r'C:\Users\User\Desktop\GA_everyday\My Project-ae8911df83b1.json'))):
        self.json_key = json_key
        self.scope_ga = ['https://www.googleapis.com/auth/analytics.readonly']
        self.scope_gs = ['https://spreadsheets.google.com/feeds']

    def ga_login(self, api_name='analytics', api_version='v3'):
        try:
            from oauth2client.client import SignedJwtAssertionCredentials
            credentials = SignedJwtAssertionCredentials(self.json_key['client_email'], self.json_key['private_key'].encode(), self.scope_ga)
            http = credentials.authorize(httplib2.Http())
            service = build(api_name, api_version, http=http)
        except ImportError:
            from oauth2client.service_account import ServiceAccountCredentials
            credentials = ServiceAccountCredentials.from_json_keyfile_name(self.json_key, self.scope_ga)
            http = credentials.authorize(httplib2.Http())
            service = build(api_name, api_version, http=http)
        return service

    def gs_login(self):
        try:
            from oauth2client.client import SignedJwtAssertionCredentials
            credentials = SignedJwtAssertionCredentials(self.json_key['client_email'], self.json_key['private_key'].encode(), self.scope_gs)
        except ImportError:
            from oauth2client.service_account import ServiceAccountCredentials
            credentials = ServiceAccountCredentials.from_json_keyfile_name(self.json_key, self.scope_ga)
        return credentials
