x = input("Enter the word: ")

vowels = list("aeiou")
consonants = list("bcdfghjklmnpqrstvwxyz")

y = {"vowels" : 0, "consonants": 0, "upper" : 0, "lower" : 0}

for i in x:
    if i in vowels:
        y["vowels"] += 1
    if i in consonants:
        y["consonants"] += 1
    if i == i.upper():
        y["upper"] += 1
    elif i == i.lower():
        y["lower"] += 1

print(y)
    
