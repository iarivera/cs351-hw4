# Terminal Version of crack.py, functionally equivalent

import sys
import json
import frqanal
import string
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
    frq = frqanal.sortedFreq(char_dict)

    mapping={}
    invMapping={}
    inp=""
    # replace characters by frequency. Allow for the choice of how many letters should be replaced as lower frequency letters can produce inconsistent results
    while(not inp.isnumeric() or inp=="" or int(inp)>26):
        inp=input("Input how many letters to replace in the cipher (1-26)")
    inp=int(inp)
    print("Mappings:")
    for i in range(inp):
        # Letter frequency order gotten from:https://en.wikipedia.org/wiki/Letter_frequency
        letter = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'[i]
        cipherL=frq[i][0]
        mapping[cipherL]=letter
        invMapping[letter]=cipherL
        print(f"{cipherL}->{letter}")
        # char_dict = frqanal.charAnalysis(text)
        # frq = frqanal.sortedFreq(char_dict)


    while(True):
        print("\nCurrent Ciphertext:\n"+frqanal.replace(text, mapping))
        print("Original Ciphertext:\n"+text)
        inp=""
        while(inp!="2" and inp!="1" and inp!="3"):
            inp=input("What would you like to do now?\n(1) New Mapping\n(2) Show Mappings\n(3) Done\n")
        if(inp=="3"):
            exit()
        elif(inp=="2"):
            for i in mapping:
                print(f"{i}->{mapping[i]}")
        elif(inp=="1"):
            while(not (inp in string.ascii_uppercase) or inp==""):
                inp=input("What cipher character are you replacing?\n")
            cipherL=inp
            inp=""
            while(not (inp in string.ascii_uppercase) or inp==""):
                inp=input("What character should it be replaced with?\n")
            letter=inp
            inp=input(f'Type (Y) to add mapping "{cipherL} -> {letter}"\n')
            if(inp=="Y"):
                # Following statements account for the fact mapping is 1 to 1 operation
                if(cipherL in mapping):
                    if(letter in invMapping):
                        mapping[invMapping[letter]]=mapping[cipherL]
                        mapping[cipherL]=letter
                        invMapping={v: k for k, v in mapping.items()}
                    else:
                        mapping[cipherL]=letter
                        invMapping={v: k for k, v in mapping.items()}
                else:
                    if(letter in invMapping):
                        invMapping[letter]=cipherL
                        mapping={v: k for k, v in invMapping.items()}
                    else:
                        mapping[cipherL]=letter
                        invMapping[letter]=cipherL
                    
                print("Added Mapping\n")
            else:
                print("Cancelled Mapping\n")
    # frqanal.sortedFreq(mapping, True)

if __name__ == '__main__':
    main()