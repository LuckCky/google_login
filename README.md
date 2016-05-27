# google_login
Tired of not working Google Authorisation for your requests?
This module is what you need!
Helps you to login into Google Analytics or Google Spreadsheets

Also needed modules:
1. Google API. To install: pip install --upgrade google-api-python-client
2. json
3. httplib2
4. oauth2client - any version (hopefully) will do, so you san keep using your favorite version without upgrading

To work with Google Spreadsheets I recommend gspread (https://github.com/burnash/gspread)

First you need to make some preparations.
How to obtain OAuth2 credentials from Google Developers Console:
1. Head to Google Developers Console and create a new project (or select the one you have.)
2. 
2. Under “API & auth”, in the API enable "Analytics API" and "Drive API"
3. 
3. Go to “Credentials” and choose “New Credentials > Service Account Key”
4. 
4. You will automatically download a JSON file with this data. Store it somewhere safe, you'll need path to it later
