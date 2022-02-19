from authlib.jose import jwt
import requests
from requests import Response
from datetime import date, datetime


class Zoomify:

    def __init__(self, API_KEY, API_SECRET, JWT):
        # Init instance variables such as api_key, api_secret, api base url, jwt token expiration, jwt algo
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET
        self.JWT = JWT
        self.base_url = "https://api.zoom.us/v2"
        self.reports_url = f"{self.base_url}/report/meetings"
        self.users_url = f"{self.base_url}/report/users"


    def get_meeting_reports(self, email):
        url = f"{self.users_url}/{email}/meetings"        
        now = datetime.now()
        # Here we will had to add an option of how far back we go checking meetings
        query_params = {
                "from": "2018-09-13",
                "to": str(now.strftime("%Y-%m-%d")),
                "page_size": 30,
            }
        r = (requests.get(url, headers={"Authorization": f"Bearer {self.JWT}"},
        params=query_params)).json()
        
        meetings = [print(i['id'], i['start_time']) for i in r['meetings']]
        print(meetings)

        # Allow user to select the meeting to display information
        user_selection = input('Type in the meeting ID you would like to select: ')
        return str(user_selection)
        

        
        
    # Here is where we use the Zoom API do get all the participants of an ongoing zoom meeting
    def get_meeting_participants(self, meeting_id):
        url = f"{self.reports_url}/{meeting_id}/participants"
        query_params = {
            "page_size": 30
        }
        r = (requests.get(url, headers={"Authorization": f"Bearer {self.JWT}"}, 
        params=query_params)).json()

        # participants still not removing duplicates
        participants = []
        [participants.append(p["name"]) for p in r["participants"] if p not in participants]
        return participants

    def get_jwt_token(self):
        pass
        # Generate a JWT using authlib library