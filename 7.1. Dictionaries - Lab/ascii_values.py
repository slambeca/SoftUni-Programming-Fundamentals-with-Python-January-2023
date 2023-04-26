letters = input().split(", ")    # ['a', 'b', 'c', 'a']

ascii_values = {}

for letter in range(len(letters)):
    key = letters[letter]
    value = ord(key)
    ascii_values[key] = int(value)

print(ascii_values)

# Variant 2 with dictionary comprehension
# letters = input().split(", ")    # ['a', 'b', 'c', 'a']
#
# dictionary = {key: (ord(key)) for key in letters}
#
# print(dictionary)
#
# # 100/100 in Judge
#
# # Variant 3 - shortest
# print({key: int(ord(key)) for key in input().split(", ")})