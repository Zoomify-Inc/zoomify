import pygsheets
from string import ascii_uppercase as alphabet


class GoogleSheet():

    def __init__(self, spreadsheet_url):
        # Authorization
        self.client = pygsheets.authorize(service_account_file='googleAPICreds.json')
        self.spreadsheet_url = spreadsheet_url
        self.sheet = self.client.open_by_url(spreadsheet_url)

        # we should get this data from the API eventually 
        data = self.client.sheet.get('1WzZMRT4JSRIx1kRg44MbzunKjClnEeHIkLiarGyjuww')

 
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
        self.update_headers(headers, page_number)

        # Specify page number to insert data
        wks = self.sheet[page_number]

        seen = set()
        iteration_count = row_index = 0
        while iteration_count < len(data):
            if data[iteration_count]['name'] in seen:
                iteration_count += 1
                continue
            else:
                seen.add(data[iteration_count]['name'])

            columns = 5
            data_dict = {0: 'name', 1: 'join_time', 2: 'leave_time', 3: 'user_email', 4: 'id'}

            for j in range(columns):   
                cell = wks.cell(alphabet[j] + str(row_index + 2))
                key = data_dict[j]
                cell.value = data[iteration_count][key]
        
            iteration_count += 1
            row_index += 1

        # Identify start and end of cell range   
        start_cell = 'A2'
        end_cell = 'E' + str(len(seen) + 1)
        cell_range = wks.range('%s:%s' % (start_cell, end_cell))
        
        # Batch updates so there is only one update request sent
        all_updates = []
        for row in cell_range:
            all_updates += row
        
        # Send update request
        wks.update_cells(all_updates)
