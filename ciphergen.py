#!/bin/python3

import string
import random
import sys

def ciphergen():
    ret = ''
    lowers = list(string.ascii_lowercase)
    while len(lowers) != 0:
        ret += lowers.pop(random.randint(0,len(lowers)-1))
    return ret

def main():
    if len(sys.argv) > 1:
        try:
            for i in range(int(sys.argv[1])):
                print(ciphergen())
        except:
            print('usage: ciphergen [num]')
    else:
        print(ciphergen())

if __name__ == '__main__':
    main()
