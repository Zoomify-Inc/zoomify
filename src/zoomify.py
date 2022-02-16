from authlib.jose import jwt
import requests
from requests import Response


class Zoomify:

    def __init__(self, API_KEY, API_SECRET):
        # Init instance variables such as api_key, api_secret, api base url, jwt token expiration, jwt algo
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET

    def get_meeting_participants(self):
        pass
        # Here is where we use the Zoom API do get all the participants of an ongoing zoom meeting

    def get_jwt_token(self):
        pass
        # Generate a JWT using authlib library