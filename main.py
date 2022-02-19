








if __name__ == "__main__":
    
    # print(f"Zoom API Key: {ZOOM_API_KEY}")
    # print(f"Zoom API Secret: {ZOOM_API_SECRET}")
    # print(f"Zoom JWT: {ZOOM_JWT}")
    
    # Consider writing all logic for CLI input/output in another module and running it here

    
    # email = "joshua.david.huston@gmail.com"
    resp = zoom.get_meeting_reports(email)
    participants = zoom.get_meeting_participants(resp)
    print(participants)

    # Get all meeting participants using methods of the zoomify object


    # Do stuff with data from zoom (put into spreadsheet, display in terminal, send somewhere?)
    