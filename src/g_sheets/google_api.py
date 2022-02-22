import pygsheets
import pandas as pd
import json
from string import ascii_uppercase as alphabet


class GoogleSheet():

    def __init__(self, spreadsheet_url):
        # Authorization
        self.client = pygsheets.authorize(service_file='googleAPICreds.json')
        self.spreadsheet_url = spreadsheet_url
        self.sheet = self.client.open_by_url(spreadsheet_url)

        # we should get this data from the API eventually 
        data = self.client.sheet.get('1WzZMRT4JSRIx1kRg44MbzunKjClnEeHIkLiarGyjuww')

    def export_to_sheet(self):
        # Create empty dataframe
        df = pd.DataFrame()

        # Create a column
        df = pd.read_json('meeting_data.json')

        #df.to_csv('meeting_data.csv')
        #print("\nInput CSV file = \n", df)

        #select the first sheet 
        wks = self.sheet[0]

        # update the first sheet with df, starting at cell B2. 
        wks.set_dataframe(df,(1,1))


    def update_headers(self, headers, page_number):
        wks = self.sheet[page_number]

        # Add all headers to first row of sheet 
        for i in range(len(headers)):
            header = wks.cell(alphabet[i] + '1') 
            header.value = headers[i]
            header.text_format['bold'] = True
            header.update()

    def add_participants(self, data, page_number):

        # Add the desired headers
        headers = ['Name', 'Join Time', 'Leave Time', 'Email', 'UUID']
        self.update_headers(headers, 1)

        # Specify page number to insert data
        wks = self.sheet[page_number]

        for i in range(len(data)):
            columns = 5
            data_dict = {0: 'name', 1: 'join_time', 2: 'leave_time', 3: 'user_email', 4: 'id'}
            # Starts from row 2 to fill A2-E2
            for j in range(columns):   
                cell = wks.cell(alphabet[j] + str(i + 2))
                key = data_dict[j]
                cell.value = data[i][key]
                cell.update()


            
if __name__ == '__main__':
    # Connect to specific sheet 
    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1WzZMRT4JSRIx1kRg44MbzunKjClnEeHIkLiarGyjuww/edit?usp=sharing'

    googleSheet = GoogleSheet(spreadsheet_url)

    # Rather than loading json file we will get participant data from API
    f = open('meeting_data.json')
    data = json.load(f)
    participants = data['participants']

    googleSheet.add_participants(participants, 1)