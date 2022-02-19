import pygsheets
import pandas as pd
import json

# Authorization
client = pygsheets.authorize(service_file='testing/googleAPICreds.json')

# Connect to specific sheet 
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1WzZMRT4JSRIx1kRg44MbzunKjClnEeHIkLiarGyjuww/edit?usp=sharing'

data = client.sheet.get('1WzZMRT4JSRIx1kRg44MbzunKjClnEeHIkLiarGyjuww')
# Create empty dataframe
df = pd.DataFrame()

# open the google spreadsheet (by URL)
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1WzZMRT4JSRIx1kRg44MbzunKjClnEeHIkLiarGyjuww/edit?usp=sharing')

# Create a column
df['name'] = ['John', 'Steve', 'Sarah', 'Victor']

#select the first sheet 
wks = sheet[0]

# update the first sheet with df, starting at cell B2. 
wks.set_dataframe(df,(1,1))