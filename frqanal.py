import string
import json

# returns dict from characters in string
def charAnalysis(text):
    d = {}
    text = text.upper()
    for char in string.ascii_uppercase:
        d[char] = text.count(char)
    return d

def sortedFreq(d, PRINT=False):
    ret = sorted(d.items(), key=lambda item: item[1], reverse=True)
    if PRINT:
        for k, v in ret:
            print(f"{k}: {v}")
    return ret

def replace(text, char1, char2):
    text = text.replace(char1, 'a') # all ciphers are upper
    text = text.replace(char2, char1)
    text = text.replace('a', char2)
    return text
