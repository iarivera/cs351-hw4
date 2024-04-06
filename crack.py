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

    # calculate frequency of each letter in ciphertext
    char_dict = frqanal.charAnalysis(file)
    # remove all non-alphabet
    for key in list(char_dict):
        if not key.isalpha():
            del char_dict[key]
    # print(json.dumps(char_dict, indent=4, sort_keys=True))
    frqanal.prettyPrintByFreq(char_dict)

    # replace first four characters by frequency
    

if __name__ == '__main__':
    main()
