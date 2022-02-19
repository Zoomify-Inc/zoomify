import pyfiglet 
import click
from colorama import init, Fore, Back, Style
import sys
from getpass import getpass

# @click.command()
# def home_menu():
#   click.secho(pyfiglet.figlet_format("Welcome to Zoomify's"), fg="green", bold=False)
#   click.secho(pyfiglet.figlet_format("Attendance Checker"), fg="red", bold=False)

def message(str, color=Fore.RED):
  message = pyfiglet.figlet_format(str)
  init(autoreset=True)
  print(Style.BRIGHT + color + message)

# def test_menu():
#   command_options_test = ["[r] apple", "[v] banana", "[e] orange"]
#   terminal_menu = TerminalMenu(command_options_test, title="command_options_test")
#   menu_entry_index = terminal_menu.show()

  # if terminal_menu == 'r':
  #   attendance_report()
  # elif terminal_menu == 'v':
  #   data_visualization()
  # elif terminal_menu == 'e':
  #   exit()
  # else: 
  #   print('you have entered a invalid option please try again.')

def command_options():
  command_options = '''
  Command Options:

  - Check Attendance Report: "R"
  - Data Visualization Tool: "V"
  - Exit Program: "E"
  '''
  print(command_options)
  option = input("Please Enter a Command > ")

  if option.lower() == 'r':
    attendance_report()
  elif option.lower() == 'v':
    data_visualization()
  elif option.lower() == 'e':
    exit()
  else: 
    print('you have entered a invalid option please try again.')

  
def welcome():
  message("Welcome to Zoomify's Attendance Checker")

def welcome_menu():
  option = input("Enter L to login or E to exit: ")
  while option.lower() != 'e':
    if option.lower() == 'l':
      login_menu()
    else: 
      print('you have entered a invalid option please try again.')
    print()
    welcome_menu()
  if option.lower() == 'e':
    exit()

def login_menu():
  # need to update login look 
  message("Please Login using your AuthO creds!")
  input('enter your username: ')
  getpass('Enter your password: ')

  main_menu()

def main_menu():
  message('Main Menu')
  title = '''
  Let's Get Started!
  ******************
  Instructions: After the end of your meeting, you have access to some useful commands shown below!
  '''
  print(title)
  command_options()


def attendance_report():
  message("Attendance Report", Fore.BLUE)
  command_options()


def data_visualization():
  message("Data Visualization", Fore.BLUE)
  command_options()


def exit():
  message('Thank you for using Zoomify')
  sys.exit()


def options():
  option = input()
  if option == 'L':
    print('you have looged in successfully')
  elif option == 'E':
    sys.exit('Thanks for using Zoomify enjoy your new Zoomify time!')
  elif option == 'B':
    print('you have gone back')
  elif option == "R":
    print('you have successfully ran a report' )
  elif option == 'V':
    print('visual success')
  

if __name__ == '__main__':
  welcome()
  welcome_menu()
  main_menu()
  # test_menu()
