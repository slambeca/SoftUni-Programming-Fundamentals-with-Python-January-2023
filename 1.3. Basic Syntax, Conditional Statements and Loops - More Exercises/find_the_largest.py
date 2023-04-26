number = input()

largest_number = []

for digit in number:
    digit = int(digit)

    largest_number.append(digit)

largest_number.sort()

print(*largest_number[::-1], sep="")

# Variant 2
# number = int(input())
#
# print(int("".join(sorted(str(number))[::-1])))