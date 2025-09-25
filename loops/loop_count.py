str = "! i like python 3.13 programming @ #5$ 5"
digits ="1234567890"
vowels="aeiouAEIOU"
chars ="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
specials = "~!@#$%^&*(){}[]"

digit = 0
vowel = 0
special =0
char = 0

for i in str :
    if i in digits:
        digit = digit + 1
    elif i in vowels :
        vowel=vowel+1
    elif i in specials :
        special = special + 1
    else:
        chars = chars + i