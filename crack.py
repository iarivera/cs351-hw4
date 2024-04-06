#!/usr/bin/env python3

import sys
import json
import frqanal

# most common characters in english, in order:
# ETAOINSHRDL

def main():
    # prompt user for file
    if len(sys.argv) > 1:
        file = sys.argv[1]
        print(f"using file {file}")
    else:
        file = input("filename: ")

    text = ''
    for line in open(file):
        text += line

    # calculate frequency of each letter in ciphertext
    char_dict = frqanal.charAnalysis(text)
    frq = frqanal.sortedFreq(char_dict, True)

    # replace first four characters by frequency
    for i in range(4):
        letter = 'ETAO'[i]
        text = frqanal.replace(text, letter, frq[i][0])
        char_dict = frqanal.charAnalysis(text)
        frq = frqanal.sortedFreq(char_dict)
    print(text)
    frqanal.sortedFreq(char_dict, True)

if __name__ == '__main__':
    main()
