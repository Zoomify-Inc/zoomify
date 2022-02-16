import os
from src.zoomify import Zoomify
from requests import Response



# Pull in environment variables
# We can use a setup script to source these env variables or use another tool to pull them from
#   a .env file. 
ZOOM_API_KEY = os.environ.get("ZOOM_API_KEY")
ZOOM_API_SECRET = os.environ.get("ZOOM_API_SECRET")
ZOOM_MEETING_ID = os.environ.get("ZOOM_MEETING_ID")



if __name__ == "main":
    pass
    # Consider writing all logic for CLI input/output in another module and running it here

    # Instantiate Zoomify object


    # Get all meeting participants using methods of the zoomify object


    # Do stuff with data from zoom (put into spreadsheet, display in terminal, send somewhere?)
    