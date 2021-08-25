s = "3people unFoll3owed me"

words = s.split(" ")
print(words)

result = ""
for word in words:
    if word[0].isalpha():
        word = word[0].upper() + word[1:].lower()
    else:
        word = word.lower()
    result = result + word + " "
result = result[:-1]
print(result)