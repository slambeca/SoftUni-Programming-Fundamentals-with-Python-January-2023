# Extract emojis from a text and find the threshold based on the input
import re

cool_emojis = []    # Should have sum(ord(ch)) >= cool_treshold
found_emojis = []    # List of all valid emojis that are valid according to our pattern

cool_treshold = 1    # Should not be 0!

pattern = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"

text = input()

for char in text:
    if char.isdigit():
        cool_treshold *= int(char)    # 540

result = re.finditer(pattern, text)

for item in result:
    found_emojis.append(item.group())
    current_score = 0
    for ch in item.group():
        if ch != ":" and ch != "*":
            current_score += ord(ch)
    if current_score >= cool_treshold:
        cool_emojis.append(item.group())


print(f"Cool threshold: {cool_treshold}")
print(f"{len(found_emojis)} emojis found in the text. The cool ones are:")
if cool_emojis:
    for emoji in cool_emojis:
        print(emoji)

# # Variant 2
#
#
# def calculate_cool_treshold(data):
#     result = 1
#
#     for word in data:
#         for character in word:
#             if character.isdigit():
#                 result *= int(character)
#
#     return result
#
#
# def find_valid_emojis(data):
#     valid_emojis = []
#
#     for word in data:
#         if word[0] in (':', '*'):
#             reversed_word = word[::-1]
#             if (word[0] == word[1]) and (word[0] == reversed_word[0]) and (word[0] == reversed_word[1]):
#                 if word[2].isalpha() and word[2].isupper():
#                     if len(word[2:-1 - 1]) >= 3:
#                         if word[3:-1 - 1].isalpha() and word[3:-1 - 1].islower():
#                             valid_emojis.append(word)
#
#     return valid_emojis
#
#
# def calculate_emojis_coolnes(emojis):
#     cool_emojis = {}
#
#     for emoji in emojis:
#         emoji_coolness = 0
#         for char in emoji:
#             if char.isalpha():
#                 emoji_coolness += ord(char)
#         cool_emojis[emoji] = emoji_coolness
#
#     return cool_emojis
#
#
# data = input().replace(',', '').replace('.', '').split()
# cool_threshold = calculate_cool_treshold(data)
# emojis = find_valid_emojis(data)
# emojis_coolness = calculate_emojis_coolnes(emojis)
#
# print(f'Cool threshold: {cool_threshold}')
# print(f'{len(emojis)} emojis found in the text. The cool ones are:')
# for emoji, coolness in emojis_coolness.items():
#     if coolness >= cool_threshold:
#         print(emoji)
#
# # Variant 3
# import re
#
# txt = input()
# threshold = 1
#
# digits = re.findall(r"\d", txt)
# emojis = re.findall(r"\*\*[A-Z][a-z]{2,}\*\*|::[A-Z][a-z]{2,}::", txt)
# emojis_for_print = []
#
# for digit in digits:
#     digit = int(digit)
#     threshold *= digit
#
# print(f"Cool threshold: {threshold}")
#
# for index in range(len(emojis)):
#     emoji_sum = 0
#     for element in emojis[index]:
#         if element == ':' or element == "*":
#             continue
#         else:
#             emoji_sum += ord(element)
#     if emoji_sum > threshold:
#         emojis_for_print.append(emojis[index])
#
# print(f"{len(emojis)} emojis found in the text. The cool ones are:")
#
# for emoji in emojis_for_print:
#     print(emoji)
