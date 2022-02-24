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

def test_spreadsheet_url_not_none(sheet):
    actual = sheet.spreadsheet_url
    assert actual != None

def test_spreadsheet_title(sheet):
    actual = sheet.sheet.title
    expected = 'Zoomify'
    assert actual == expected

def test_spreadsheet_id(sheet):
    actual = sheet.sheet.id
    expected = '1WzZMRT4JSRIx1kRg44MbzunKjClnEeHIkLiarGyjuww'
    assert actual == expected

def test_add_participants(sheet):
    expected = ['Test1','Test2','Test3']
    sheet.update_headers(expected, 0)

    data = [
        {'name': 'test1', 'join_time': 'test-time', 'leave_time': 'test-time', 'user_email': 'test-email', 'id': 'test-id'},
        {'name': 'test2', 'join_time': 'test-time', 'leave_time': 'test-time', 'user_email': 'test-email', 'id': 'test-id'}
    ]
    sheet.add_participants(data, 0)
    expected = ['test1', 'test2']
    wks = sheet.sheet.worksheet(0)
    cell1 = wks.cell((2,1))
    cell2 = wks.cell((3,1))
    actual = [cell1.value, cell2.value]
    assert actual == expected

def test_add_participants_with_duplicates(sheet):
    data = [
        {'name': 'test1', 'join_time': 'test-time', 'leave_time': 'test-time', 'user_email': 'test-email', 'id': 'test-id'},
        {'name': 'test1', 'join_time': 'test-time', 'leave_time': 'test-time', 'user_email': 'test-email', 'id': 'test-id'}
    ]
    sheet.add_participants(data, 0)
    expected = ['test1', '']
    wks = sheet.sheet.worksheet(0)
    cell1 = wks.cell((2,1))
    cell2 = wks.cell((3,1))

    actual = [cell1.value, cell2.value]
    assert actual == expected












