from authlib.jose import jwt
import requests
from requests import Response


class Zoomify:

    def __init__(self, API_KEY, API_SECRET, JWT):
        # Init instance variables such as api_key, api_secret, api base url, jwt token expiration, jwt algo
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET
        self.JWT = JWT
        self.base_url = "https://api.zoom.us/v2"
        self.reports_url = f"{self.base_url}/report/meetings"
        self.users_url = f"{self.base_url}/report/users"


    # Test route using my JWT, and a known meeting ID
    # Report > meetings > meetingID
    # {{baseUrl}}/report/meetings/:meetingId/participants?page_size=30
    # Report >  users > userID > Meetings
    # {{baseUrl}}/report/users/:userId/meetings?from=2018-09-13&to=2022-02-19&page_size=30
    def get_meeting_reports(self, email):
        url = f"{self.users_url}/{email}/meetings"
        print(url)
        

        # Here we will had to add an option of how far back we go checking meetings
        query_params = {
                "from": "2018-09-13",
                "to": "2022-02-19",
                "page_size": 30,
            }

        r = (requests.get(url, headers={"Authorization": f"Bearer {self.JWT}"},
        params=query_params)).json()
        
        # return r
        return r['meetings'][0]['id']

        
        
    # Here is where we use the Zoom API do get all the participants of an ongoing zoom meeting
    def get_meeting_participants(self, meeting_id):
        url = f"{self.reports_url}/{meeting_id}/participants"
        query_params = {
            "page_size": 30
        }
        r = (requests.get(url, headers={"Authorization": f"Bearer {self.JWT}"}, 
        params=query_params)).json()

        participants = []
        for p in r["ps"]:
            participants.append(p["name"])
        return participants


    def get_jwt_token(self):
        pass
        # Generate a JWT using authlib library