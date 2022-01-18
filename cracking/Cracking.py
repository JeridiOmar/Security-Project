import hashlib

import pyinputplus as pyip

from hashing.Hashing import Hashing


class Cracking:
    @classmethod
    def menu(cls):
        print("--------CRACKING MODULE--------\n")
        print("Supported format : aaaaa@insat.ucar.tn \n")
        print("the Name vary between 3 and 5 characters \n")
        while True:
            print('\n')
            choice = pyip.inputMenu(['crack-with-hash-type', 'crack-unknown-hash-type', 'quit'], numbered=True)
            if choice == 'crack-unknown-hash-type':
                hash = pyip.inputStr('Enter hash for cracking : \n')
                cracked_hash = Cracking.mail_cracker(hash)
                print(cracked_hash)
            if choice == 'crack-with-hash-type':
                hash = pyip.inputStr('Enter hash for cracking : \n')
                hash_type = pyip.inputMenu(list(hashlib.algorithms_guaranteed), numbered=True)
                cracked_hash = Cracking.mail_cracker_hash_type(hash, hash_type)
                print(cracked_hash)
            else:
                return

    @classmethod
    def mail_cracker(cls, hash):
        methods = list(hashlib.algorithms_guaranteed)
        with open('cracking/insat2.dic', 'r+') as f:
            names = f.read().splitlines()
            l = len(names) * len(methods)
            i = 0
            Cracking.printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
        for name in names:
            mail = name + '@insat.ucar.tn'
            for method in methods:
                if (Hashing.text_to_hash(mail, method) == hash):
                    return mail
                i = i + 1
                Cracking.printProgressBar(i, l, prefix='Progress:', suffix='Complete', length=50)
        return '[X] Unable to crack the hash'

    @classmethod
    def mail_cracker_hash_type(cls, hash, type):
        methods = list(hashlib.algorithms_guaranteed)
        with open('cracking/insat2.dic', 'r+') as f:
            names = f.read().splitlines()
            l = len(names)
            i = 0
            Cracking.printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
        for name in names:
            mail = name + '@insat.ucar.tn'

            if (Hashing.text_to_hash(mail, type) == hash):
                return mail
            i = i + 1
            Cracking.printProgressBar(i, l, prefix='Progress:', suffix='Complete', length=50)
        return '[X] Unable to crack the hash'

    # Print iterations progress
    @classmethod
    def printProgressBar(cls, iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
        # Print New Line on Complete
        if iteration == total:
            print()
