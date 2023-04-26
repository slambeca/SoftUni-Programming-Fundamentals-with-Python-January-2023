def sum_numbers(num1, num2):
    """This function sums two numbers."""
    result = num1 + num2
    return result


def subtract(sum, third):
    """This function subtracts two numbers - the result from the first and the third_num."""
    result = sum - third
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(subtract(sum_numbers(first_num, second_num), third_num))

# Variant 2 with 3 functions as per the exercise
#
#
# def sum_numbers(first, second):
#     """This function sums two numbers."""
#     return first + second
#
#
# def subtract(sum_first_second, third):
#     """This function subtracts two numbers."""
#     return sum_first_second - third
#
#
# def add_and_subtract(first, second, third):
#     """This function adds and subtracts."""
#     sum_of_first_and_second = sum_numbers(first, second)
#     result = subtract(sum_of_first_and_second, third)
#     return result
#
#
# first_num = int(input())
# second_num = int(input())
# third_num = int(input())
#
# print(add_and_subtract(first_num, second_num, third_num))
#
# # Variant 3 with eval()
# first_num = int(input())
# second_num = int(input())
# third_num = int(input())
#
# sum_first_second_numbers = eval("first_num + second_num")
# subtract_sum_third = eval("sum_first_second_numbers - third_num")
#
# print(subtract_sum_third)
#
# # Variant 4 - the simplest
# first_number, second_number, third_number = int(input()), int(input()), int(input())
#
# sum_first_two = first_number + second_number
# subtraction = sum_first_two - third_number
#
# print(subtraction)