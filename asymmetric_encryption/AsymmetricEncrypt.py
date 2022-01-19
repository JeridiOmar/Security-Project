import base64
import binascii
import random

import pyinputplus as pyip
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import elgamal
import pickle


class AsymmetricEncrypt:
    RSA_KEYS_PATH = 'asymmetric_encryption/rsa_keys/'
    ELGAMAL_KEYS_PATH = 'asymmetric_encryption/elGamal_keys/'
    @classmethod
    def menu(cls):
        print('\n')
        print("--------ASYMMETRIC ENCRYPTION MODULE--------\n")
        while True:
            choice = pyip.inputMenu(['RSA', 'ElGamal', 'quit'], numbered=True)
            if (choice == 'RSA'):
                while True:
                    type = pyip.inputMenu(['gen-new-key', 'encrypt', 'decrypt', 'sign', 'verify', 'quit'],
                                          numbered=True)
                    if (type == 'gen-new-key'):
                        key_name = pyip.inputStr('Please type the name of the key pair : \n')
                        key_size = text_input = pyip.inputInt('Please type the size of the key : \n')
                        AsymmetricEncrypt.gen_rsa_key(key_name, key_size)
                        print('New par of key are generated under /asymmetric_encryption/rsa_keys\n')
                        print('keys names :( {}-private.pem , {}-public.pem )'.format(key_name, key_name))
                    if (type == 'encrypt'):
                        text_input = pyip.inputStr('Please type the plain text : \n')
                        key_name = pyip.inputStr('Please type the key name : \n')
                        print('encrypted text : \n')
                        print(AsymmetricEncrypt.rsa_encrypt(text_input, key_name))
                    if (type == 'decrypt'):
                        cipher_input = pyip.inputStr('Please type the cipher text : \n')
                        key_name = pyip.inputStr('Please type the key name : \n')
                        print('decrypted text : ')
                        print(AsymmetricEncrypt.rsa_decrypt(cipher_input, key_name))
                    if (type == 'sign'):
                        text = pyip.inputStr('Please type the text : \n')
                        key_name = pyip.inputStr('Please type the key name : \n')
                        print('signature : ')
                        print(AsymmetricEncrypt.rsa_sign(text, key_name))
                    if (type == 'verify'):
                        signature = pyip.inputStr('Please type the signature : \n')
                        text = pyip.inputStr('Please type the text to verify signature : \n')
                        key_name = pyip.inputStr('Please type the key name : \n')
                        print(AsymmetricEncrypt.rsa_verify(text, signature, key_name))
                    else:
                        break
            if (choice == 'ElGamal'):
                while True:
                    type = pyip.inputMenu(['gen-key', 'encrypt', 'decrypt', 'quit'], numbered=True)
                    if (type == 'gen-key'):
                        key_name = pyip.inputStr('Please type the key name :')
                        AsymmetricEncrypt.gen_el_gamal_key(key_name)
                        print('New par of key are generated under /asymmetric_encryption/elGamal_keys\n')

                    if (type == 'encrypt'):
                        text_input = pyip.inputStr('Please type the text to encrypt : \n')
                        key_name = pyip.inputStr('Please type the key name :')
                        AsymmetricEncrypt.encrypt(key_name, text_input)
                    if (type == 'decrypt'):
                        cipher_input = pyip.inputStr('Please type the encrypted text : \n')
                        key_name = pyip.inputStr('Please type the key name :')
                        AsymmetricEncrypt.decrypt(key_name, cipher_input)
                    else:
                        break
            if (choice == 'quit'):
                return

    #############RSA################

    @classmethod
    def gen_rsa_key(cls, name, size):
        key = RSA.generate(size)
        private = key.exportKey('PEM')
        public = key.publickey().exportKey('PEM')
        with open(AsymmetricEncrypt.RSA_KEYS_PATH + name + '-private.pem', 'w') as f:
            f.write(private.decode())
            f.close()
        with open(AsymmetricEncrypt.RSA_KEYS_PATH  + name + '-public.pem', 'w') as f:
            f.write(public.decode())
            f.close()

    @classmethod
    def get_rsa_keys_from_file(cls, name):
        with open(AsymmetricEncrypt.RSA_KEYS_PATH  + name + '-private.pem', 'r') as fk:
            priv = fk.read()
            fk.close()

        with open(AsymmetricEncrypt.RSA_KEYS_PATH  + name + '-public.pem', 'r') as fp:
            pub = fp.read()
            fp.close()

        private = RSA.importKey(priv)
        public = RSA.importKey(pub)
        return {'public': public, 'private': private}

    @classmethod
    def rsa_encrypt(cls, plain_text, key_name):
        public_key = AsymmetricEncrypt.get_rsa_keys_from_file(key_name)['public']
        cipher = PKCS1_v1_5.new(public_key)
        encrypted_text = cipher.encrypt(plain_text.encode('utf-8'))
        encode_string = base64.b64encode(encrypted_text)
        return encode_string.decode('utf-8')

    @classmethod
    def rsa_decrypt(cls, encrypted_text, key_name):
        cipher_text = base64.b64decode(encrypted_text)
        private_key = AsymmetricEncrypt.get_rsa_keys_from_file(key_name)['private']
        cipher = PKCS1_v1_5.new(private_key)
        decrypted_text = cipher.decrypt(cipher_text, None)
        return bytes.decode(decrypted_text)

    @classmethod
    def rsa_sign(cls, plain_text, key_name):
        private = AsymmetricEncrypt.get_rsa_keys_from_file(key_name)['private']
        hash = SHA256.new(plain_text.encode('utf-8'))
        signer = PKCS115_SigScheme(private)
        signature = signer.sign(hash)
        return bytes.decode(binascii.hexlify(signature))

    @classmethod
    def rsa_verify(cls, text, signature, key_name):
        public = AsymmetricEncrypt.get_rsa_keys_from_file(key_name)['public']
        hash = SHA256.new(text.encode('utf-8'))
        verifier = PKCS115_SigScheme(public)
        try:
            verifier.verify(hash, binascii.unhexlify(signature))
            return "Signature is valid."
        except:
            return "Signature is invalid."

    ############ELGAMAL#############

    @classmethod
    def gen_el_gamal_key(cls, name):
        key = elgamal.generate_keys()
        with open(AsymmetricEncrypt.ELGAMAL_KEYS_PATH + name + '.pem', 'wb') as f:
            pickle.dump(key, f)

    @classmethod
    def load_el_gamal_key(cls, name):
        with open(AsymmetricEncrypt.ELGAMAL_KEYS_PATH + name + '.pem', 'rb') as f:
            key = pickle.load(f)
        return key

    @classmethod
    def encrypt(cls, key_name, plaintext):
        el_gamal_keys = AsymmetricEncrypt.load_el_gamal_key(key_name)
        cipher = AsymmetricEncrypt.elgamalEncrypt(plaintext, el_gamal_keys)
        return ('encrypt', cipher)

    @classmethod
    def decrypt(cls, key_name, signature=''):
        el_gamal_keys = AsymmetricEncrypt.load_el_gamal_key(key_name)
        AsymmetricEncrypt.elgamaDecrypt(signature, el_gamal_keys)

    @classmethod
    def elgamalEncrypt(cls, msg, elGamalKeys):
        cipher = elgamal.encrypt(elGamalKeys['publicKey'], msg)
        print(cipher)
        return cipher

    @classmethod
    def elgamaDecrypt(cls, cipher, el_gamal_keys):
        plaintext = elgamal.decrypt(el_gamal_keys['privateKey'], cipher)
        print(plaintext)
