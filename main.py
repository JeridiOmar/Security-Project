import pyinputplus as pyip
import sqlite3

from cracking.Cracking import Cracking
from encoding.Encoding import Encoding
from hashing.Hashing import Hashing
from symmetric_encryption.SymmetricEncrypt import SymmetricEncrypt

def menu():
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
