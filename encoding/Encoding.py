import base64

import pyinputplus as pyip


class Encoding:
    @classmethod
    def menu(cls):
        print('/n')
        print("--------ENCODING MODULE--------\n")
        while True:
            choice = pyip.inputMenu(['encode', 'decode', 'quit'], numbered=True)
            if (choice == 'encode'):
                text_input = pyip.inputStr('Please type the text to encode : \n')
                method = pyip.inputMenu(['utf8', 'ascii', 'base16', 'base32', 'base64'])
                Encoding.encode(text_input, method)
            if (choice == 'decode'):
                encoded_input = pyip.inputStr('Please type the text to decode : \n')
                method = pyip.inputMenu(['utf8', 'ascii', 'base16', 'base32', 'base64'], numbered=True)
                Encoding.decode(encoded_input, method)
            if (choice == 'quit'):
                return

    @classmethod
    def encode(cls, data, method):
        if (method in ['utf8', 'ascii']):
            encoded_text = str.encode(data, encoding=method)
            print(' encoded text is : ')
            print(encoded_text)
            return (encoded_text)

        elif (method == 'base64'):
            message_bytes = data.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            print(' encoded text is : ' + base64_message)
            return (base64_message)

        elif (method == 'base32'):
            message_bytes = data.encode('ascii')
            base32_bytes = base64.b32encode(message_bytes)
            base32_message = base32_bytes.decode('ascii')
            print(' encoded text is : ' + base32_message)
            return (base32_message)

        elif (method == 'base16'):
            message_bytes = data.encode('ascii')
            base16_bytes = base64.b32encode(message_bytes)
            base16_message = base16_bytes.decode('ascii')
            print(' encoded text is : ' + base16_message)
            return (base16_message)

    @classmethod
    def decode(cls, encoded_data, method):
        if (method in ['utf8', 'ascii']):
            encoded_text = encoded_data.decode(encoding=method)
            print(' decoded text is : ' + encoded_text)
            return (encoded_text)

        elif (method == 'base64'):
            message_bytes = encoded_data.encode('ascii')
            base64_bytes = base64.b64decode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            print(' decoded text is : ' + base64_message)
            return (base64_message)

        elif (method == 'base32'):
            message_bytes = encoded_data.encode('ascii')
            base32_bytes = base64.b32decode(message_bytes)
            base32_message = base32_bytes.decode('ascii')
            print(' decoded text is : ' + base32_message)
            return (base32_message)

        elif (method == 'base16'):
            message_bytes = encoded_data.encode('ascii')
            base16_bytes = base64.b32decode(message_bytes)
            base16_message = base16_bytes.decode('ascii')
            print(' decoded text is : ' + base16_message)
            return (base16_message)
