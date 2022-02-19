import pyfiglet 
from colorama import init, Fore, Back, Style
import sys
from getpass import getpass


def title_message(str, color=Fore.RED):
  message = pyfiglet.figlet_format(str)
  init(autoreset=True)
  print(Style.BRIGHT + color + message)

def paragraph_message(str, color=Fore.RED):
  init(autoreset=True)
  print(Style.BRIGHT + color + str)

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
  command_options_menu = '''
  Command Options:

  - Check Attendance Report: "R"
  - Data Visualization Tool: "V"
  - Exit Program: "E"
  '''
  paragraph_message(command_options_menu, Fore.CYAN)

  user_input = input("Please enter a command > ")


  print()
  if user_input.lower() == 'r':
    attendance_report()
  elif user_input.lower() == 'v':
    data_visualization()
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
      login_menu()
    else: 
      paragraph_message('You have entered a invalid option please try again.')
    print()
    welcome_menu()
  if user_input.lower() == 'e':
    exit()

def login_menu():
  # need to update login look 
  title_message("Please login using your AuthO credentials!", Fore.GREEN)
  input('Enter your username > ')
  getpass('Enter your password > ')

  main_menu()

def main_menu():
  title_message('Main Menu', Fore.GREEN)
  title = '''
  Let's Get Started!
        ---
  *************************************************************************************************

  Instructions: After the end of your meeting, you have access to some useful commands shown below!

  *************************************************************************************************
  '''
  paragraph_message(title, Fore.LIGHTGREEN_EX)
  command_options()


def attendance_report():
  title_message("Attendance Report", Fore.GREEN)
  command_options()


def data_visualization():
  title_message("Data Visualization", Fore.GREEN)
  command_options()


def exit():
  title_message('Thank you for using Zoomify', Fore.LIGHTYELLOW_EX)
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
