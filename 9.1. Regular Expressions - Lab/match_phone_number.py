import re

phone_numbers = input()

pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
# with group \+359( |-)2\1d{3}\1\d{4}\b
# pattern = r"(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4}\\b"

# \+(\d{3})([ -])\d\2\d{3}\2\d{4}\b -> this one works in regex101, but not in Judge

result = re.findall(pattern, phone_numbers)

print(", ".join(result))
# print(*result, sep=", ")