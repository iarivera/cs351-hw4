import json

d = {}
with open("cipher.txt", 'r') as r:
  for line in r:
    for char in line:
      if char not in d:
        d[char] = 1
      else:
        d[char] += 1

print(json.dumps(d,sort_keys=True,indent=4))
