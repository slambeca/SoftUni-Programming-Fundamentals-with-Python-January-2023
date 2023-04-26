number_sequence = [int(num) for num in input().split()]    # [2, 4, 6]

min_number = min(number_sequence)
max_number = max(number_sequence)
sum_numbers = sum(number_sequence)

print(f"The minimum number is {min_number}\nThe maximum number is {max_number}\nThe sum number is: {sum_numbers}")

# Variant 2 with functions
#
#
# def min_func(numbers):
#     """This function returns the minimum from a list of numbers."""
#     return min(numbers)
#
#
# def max_number(numbers):
#     """This function returns the maximum from a list of numbers."""
#     return max(numbers)
#
#
# def sum_numbers(numbers):
#     """This function returns the sum of all numbers in a list."""
#     return sum(numbers)
#
#
# number_sequence = [int(num) for num in input().split()]    # [2, 4, 6]
#
# min_number = min_func(number_sequence)
# max_number = max_number(number_sequence)
# sum_numbers = sum_numbers(number_sequence)
#
# print(f"The minimum number is {min_number}\nThe maximum number is {max_number}\nThe sum number is: {sum_numbers}")