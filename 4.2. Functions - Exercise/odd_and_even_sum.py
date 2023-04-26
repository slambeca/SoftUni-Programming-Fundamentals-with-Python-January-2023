# Test with sys module and sys.stdout.write() instead of print()
import sys


def even_odd_sums(number):
    """This function sums the even and the odd numbers from an integer."""
    even_numbers = 0
    odd_numbers = 0
    for digit in str(number):
        current_digit = int(digit)
        if current_digit % 2 == 0:
            even_numbers += current_digit
        else:
            odd_numbers += current_digit

    result = f"Odd sum = {odd_numbers}, Even sum = {even_numbers}"
    return result


received_number = int(input())

sys.stdout.write(even_odd_sums(received_number))

# Variant 2
#
#
# def even_odd_numbers(number):
#     """This function sums the even and the odd numbers from an integer."""
#     sum_odd_numbers = 0
#     sum_even_numbers = 0
#     for digit in number:
#         if int(digit) % 2 == 0:
#             sum_even_numbers += int(digit)
#         else:
#             sum_odd_numbers += int(digit)
#
#     return sum_odd_numbers, sum_even_numbers    # the return can give us multiple variables, not just one
#
#
# number_as_string = input()
#
# sum_odd_numbers, sum_even_numbers = even_odd_numbers(number_as_string)    # odd should be first, even second, as it`s
# # in the function`s return statement
#
# print(f"Odd sum = {sum_odd_numbers}, Even sum = {sum_even_numbers}")