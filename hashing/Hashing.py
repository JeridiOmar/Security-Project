import hashlib

import pyinputplus as pyip


class Hashing:
    @classmethod
    def hash_menu(cls):
        print('--------HASHING MODULE--------')

        while True:
            print('\n')
            choice = pyip.inputMenu(['hash', 'quit'], numbered=True)
            if choice == 'hash':
                text = pyip.inputStr('Enter text to hash : \n')
                hashed_text = Hashing.multi_method_hash(text)
                print(' Hash ====> ' + hashed_text)
            else:
                return

    @classmethod
    def multi_method_hash(cls, text):
        method = pyip.inputMenu(list(hashlib.algorithms_guaranteed), numbered=True)
        input_hash = Hashing.text_to_hash(text, method)
        return input_hash

    @classmethod
    def text_to_hash(cls, text, method):
        encoded_text = text.encode()
        if method.upper() == 'MD5':
            return hashlib.md5(encoded_text).hexdigest()
        if method.upper() == 'SHA1':
            return hashlib.sha1(encoded_text).hexdigest()
        if method.upper() == 'SHA256':
            return hashlib.sha256(encoded_text).hexdigest()
        if method.upper() == 'SHA384':
            return hashlib.sha384(encoded_text).hexdigest()
        if method.upper() == 'SHA512':
            return hashlib.sha512(encoded_text).hexdigest()
        if method.upper() == 'SHA3_256':
            return hashlib.sha3_256(encoded_text).hexdigest()
        if method.upper() == 'SHA3_384':
            return hashlib.sha3_384(encoded_text).hexdigest()
        if method.upper() == 'SHAKE_128':
            return hashlib.shake_128(encoded_text).hexdigest(128)
        if method.upper() == 'SHA224':
            return hashlib.sha224(encoded_text).hexdigest()
        if method.upper() == 'BLAKE2B':
            return hashlib.blake2b(encoded_text).hexdigest()
        if method.upper() == 'BLAKE2S':
            return hashlib.blake2s(encoded_text).hexdigest()
        if method.upper() == 'SHAKE_256':
            return hashlib.shake_256(encoded_text).hexdigest(256)
        if method.upper() == 'SHA3_512':
            return hashlib.sha3_512(encoded_text).hexdigest()
        if method.upper() == 'SHA3_224':
            return hashlib.sha3_224(encoded_text).hexdigest()
