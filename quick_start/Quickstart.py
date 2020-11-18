from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
#my imports
# import time
# from datetime import datetime
# import pytz
from tabulate import tabulate
from prettytable import PrettyTable
from datetime import datetime, timedelta
from pprint import pprint

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    # now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    now_date = datetime.today()

    now_split = str(now_date). split(' ')
    now = now_split[0] + 'T' + now_split[1] + 'Z'
    
    # UTC = pytz.utc
    # now = pytz.timezone('Africa/Johannesburg')
    # print('---->', now)

    print('Getting the upcoming events for 7 days')
    events_result = service.events().list(calendarId='primary', timeMin=now, timeMax = (now_date + timedelta(days = 7)).isoformat() + 'Z',
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    my_file = open('Calender.txt', 'w')
    if not events:
        print('No upcoming events found.')
    # for x in range(0, 8):
    #     after_7_date = now_date + timedelta(x)
        # print('after_7----->', after_7_date)
    t = PrettyTable(['Date', 'Time', 'Event'])
        # after_7_split = str(after_7_date).split(' ')
        # print('a7s--------->', after_7_split[0])
    # pprint(service.calendarList().list().execute())
    for event in events:
        # max_date = after_7_split[0] + 'T' + after_7_split[1] + 'Z'
        start = event['start'].get('dateTime', event['start'].get('date'))
        # print('start------>', start)
        for x in range(0, len(start)):
            if start[x] == 'T':
                date = start[:x]
                time = start[x + 1: start.index('+')]

        t.add_row([date, time, event['summary']])
        my_file.write(start + event['summary']+'\n')
    # print(t)
    my_file.close()


if __name__ == '__main__':
    main()