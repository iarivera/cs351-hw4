import json

# returns dict from characters in file
def charAnalysisFromFile(file):
    d = {}
    with open(file, 'r') as r:
        for line in r:
            for char in line:
                if char not in d:
                    d[char] = 1
                else:
                    d[char] += 1
    return d

