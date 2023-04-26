numbers = [float(x) for x in input().split(" ")]    # [1.0, 2.5, 3.0, 4.5]

rounded_numbers = []

for i in numbers:
    rounded_numbers.append(round(i))


print(rounded_numbers)

# Variant 2
# result = list(map(lambda x: round(float(x)), input().split()))
#
# print(result)