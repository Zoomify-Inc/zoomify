import os
import pytest
from src.zoomify import Zoomify
import requests
from dotenv import load_dotenv
from datetime import datetime
import builtins

@pytest.fixture
def zoomify():
  load_dotenv()
  ZOOM_API_KEY = os.environ.get("ZOOM_API_KEY")
  ZOOM_API_SECRET = os.environ.get("ZOOM_API_SECRET")
  ZOOM_JWT = os.environ.get("ZOOM_JWT")
  zoom = Zoomify(ZOOM_API_KEY, ZOOM_API_SECRET, ZOOM_JWT)
  return zoom

def test_meeting_report(zoomify):
  inputs = [0]
  def mock_input(*args):
    return inputs.pop(0)
  real_input = builtins.input
  builtins.input = mock_input
  mtg_obj = zoomify.get_meeting_reports('joshua.david.huston@gmail.com')
  actual = mtg_obj
  expected = "S04FR9NfQ3S4M43QZ+isPQ=="
  assert expected == actual
  builtins.input = real_input

def test_meeting_participants(zoomify):
  inputs = [0]
  def mock_input(*args):
    return inputs.pop(0)
  real_input = builtins.input
  builtins.input = mock_input
  mtg_obj = zoomify.get_meeting_reports('joshua.david.huston@gmail.com')
  actual = zoomify.get_meeting_participants(mtg_obj)
  expected = ['Joshua Huston', 'Isaiah Burkes']
  assert expected == actual
  builtins.input = real_input


# def test_format_meetings(zoomify):
#   inputs = [0]
#   def mock_input(*args):
#     return inputs.pop(0)
#   real_input = builtins.input
#   builtins.input = mock_input
#   mtg_obj = zoomify.get_meeting_reports('joshua.david.huston@gmail.com')
#   print(mtg_obj)
#   formatted_mtg = zoomify.format_meetings(mtg_obj)
#   print(formatted_mtg)
#   # actual = formatted_mtg
#   # # expected = "S04FR9NfQ3S4M43QZ+isPQ=="
#   # assert expected == actual
#   builtins.input = real_input
#   assert actual == expected









