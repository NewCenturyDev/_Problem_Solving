raw_input = input()
word = raw_input.upper()

alphabet = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
    'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
    'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
    'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
    'Y': 0, 'Z': 0
}

for char in word:
    alphabet[char] += 1

max_char_key = None
max_char_cnt = None
for key, value in alphabet.items():
    if (max_char_cnt is None) or (value > max_char_cnt):
        max_char_key = key
        max_char_cnt = value

max_key_cnt = 0
for key, value in alphabet.items():
    if value == alphabet[max_char_key]:
        max_key_cnt += 1
if max_key_cnt != 1:
    print("?")
else:
    print(max_char_key)
