from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# from oauth2client import file, client, tools 

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def google_calendar_service():
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
    return service 

def get_google_calendar_events(n, service):
    """
        return eventlist
    """
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    # print(f'Getting the upcoming {n} events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    eventList = []
    for event in events:

        #original 
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))

        #get date thoi
        # start = event['start'].get('date', event['start'].get('date'))
        # end = event['end'].get('date', event['end'].get('date'))
        #day moi la cai date  
        # print(start[0: 10])
        # print(start, "_______", end, event['summary'])
       
        
        # [start[0:4], start[5:7], start[6:9]]
        # eventList.append([start[0:10], end[0:10], event['summary']]) 

        # eventList.append([start, end, event['summary']])

        eventList.append([[start[0:4], start[5:7], start[8:10]], [end[0:4], end[5:7], end[8:10]], event['summary']])

    return eventList 


# if __name__ == '__main__':
#     main()


# def 


# [['2020', '11', '14'], ['2020', '11', '14'], 'đi chơi gái ']
# [['2020', '11', '14'], ['2020', '11', '14'], 'đi ngủ ']
# [['2020', '11', '15'], ['2020', '11', '15'], 'đánh răng']


# service = google_calendar_service() 

# eventList = get_google_calendar_events(2, service)
# # for event in eventList:
#     # print(event)


# event = {
#     'summary': 'Google I/O 2015',
#     'location': 'Viet Nam',
#     'description': 'test event thoi ma hahaa',
#     'start': {
#         'dateTime': '2020-11-15T07:30:00+07:00',
#         'timeZone': 'Asia/Bangkok',
#     },
#     'end': {
#         'dateTime': '2020-11-15T08:30:00+07:00',
#         'timeZone': 'Asia/Bangkok',
#     },
#     'recurrence': [
#         'RRULE:FREQ=DAILY;COUNT=2'
#     ],
#     'attendees': [
#         {'email': 'thaison111299@gmail.com'}
#     ],
#     'reminders': {
#         'useDefault': False,
#         'overrides': [
#             {'method': 'email', 'minutes': 24 * 60},
#             {'method': 'popup', 'minutes': 10},
#         ],
#     },
# }

# event = service.events().insert(calendarId='primary', body=event).execute()

# # print ('Event created: %s' % (event.get('htmlLink')))  
