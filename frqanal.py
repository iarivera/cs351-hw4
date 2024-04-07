import string
import json

# returns dict from characters in string
def charAnalysis(text):
    d = {}
    totChar=0
    text = text.upper()
    for char in string.ascii_uppercase:
        totChar+=text.count(char)
        d[char] = text.count(char)
    for key in list(d):
        d[key]=(d[key]/totChar*100, d[key])
    return d

def sortedFreq(d, PRINT=False):
    ret = sorted(d.items(), key=lambda item: item[1][1], reverse=True)
    if PRINT:
        for k, v in ret:
            #print(f"\033[4m{k}:\033[0m {v}"
            print(f"{k}:  {v[0]:5.2f}%  {v[1]:2n}")
    return ret

# def replace(text, char1, char2):
#     text = text.replace(char1, 'a') # all ciphers are upper
#     text = text.replace(char2, char1)
#     text = text.replace('a', char2)
#     return text
def replace(text, mapping):
    newText=""
    for i in text:
        if i in mapping:
            newText += "\033[4m"+mapping[i]+"\033[0m" # \033[...m is ANSI used for terminal underline
        else:
            newText +=i
    return newText
