s = " adgagd 3eagdag "

words = s.split(" ")
print(words)

result = ""
for word in words:
    print(word)
    if word == '':
        pass
    elif word[0].isalpha():
        word = word[0].upper() + word[1:].lower()
    else:
        word = word.lower()
    result += word + " "
result = result[:-1]
print(result)