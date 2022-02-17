import pyfiglet 
import click
from colorama import init, Fore, Back, Style
import sys
from getpass import getpass

# @click.command()
# def home_menu():
#   click.secho(pyfiglet.figlet_format("Welcome to Zoomify's"), fg="green", bold=False)
#   click.secho(pyfiglet.figlet_format("Attendance Checker"), fg="red", bold=False)

def message(str):
  message = pyfiglet.figlet_format(str)
  init(autoreset=True)
  print(Style.BRIGHT + Fore.RED + message)
  
def welcome():
  message("Welcome to Zoomify's Attendance Checker")


def welcome_menu():
  # print('PLEASE ENTER "L" TO LOGIN')
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

def main_menu():
  message('Main Menu')
  title = '''
  Let's Get Started!
  ******************
  Instructions: After the end of your meeting, you have access to some useful commands shown below!
  '''
  # instructions = 'Instructions: After the end of your meeting, you have access to some useful commands shown below!'
  print(title)


def exit():
  message('Thank you for using Zoomify')
  print('close terminal to leave')
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
  # home_menu()
  welcome()
  welcome_menu()
  main_menu()
