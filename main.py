import pyinputplus as pyip
import sqlite3

from encoding.Encoding import Encoding


def menu():
    while True:
        choice = pyip.inputMenu(
            ['encoding', 'hashing', 'password-crack', 'symmetric-encrypt', 'asymmetric-encrypt', 'chat-room', 'quit'],
            numbered=True)
        if choice == 'encoding':
            Encoding.menu()
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


if __name__ == '__main__':
    # con = sqlite3.connect('pen')
    # cur = con.cursor()
    # cur.execute("INSERT INTO users (firstname,lastname,email,password) VALUES ('omar','jeridi',"
    #             "'amrouch_jridi@hotmail.fr','pass')")
    #
    # con.commit()
    # for row in cur.execute('SELECT * FROM users'):
    #     print(row)
    # con.close()

    menu()
