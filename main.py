import os
from src.zoomify import Zoomify
from requests import Response
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Pull in environment variables
# We can use a setup script to source these env variables or use another tool to pull them from
#   a .env file. 

ZOOM_API_KEY = os.environ.get("ZOOM_API_KEY")
ZOOM_API_SECRET = os.environ.get("ZOOM_API_SECRET")
ZOOM_JWT = os.environ.get("ZOOM_JWT")
ZOOM_MEETING_ID = os.environ.get("ZOOM_MEETING_ID")



if __name__ == "__main__":
    
    print(f"Zoom API Key: {ZOOM_API_KEY}")
    print(f"Zoom API Secret: {ZOOM_API_SECRET}")
    print(f"Zoom JWT: {ZOOM_JWT}")
    
    # Consider writing all logic for CLI input/output in another module and running it here

    # Instantiate Zoomify object
    zoom = Zoomify(ZOOM_API_KEY, ZOOM_API_SECRET, ZOOM_JWT)
    email = "joshua.david.huston@gmail.com"
    resp = zoom.get_meeting_reports(email)
    print(resp)
    participants = zoom.get_meeting_participants(resp)
    print(participants)

    # Get all meeting participants using methods of the zoomify object


    # Do stuff with data from zoom (put into spreadsheet, display in terminal, send somewhere?)
    