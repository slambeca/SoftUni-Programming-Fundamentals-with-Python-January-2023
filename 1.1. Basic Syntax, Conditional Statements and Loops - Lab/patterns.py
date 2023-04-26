number = int(input())

for x in range(1, number + 1):    # this is half the pattern
    for y in range(0, x):
        print("*", end="")
    print()
for i in range(number - 1, 0, -1):    # this is the other half of the pattern
    for j in range(0, i):
        print("*", end="")
    print()

# Variant 2
# maximum_stars = int(input())
#
# for x in range(1, maximum_stars + 1):
#     print("*" * x)
#
# for y in range(maximum_stars - 1, 0, -1):
#     print("*" * y)