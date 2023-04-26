number = int(input())

for x in range(97, 97 + number):
    for y in range(97, 97 + number):
        for z in range(97, 97 + number):
            print(f"{chr(x)}{chr(y)}{chr(z)}")

# Variant 2
# number = int(input())
#
# for x in range(97, 97 + number):
#     for y in range(97, 97 + number):
#         for z in range(97, 97 + number):
#             print(chr(x), chr(y), chr(z), sep="")
#
# # Variant 3
# n = int(input())
#
# start = 97
#
# for first in range(start, start + n):
#     for second in range(start, start + n):
#         for third in range(start, start + n):
#             print(chr(first), chr(second), chr(third), sep="")