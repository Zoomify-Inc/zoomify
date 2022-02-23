import pytest
from src.g_sheets.google_api import GoogleSheet


# Fixture to provide a Setup, GoogleSheet, and Tear Down
@pytest.fixture
def sheet():
    # SETUP
    url = 'https://docs.google.com/spreadsheets/d/1WzZMRT4JSRIx1kRg44MbzunKjClnEeHIkLiarGyjuww/edit?usp=sharing'
    sheet = GoogleSheet(url)

    # YIELD SHEET
    yield sheet

    # TEARDOWN
    wks = sheet.sheet.worksheet(0)
    wks.clear(fields='*')


def test_constructor(sheet):
    assert sheet != None

def test_spreadsheet_url(sheet):
    expected = 'https://docs.google.com/spreadsheets/d/1WzZMRT4JSRIx1kRg44MbzunKjClnEeHIkLiarGyjuww/edit?usp=sharing'
    actual = sheet.spreadsheet_url
    assert expected == actual

def test_update_headers(sheet):
    headers = ['Test1','Test2','Test3']
    sheet.update_headers(headers, 0)









