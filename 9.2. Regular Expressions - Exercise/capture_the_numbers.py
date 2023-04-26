import re

pattern = "\d+"

line = input()

while line:
    matches = re.findall(pattern, line)

    if matches:
        print(" ".join(matches), end=" ")

    line = input()

# Variant 2
# import re
#
# numbers = []
#
# pattern = r"\d+"
# # pattern = r"[0-9]+"
#
# while True:
#     line = input()
#
#     if not line:
#         break
#
#     matches = re.findall(pattern, line)
#     # matches = re.findall("\\d+", line)
#     # matches = re.findall(r"\d", line)
#
#     numbers.extend(matches)
#
# print(" ".join(numbers))