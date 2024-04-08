"""
Step 2: Frequency Analysis
    takes in a string [text] and returns a dictionary containing the frequencies of each letter
"""
import string

# gather letter frequencies in a text and save values to dictionary (key, letter -> value, frequency) 
def charAnalysis(text):
    # initialize an empty dictionary [d], a character count [totChar], and uppercase each character for consistency [text]
    d = {}
    totChar=0
    text = text.upper()

    # iterate through each charater, update totChar, counting and storing the frequecy in a dictionary
    for char in string.ascii_uppercase:
        totChar+=text.count(char)
        d[char] = text.count(char)
    for key in list(d):
        d[key]=(d[key]/totChar*100, d[key])

    return d

# sorting the frequenceies in descending order | printing letter, precentage, and count
def sortedFreq(d):
    ret = sorted(d.items(), key=lambda item: item[1][1], reverse=True)
    formatted_strings = []
    for k, v in ret:
        formatted_strings.append(f"{k}: {v[0]:5.2f}%  {v[1]:2n}")
    return formatted_strings

# replace the characters based on frequency and mapping
def replace(text, mapping):
    newText=""
    for i in text:
        if i in mapping:
            newText += "\033[4m"+mapping[i]+"\033[0m" # \033[...m is ANSI used for terminal underline
        else:
            newText +=i
    return newText
