import re

text = input()

searched_word = input()

pattern = fr"\b{searched_word}\b"
# pattern = fr"(?i)\b{searched_word}\b" -> (?i) is for IGNORECASE

matches = re.findall(pattern, text, flags=re.IGNORECASE)
# matches = re.findall(pattern, text)

print(len(matches))

# Variant 2
# import re
#
# text = input().lower()
# target = input().lower()
#
# pattern = fr"\b{target}\b"
#
# matches = re.findall(pattern, text)
#
# print(len(matches))