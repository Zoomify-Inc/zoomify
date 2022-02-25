from cmath import exp
import imp
import pytest 
from menu import Menu
from colorama import Fore, Back, Style
import pyfiglet
import builtins
import difflib

# Multiple Lines for the test were taken from the game of greed flo.py file to get a way to test
def test_welcome():
    inputs = ['e']
    text = ''

    def mock_input(*args):
        return inputs.pop(0)
    # store the "real" print & input so we can restore them later
    real_input = builtins.input
    # mock the built in print & input
    builtins.input = mock_input

    def mock_print(*args):
        nonlocal text
        text += "".join(args) + "\n"
    real_print = builtins.print
    # mock the built in print & input
    builtins.print = mock_print
    menu = Menu()

    try:
      menu.get_env_vars()
      menu.welcome()
      menu.welcome_menu()
    except SystemExit:
        real_print("Exiting is allowed")
    expected_lines = parse_expected_lines(path='tests/exit_menu_sim.txt', sample='')
    diff = find_differences(text, expected_lines)
    assert diff != None

def test_email_and_exit():
    inputs = ['l', 'idkburkes@gmail.com', '0', 'e']
    text = ''

    def mock_input(*args):
        return inputs.pop(0)
    # store the "real" print & input so we can restore them later
    real_input = builtins.input
    # mock the built in print & input
    builtins.input = mock_input

    def mock_print(*args):
        nonlocal text
        text += "".join(args) + "\n"
    real_print = builtins.print
    # mock the built in print & input
    builtins.print = mock_print
    menu = Menu()

    try:
      menu.get_env_vars()
      menu.welcome()
      menu.welcome_menu()
    except SystemExit:
        real_print("Exiting is allowed")
    expected_lines = parse_expected_lines(path='tests/login_and_exit.txt', sample='')
    diff = find_differences(text, expected_lines)
    assert diff != None

def test_sheet_export():
    inputs = ['l', 'idkburkes@gmail.com', '0', 'r', '19', 'g','e']
    text = ''

    def mock_input(*args):
        return inputs.pop(0)
    # store the "real" print & input so we can restore them later
    real_input = builtins.input
    # mock the built in print & input
    builtins.input = mock_input

    def mock_print(*args):
        nonlocal text
        text += "".join(args) + "\n"
    real_print = builtins.print
    # mock the built in print & input
    builtins.print = mock_print
    menu = Menu()

    try:
      menu.get_env_vars()
      menu.welcome()
      menu.welcome_menu()
    except SystemExit:
        real_print("Exiting is allowed")
    expected_lines = parse_expected_lines(path='tests/login_report_sheets_sim.txt', sample='')
    diff = find_differences(text, expected_lines)
    assert diff != None

def test_attendance_report():
    inputs = ['l', 'idkburkes@gmail.com', '0', 'r', '19','e']
    text = ''

    def mock_input(*args):
        return inputs.pop(0)
    # store the "real" print & input so we can restore them later
    real_input = builtins.input
    # mock the built in print & input
    builtins.input = mock_input

    def mock_print(*args):
        nonlocal text
        text += "".join(args) + "\n"
    real_print = builtins.print
    # mock the built in print & input
    builtins.print = mock_print
    menu = Menu()

    try:
      menu.get_env_vars()
      menu.welcome()
      menu.welcome_menu()
    except SystemExit:
        real_print("Exiting is allowed")
    expected_lines = parse_expected_lines(path='tests/login_report_sheets_sim.txt', sample='')
    diff = find_differences(text, expected_lines)
    assert diff != None




def find_differences(text, expected_lines):
    actual_lines = text.splitlines()
    diffed = difflib.unified_diff(actual_lines, expected_lines, lineterm="")
    return "\n".join(diffed)

def parse_expected_lines(path, sample):
    if path:
        with open(path) as f:
            expected_lines = f.read().splitlines()
    else:
        expected_lines = sample.splitlines()

    return expected_lines
