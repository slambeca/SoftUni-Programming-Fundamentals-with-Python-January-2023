number_sequence = input().split()

numbers_as_digits = []

for number in range(len(number_sequence)):
    numbers_as_digits.append(int(number_sequence[number]))

sorted_numbers = sorted(numbers_as_digits)

print(sorted_numbers)

# Variant 2
#
#
# def sort_func(numbers):
#     """This function sorts a given list with numbers."""
#     return sorted(numbers)
#
#
# number_sequence = input().split()
#
# numbers_as_digits = []
#
# for number in range(len(number_sequence)):
#     numbers_as_digits.append(int(number_sequence[number]))
#
# print(sort_func(numbers_as_digits))    # [2, 8, 11, 12, 45, 52, 53]