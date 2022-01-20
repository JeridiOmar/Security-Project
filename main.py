import hashlib
import threading
from socket import socket
from tkinter import mainloop
from socket import *
import pyinputplus as pyip

from random import randint

import rsa

from client.assist import process
from client.assist.sthread import stop_thread
from client.chat_client import ChatRoomGUI
from services.dao import add_new_user, fetch_user
from services.emails_service import *
from services.input_service import *

from asymmetric_encryption.AsymmetricEncrypt import AsymmetricEncrypt
from cracking.Cracking import Cracking
from encoding.Encoding import Encoding
from hashing.Hashing import Hashing
from symmetric_encryption.SymmetricEncrypt import SymmetricEncrypt


def menu():
    while True:
        choice = pyip.inputMenu(
            ['sign-in', 'sign-up', 'quit'], numbered=True)
        if choice == 'sign-in':
            return signIn()
        if choice == 'sign-up':
            signUp()


def menu_logged_in(name):
    while True:
        choice = pyip.inputMenu(
            ['encoding', 'hashing', 'mail-crack', 'symmetric-encrypt', 'asymmetric-encrypt', 'chat-room', 'quit'],
            numbered=True)
        if choice == 'encoding':
            Encoding.menu()
        elif choice == 'hashing':
            Hashing.hash_menu()
        elif choice == 'mail-crack':
            Cracking.menu()
        elif choice == 'symmetric-encrypt':
            SymmetricEncrypt.menu()
        elif choice == 'asymmetric-encrypt':
            AsymmetricEncrypt.menu()
        elif choice == 'chat-room':
            launch_chat_room(name)
        elif choice == 'quit':
            return


def signIn():  # returns a tuple with user infos
    print()
    print("============== SIGN IN ===============")
    print()
    while True:
        email = input('email : ')
        password = read_pass()
        user = fetch_user(email, hashlib.sha256(bytes(password, 'utf-8')).digest())
        if user is not None:
            break

    firstname = user[2]

    message = randint(100000, 999999)

    send_double_factor_code(email, message, firstname)
    while True:
        verify_code = input('type your code here : ')
        # print('user : ', user)
        if int(verify_code) == message:
            return user


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
    code = int(input("code : "))
    while int(code) != message:
        resend_mail = input('resend mail yes/no')
        if resend_mail == 'yes':
            sendCode(email, message, firstname)
        code = input("codes don't match, retype code : ")

    add_new_user(firstname, lastname, email, hashlib.sha256(bytes(password, 'utf-8')).digest())


def launch_chat_room(name):
    HOST = 'localhost'  # input('Please input the ip of the server:')
    PORT = 12345
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    pub, priv = rsa.newkeys(1024)
    udpCliSock = socket(AF_INET, SOCK_DGRAM)
    chat_room = ChatRoomGUI(udpCliSock, ADDR, name)

    mthread = threading.Thread(target=chat_room.recv_message, args=[])

    mthread.start()

    mainloop()

    msg = 'disconnect'

    package = process.assemble('disconnect', name, 'server', len(msg), msg)

    udpCliSock.sendto(package, ADDR)

    stop_thread(mthread)

    udpCliSock.close()


if __name__ == '__main__':
    user = menu()
    menu_logged_in(user[2])
