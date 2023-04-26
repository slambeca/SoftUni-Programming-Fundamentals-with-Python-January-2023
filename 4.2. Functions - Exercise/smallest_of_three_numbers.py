def smallest_number(first, second, third):
    """This function prints the smallest number of three."""
    if first < second and first < third:
        return first
    elif second < first and second < third:
        return second
    return third


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(smallest_number(first_num, second_num, third_num))
# print(smallest_number.__doc__)    # This function prints the smallest number of three.

# Variant 2 using a list and min()
#
#
# def smallest_number(numbers):
#     """This function prints the smallest number of three."""
#     return min(numbers)
#
#
# first_num = int(input())
# second_num = int(input())
# third_num = int(input())
#
# all_numbers = [first_num, second_num, third_num]
# min_number = smallest_number(all_numbers)
#
# print(min_number)
#
# # Variant 3 without function, only min()
# first_num = int(input())
# second_num = int(input())
# third_num = int(input())
#
# all_numbers = [first_num, second_num, third_num]
#
# min_number = min(all_numbers)
#
# print(min_number)
#
# # Variant 4 with one function
#
#
# def add(a, b):
#     """This function adds two numbers."""
#     return a + b
#
#
# first_num = int(input())
# second_num = int(input())
# third_num = int(input())
#
# print(add(first_num, second_num) - third_num)