import base64
import hashlib
import os

import base32hex
from getpass import getpass

import pyinputplus as pyip
from Crypto import Random
from Crypto.Cipher import DES, AES


class SymmetricEncrypt:
    AES_BLOCK_SIZE = 16
    @classmethod
    def menu(cls):
        print('\n')
        print("--------SYMMETRIC ENCRYPTION MODULE--------\n")
        while True:
            choice = pyip.inputMenu(['DES', 'AES256', 'quit'], numbered=True)
            if (choice == 'DES'):
                while True:
                    type = pyip.inputMenu(['encrypt', 'decrypt', 'quit'], numbered=True)
                    if (type == 'encrypt'):
                        text_input = pyip.inputStr('Please type the text to encrypt : \n')
                        password = pyip.inputStr('Please type the password :')
                        SymmetricEncrypt.des_encrypt(text_input, password)
                    if (type == 'decrypt'):
                        text_input = pyip.inputStr('Please type the encrypted text : \n')
                        password = pyip.inputStr('Please type the password : \n')
                        SymmetricEncrypt.des_decrypt(text_input, password)
                    else:
                        break
            if (choice == 'AES256'):
                while True:
                    type = pyip.inputMenu(['encrypt', 'decrypt', 'quit'], numbered=True)
                    if (type == 'encrypt'):
                        text_input = pyip.inputStr('Please type the text to encrypt : \n')
                        password = pyip.inputStr('Please type the password :')
                        print("Cipher Text : "+SymmetricEncrypt.aes_encrypt(text_input, password))
                    if (type == 'decrypt'):
                        cipher_input = pyip.inputStr('Please type the encrypted text : \n')
                        password = pyip.inputStr('Please type the password :')
                        print("Raw Text : "+SymmetricEncrypt.aes_decrypt(cipher_input, password))
                    else:
                        break
            if (choice == 'quit'):
                return

    @classmethod
    def des_encrypt(cls, text, password):
        key = password
        m = hashlib.md5(key.encode('utf-8'))
        key = m.digest()
        (dk, iv) = (key[:8], key[8:])
        crypter = DES.new(dk, DES.MODE_CBC, iv)
        print("The plain text is : ", text)
        # text += '\x00' * (8 - len(text) % 8)
        text = SymmetricEncrypt.pad_des(text.encode('utf-8'))
        ciphertext = crypter.encrypt(text)
        encode_string = base64.b64encode(ciphertext)
        print("The encoded text is : ", encode_string.decode("utf-8"))

    @classmethod
    def des_decrypt(cls, encrypted_text, password):
        key = password.encode('utf-8')
        m = hashlib.md5(key)
        key = m.digest()
        (dk, iv) = (key[:8], key[8:])
        crypter = DES.new(dk, DES.MODE_CBC, iv)
        print("The ecrypted string is : ", encrypted_text)
        encrypted_text = base64.b64decode(encrypted_text)
        decrypted_string = crypter.decrypt(encrypted_text)
        print("The decrypted string is : ", decrypted_string.decode("utf-8"))

    @classmethod
    def pad_des(cls, text):
        n = len(text) % 8
        return text + (b' ' * n)

    @classmethod
    def pad_aes(cls, s):
        remainder = len(s) % SymmetricEncrypt.AES_BLOCK_SIZE
        padding_needed = SymmetricEncrypt.AES_BLOCK_SIZE - remainder
        return s + padding_needed * ' '

    @classmethod
    def unpad_aes(cls, s):
        return s.rstrip()
    @classmethod
    def aes_encrypt(cls,raw_text, password):
        private_key = hashlib.sha256(password.encode("utf-8")).digest()
        raw_text = SymmetricEncrypt.pad_aes(raw_text)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw_text.encode("utf-8"))).decode("utf-8")

    @classmethod
    def aes_decrypt(cls,encrypted_text, password):
        private_key = hashlib.sha256(password.encode("utf-8")).digest()
        encrypted_text = base64.b64decode(encrypted_text)
        iv = encrypted_text[:16]
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        return SymmetricEncrypt.unpad_aes(cipher.decrypt(encrypted_text[16:])).decode("utf-8")
