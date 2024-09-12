"""
if word has more uppercase, convert whole word into uppercase, and vice-versa.
if equal, then lowercase.
"""
word = input().strip()

upperc = 0
lowerc = 0

for char in word:
    if char.isupper():
        upperc += 1
    else:
        lowerc += 1
if upperc > lowerc:
    print(word.upper())
else:
    print(word.lower())

