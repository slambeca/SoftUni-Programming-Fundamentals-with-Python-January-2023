input_line = input()   # Programming is cool!

result = []

for letter in input_line:
    result.append(chr(ord(letter) + 3))

print(*result, sep="")

# Variant 2 with list comprehension, list unpacking and join
# print(*[''.join(chr(ord(letter) + 3) for letter in input())])