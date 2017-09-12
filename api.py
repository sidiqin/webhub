# from future import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1BiQNcXnnVPNhCLRRuNaYcw76-R85QG8g5DlbJWzXI_I' #input spreadsheet id
    rangeName =  '22/8!A:N' #input range
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    shareholders = {}

    if not values:
        print('No data found.')
    else:
        for row in values:

            date = row[0]
            stock = row[1]
            shareholder = row[2]
            num_of_share = row[6]
            price = row[8]
            bal = row[11]

        
            date = date.split("\n")[1].replace("(","").replace(")","")
            shareholder = shareholder.split("[")[0].rstrip()
            num_of_share = float(num_of_share.replace(",",""))
            price = float(price)
            bal = bal.replace(",","")
            if not bal:
                bal=0

            bal=float(bal)

            if shareholder not in shareholders:
                 shareholders[shareholder]=[]
                 shareholders[shareholder].append([date, stock, price, num_of_share, bal])
            else:
                 shareholders[shareholder].append([date, stock, price, num_of_share, bal])
           

            for shareholder in shareholders:
                 print shareholder
                 print
                 for s in shareholders[shareholder]:
                    print s

                 print



if __name__ == '__main__':
    main()