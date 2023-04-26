numbers = input().split()    # ['10', '9', '8', '7', '6', '5']
count_numbers_to_remove = int(input())    # 3

numbers_as_integers = []    # [10, 9, 8, 7, 6, 5]

for number in numbers:
    numbers_as_integers.append(int(number))

for i in range(count_numbers_to_remove):
    numbers_as_integers.remove(min(numbers_as_integers))

print(*numbers_as_integers, sep=", ")    # 10, 9, 8

# Using the * symbol to print a list in Python. To print the contents of a list in a single line with space, * or
# splat operator is one way to go. It passes all the contents of a list to a function. We can print all elements
# in new lines or separated by space and to do that, we use sep=”\n” or sep=”, ” respectively.

# Variant 2
# numbers = [int(x) for x in input().split()]
# count = int(input())
#
# for _ in range(count):
#     number_to_remove = min(numbers)
#     numbers.remove(number_to_remove)
#
# for idx in range(len(numbers)):
#     num = numbers[idx]
#     if idx == len(numbers) - 1:
#         print(num)
#     else:
#         print(num, end=", ")
#
# # Variant 3
# # Survival of the biggest
# numbers = [int(x) for x in input().split()]    # [10, 9, 8, 7, 6, 5]
# count = int(input())   # 3
#
# for num in range(count):
#     smallest_number = min(numbers)
#
#     numbers.remove(smallest_number)
#
# print(*numbers, sep=", ")