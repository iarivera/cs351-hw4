import json

# returns dict from characters in file
def charAnalysis(file):
    d = {}
    with open(file, 'r') as r:
        for line in r:
            for char in line:
                char = char.upper()
                if char not in d:
                    d[char] = 1
                else:
                    d[char] += 1
    # remove all non-alphabet
    for key in list(d):
        if not key.isalpha():
            del d[key]
    return d

def prettyPrintByFreq(d):
    for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True):
        print(f"{k}: {v}")

def replace(text, char1, char2):
    text = text.replace(char1, 'a') # all ciphers are upper
    text = text.replace(char2, char1)
    text = text.replace('a', char2)
    return text
