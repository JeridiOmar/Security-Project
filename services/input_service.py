import re
from getpass import getpass


def read_email():
    email = input('enter your email : ')
    while not re.match('^.+@.+\.[a-z,A-Z]+$', email):
        print(' please enter a valid email!')
        email = input('email : ')
    return email

def read_pass():
    password = getpass('enter your password : ')
    while not re.match('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
        print("password must be at least 8 characters long \n and has a number and a letter")
        password = getpass('password : ')
    return password

def confirm_pass(password):
    confirm_password = getpass('confirm your password : ')
    while not password == confirm_password:
        print('passwords dont match please re-enter your password!')
        confirm_password = getpass('password : ')
