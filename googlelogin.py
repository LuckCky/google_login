from googleapiclient.discovery import build
import json
import httplib2

try:
    from oauth2client.client import SignedJwtAssertionCredentials
except ImportError:
    from oauth2client.service_account import ServiceAccountCredentials

class AUTH:
    def __init__(self, json_key=json.load(open(r'path on your PC to your json file you generated earlier')),
                 scope_ga=['https://www.googleapis.com/auth/analytics.readonly'],
                 scope_gs=['https://spreadsheets.google.com/feeds']):
        self.json_key = json_key
        self.scope_ga = scope_ga
        self.scope_gs = scope_gs

    # call this function to login into Google Analytics if you got OAuth2client version < 2.0
    def ga_login(self, api_name='analytics', api_version='v3'):
        credentials = SignedJwtAssertionCredentials(self.json_key['client_email'], self.json_key['private_key'].encode(), self.scope_ga)
        http = credentials.authorize(httplib2.Http())
        service = build(api_name, api_version, http=http)
        return service

    # call this function to login into Google Spreadsheets if you got OAuth2client version < 2.0
    def gs_login(self):
        credentials = SignedJwtAssertionCredentials(self.json_key['client_email'], self.json_key['private_key'].encode(), self.scope_gs)
        return credentials

    # call this function to login into Google Analytics if you got OAuth2client version >= 2.0
    def ga_login_20(self, api_name='analytics', api_version='v3'):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.json_key, self.scope_ga)
        http = credentials.authorize(httplib2.Http())
        service = build(api_name, api_version, http=http)
        return service

    # call this function to login into Google Spreadsheets if you got OAuth2client version >= 2.0
    def gs_login_20(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.json_key, self.scope_ga)
        return credentials
