import sys
from sys import maxsize

divisor = int(input())
boundary = int(input())

largest_integer = -sys.maxsize

for num in range(0, boundary + 1):
    if num % divisor == 0 and boundary >= num > 0:
        largest_integer = num

print(largest_integer)

# Variant 2
# divisor = int(input())
# max_number = int(input())
#
# for num in range(max_number, 0, -1):
#     if num % divisor == 0:
#         print(num)    # we find the biggest number, no need for another iterations
#         break