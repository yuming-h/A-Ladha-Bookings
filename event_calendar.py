from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime


def format_datetime(datetime):
    yr = str(datetime.year)
    month = str(datetime.month)
    day = str(datetime.day)
    hour = str(datetime.hour)
    minute = str(datetime.minute)
    if len(month) < 2:
        month = '0'+month
    if len(day) < 2:
        day = '0'+day
    if len(hour) < 2:
        hour = '0'+hour
    if len(minute) < 2:
        minute = '0'+minute
    return yr+'-'+month+'-'+day+'T'+hour+':'+minute+':00-07:00'

class EventCalendar:

    def __init__(self, responseObj):
        self.response = responseObj

    def update_calendar(self):

        SCOPES = 'https://www.googleapis.com/auth/calendar'
        store = file.Storage('cal_credential.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('calendar', 'v3', http=creds.authorize(Http()))

        event = {
          'summary': self.response.org + ' - ' + self.response.event_name,
          'start': {'dateTime': format_datetime(self.response.start_datetime)},
          'end': {'dateTime': format_datetime(self.response.end_datetime) },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
