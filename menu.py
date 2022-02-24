from re import L
import pyfiglet
from colorama import init, Fore, Back, Style
import sys
from getpass import getpass
from dotenv import load_dotenv
import os
from src.zoomify import Zoomify


class Menu:
  
  def __init__(self, zoom=None, participants=[]):
    self.participants = participants
    self.zoom = zoom

  # Pull in environment variables
  def get_env_vars(self):
    load_dotenv()
    ZOOM_API_KEY = os.environ.get("ZOOM_API_KEY")
    ZOOM_API_SECRET = os.environ.get("ZOOM_API_SECRET")
    ZOOM_JWT = os.environ.get("ZOOM_JWT")
    self.zoom = Zoomify(ZOOM_API_KEY, ZOOM_API_SECRET, ZOOM_JWT)

  # Instantiate Zoomify object

  def title_message(self, str, color=Fore.RED):
    message = pyfiglet.figlet_format(str)
    init(autoreset=True)
    print(Style.BRIGHT + color + message)

  def paragraph_message(self, str, color=Fore.RED):
    init(autoreset=True)
    print(Style.BRIGHT + color + str)

  def command_options(self):
    command_options_menu = '''
    Command Options:

    - Check Attendance Report: "R"
    - Export to Google Sheets: "G"
    - Main Menu: "M"
    - Exit Program: "E"
    '''
    self.paragraph_message(command_options_menu, Fore.CYAN)

    user_input = input("Please enter a command > ")


    print()
    if user_input.lower() == 'r':
      self.attendance_report()
    elif user_input.lower() == 'g':
      self.google_sheets()
    elif user_input.lower() == 'm':
      self.main_menu()
    elif user_input.lower() == 'e':
      self.exit()
    else: 
      self.paragraph_message('You have entered a invalid option please try again.')
      self.command_options()

    
  def welcome(self):
    self.title_message("Welcome to Zoomify's Attendance Checker", Fore.CYAN)

  def welcome_menu(self):
    init(autoreset=True)
    user_input = input("Enter 'L' to login or 'E' to exit > ")

    while user_input.lower() != 'e':
      if user_input.lower() == 'l':
        self.main_menu()
      else: 
        self.paragraph_message('You have entered a invalid option please try again.')
      print()
      self.welcome_menu()
    if user_input.lower() == 'e':
      self.exit()

  def main_menu(self):
    self.title_message('Main Menu', Fore.GREEN)
    title = '''
    Let's Get Started!
    
    *****************************************************************************************************************

    Instructions: After your meeting ends, please enter your email below to select a meeting to check attendance on!

    *****************************************************************************************************************
    '''
    self.paragraph_message(title, Fore.LIGHTGREEN_EX)
    try:
      email = input("Enter your email > ")
      self.uuid = self.zoom.get_meeting_reports(email)
      self.participants = self.zoom.get_meeting_participants(self.uuid)
    except KeyError as ke:
      print('Please enter a valid user email', ke)
      self.welcome_menu()
    self.command_options()


  def attendance_report(self):
    self.title_message("Attendance Report", Fore.GREEN)
    attendance = self.zoom.check_attendance(self.participants)    
    self.command_options()


  def google_sheets(self):
    self.title_message("Google Sheets", Fore.GREEN)
    self.paragraph_message("This export process may take a moment... ", Fore.LIGHTGREEN_EX)
    print("https://docs.google.com/spreadsheets/d/1WzZMRT4JSRIx1kRg44MbzunKjClnEeHIkLiarGyjuww/edit?usp=sharing")
    self.zoom.export_participant_data(self.uuid)
    self.command_options()

  def exit(self):
    self.title_message('Thank you for using Zoomify', Fore.LIGHTRED_EX)
    sys.exit()

    

if __name__ == '__main__':
  new_menu = Menu()

  new_menu.get_env_vars()
  new_menu.welcome()
  new_menu.welcome_menu()
  # main_menu()
  # test_menu()
