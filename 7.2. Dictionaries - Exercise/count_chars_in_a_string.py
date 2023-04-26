text = input()

dictionary = {}

for letter in text:
    if letter != " ":
        if letter not in dictionary.keys():
            dictionary[letter] = 0

        dictionary[letter] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")

# Variant 2
# text = input().replace(" ", "")
#
# dictionary = {}
#
# for letter in text:
#     if letter not in dictionary.keys():
#         dictionary[letter] = 0
#
#     dictionary[letter] += 1
#
# for key, value in dictionary.items():
#     print(f"{key} -> {value}")
#
# # Variant 3
# text = "".join(input().split())
#
# dictionary = {}
#
# for letter in text:
#     if letter not in dictionary.keys():
#         dictionary[letter] = 0
#
#     dictionary[letter] += 1
#
# for key, value in dictionary.items():
#     print(f"{key} -> {value}")
#
# # Variant 4
# words = input().split()
#
# count_by_letter = {}
#
# for word in words:
#     for letter in word:
#         if letter in count_by_letter:
#             count_by_letter[letter] += 1
#         else:
#             count_by_letter[letter] = 1
#
# for key, value in count_by_letter.items():
#     print(f"{key} -> {value}")
#
# # for letter in count_by_letter:
# #     print(f"letter" -> {count_by_letter[letter]}")