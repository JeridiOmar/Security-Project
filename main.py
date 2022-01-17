import pyinputplus as pyip


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


if __name__ == '__main__':
    menu()
