word = input()
result = ""
for char in word:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
    else:
        result += char
print(result)
