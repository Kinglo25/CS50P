word = input("camelCase: ").strip()
i = 0
for letter in word:
    if (letter.isupper()):
        word = word[:i] + '_' + word[i:]
        i += 1
    i += 1
print(word.lower())
