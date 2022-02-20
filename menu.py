from re import L
import pyfiglet
from colorama import init, Fore, Back, Style
import sys
from getpass import getpass
from dotenv import load_dotenv
import os
from src.zoomify import Zoomify

# Pull in environment variables
load_dotenv()
ZOOM_API_KEY = os.environ.get("ZOOM_API_KEY")
ZOOM_API_SECRET = os.environ.get("ZOOM_API_SECRET")
ZOOM_JWT = os.environ.get("ZOOM_JWT")

# Instantiate Zoomify object
zoom = Zoomify(ZOOM_API_KEY, ZOOM_API_SECRET, ZOOM_JWT)
participants = []

def title_message(str, color=Fore.RED):
  message = pyfiglet.figlet_format(str)
  init(autoreset=True)
  print(Style.BRIGHT + color + message)

def paragraph_message(str, color=Fore.RED):
  init(autoreset=True)
  print(Style.BRIGHT + color + str)

def command_options():
  command_options_menu = '''
  Command Options:

  - Check Attendance Report: "R"
  - Data Visualization Tool: "V"
  - Main Menu: "M"
  - Exit Program: "E"
  '''
  paragraph_message(command_options_menu, Fore.CYAN)

  user_input = input("Please enter a command > ")


  print()
  if user_input.lower() == 'r':
    attendance_report()
  elif user_input.lower() == 'v':
    data_visualization()
  elif user_input.lower() == 'm':
    main_menu()
  elif user_input.lower() == 'e':
    exit()
  else: 
    paragraph_message('You have entered a invalid option please try again.')
    command_options()

  
def welcome():
  title_message("Welcome to Zoomify's Attendance Checker", Fore.BLUE)

def welcome_menu():
  init(autoreset=True)
  user_input = input("Enter 'L' to login or 'E' to exit > ")

  while user_input.lower() != 'e':
    if user_input.lower() == 'l':
      main_menu()
    else: 
      paragraph_message('You have entered a invalid option please try again.')
    print()
    welcome_menu()
  if user_input.lower() == 'e':
    exit()

def main_menu():
  title_message('Main Menu', Fore.GREEN)
  title = '''
  Let's Get Started!
  
  *****************************************************************************************************************

  Instructions: After your meeting ends, please enter your email below to select a meeting to check attendance on!

  *****************************************************************************************************************
  '''
  paragraph_message(title, Fore.LIGHTGREEN_EX)
  email = input("Enter your email > ")
  # print(email)
  uuid = zoom.get_meeting_reports(email)
  global participants
  participants = zoom.get_meeting_participants(uuid)
  
  command_options()


def attendance_report():
  title_message("Attendance Report", Fore.GREEN)
  global participants
  attendance = zoom.check_attendance(participants)
  # print(attendance)
  # print("\n Attendees \n ---------")
  # for name in participants: 
  #   print(f'{name}')
  
  command_options()


def data_visualization():
  title_message("Data Visualization", Fore.GREEN)
  command_options()

def exit():
  title_message('Thank you for using Zoomify', Fore.LIGHTYELLOW_EX)
  sys.exit()

  

if __name__ == '__main__':



  welcome()
  welcome_menu()
  # main_menu()
  # test_menu()