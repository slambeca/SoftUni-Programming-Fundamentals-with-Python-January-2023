word = input()

reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print(reversed_word)

# Variant 2
# word = input()
#
# for index in range(len(word) -1, -1, -1):
#     print(word[index], end='')
#
# # Variant 3
# word = input()
# print(word[::-1])
