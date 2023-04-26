# factorial number of 5 is 120 = 1 * 2 * 3 * 4 * 5
# factorial number of 6 is 720 = 1 * 2 * 3 * 4 * 5 * 6
import math


def find_factorial(num1, num2):
    """A function that does factorial division."""
    result_one = math.factorial(num1)
    result_two = math.factorial(num2)
    final_result = result_one / result_two

    return f"{final_result:.2f}"


first_num = int(input())
second_num = int(input())

print(find_factorial(first_num, second_num))

# Variant 2 without math module
#
#
# def factorial(number):
#     """A function that does factorial division."""
#     result = 1
#     for current_number in range(1, number + 1):   # or for current_number in range(1, number):
#         result *= current_number                  # number *= current_number
#                                                   # return number
#     return result
#
#
# first_number = int(input())
# second_number = int(input())
#
# first_num_factorial = factorial(first_number)
# second_num_factorial = factorial(second_number)
#
# final_result = first_num_factorial / second_num_factorial
#
# print(f"{final_result:.2f}")