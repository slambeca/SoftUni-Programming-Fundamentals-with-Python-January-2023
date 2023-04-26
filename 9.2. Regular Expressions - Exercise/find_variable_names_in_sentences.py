# Remove the underscore in front of the valid variable names
import re

text = input()

pattern = r"\ "

matches = re.findall(pattern, text)

print(",".join(matches))

# Variant 2 with negative look behind
# import re
#
# pattern = r"(?<!_)_{1}([A-Za-z0-9]+\b)"
#
# line = input()
#
# matches = re.findall(pattern, line)
#
# if matches:
#     print(",".join(matches))