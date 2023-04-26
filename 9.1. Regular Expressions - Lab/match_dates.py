import re

text = input()

pattern = r"(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"
# No need for \/, only / works
# \2 is for applying group 2 again ([\/.-])


result = re.findall(pattern, text)

for match in result:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")

# Variant 2
# import re
#
# text = input()
#
# pattern = r"\b(?P<Day>\d{2})([\./-])(?P<Month>[A-Z][a-z][a-z])\2(?P<Year>\d{4})\b"
#
# matches = re.findall(pattern, text)
#
# for match in matches:
#     print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
#
# # Variant 3
# import re
#
# pattern = r"\b(?P<Day>\d{2})([\./-])(?P<Month>[A-Z][a-z][a-z])\2(?P<Year>\d{4})\b"
#
# text = input()
#
# dates = re.finditer(pattern, text)
#
# for date in dates:
#     date_data = date.groupdict()
#     print(f"Day: {date_data['Day']}, Month: {date_data['Month']}, Year: {date_data['Year']}")