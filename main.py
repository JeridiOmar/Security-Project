import hashlib
import pyinputplus as pyip

from random import randint
from services.dao import add_new_user, fetch_user
from services.emails_service import *
from services.input_service import *


def menu():
    while True:
        choice = pyip.inputMenu(
            ['encoding', 'hashing', 'password-crack', 'symmetric-encrypt', 'asymmetric-encrypt', 'chat-room', 'quit'])
        if choice == 'encoding':
            print('encoding')
        elif choice == 'hashing':
            print('hashing')
        elif choice == 'password-crack':
            print('password-crack')
        elif choice == 'symmetric-encrypt':
            print('symmetric-encrypt')
        elif choice == 'asymmetric-encrypt':
            print('asymmetric-encrypt')
        elif choice == 'chat-room':
            print('chat-room')
        elif choice == 'quit':
            return


def signIn(): # returns a tuple with user infos
    print()
    print("============== SIGN IN ===============")
    print()

    email = input('email : ')
    password = input('password : ')

    user = fetch_user(email, hashlib.sha256(bytes(password, 'utf-8')).digest())

    firstname = user[2]

    message = randint(100000, 999999)

    send_double_factor_code(email, message, firstname)

    verify_code = input('type your code here : ')
    # print('user : ', user)
    if int(verify_code) == message:
        return user
    return None


def signUp():
    print()
    print("============== SIGN UP ===============")
    print()

    firstname = input('enter your firstname : ')
    lastname = input('enter your lastname : ')

    email = read_email()

    password = read_pass()

    confirm_pass(password)

    message = randint(100000, 999999)

    sendCode(email, message, firstname)

    print("we've sent you an email containing a verification code!")
    code = int(input("code"))
    while int(code) != message:
        resend_mail = input('resend mail yes/no')
        if resend_mail == 'yes':
            sendCode(email, message, firstname)
        code = input("codes don't match, retype code : ")

    add_new_user(firstname, lastname, email, hashlib.sha256(bytes(password, 'utf-8')).digest())


if __name__ == '__main__':

    # signUp()

    user = signIn()
