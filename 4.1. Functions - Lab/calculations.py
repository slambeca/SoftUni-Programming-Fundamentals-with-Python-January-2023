input_operation = input()
first_num = int(input())
second_num = int(input())


def my_func(x, y):
    """This function makes simple calculations."""
    if input_operation == "multiply":
        return x * y
    elif input_operation == "divide":
        return int(x / y)
    elif input_operation == "add":
        return x + y
    else:
        return x - y


print(my_func(first_num, second_num))

# Variant 2
# input_operator = input()
# first_num = int(input())
# second_num = int(input())
#
#
# def solve(a, b, operator):
#     """This function makes simple calculations."""
#     result = None
#     if operator == "multiply":
#         result = a * b
#     elif operator == "divide":
#         result = int(a / b)    # or a // b
#     elif operator == "add":
#         result = a + b
#     elif operator == "subtract":
#         result = a - b
#     return result
#
#
# print(solve(first_num, second_num, input_operator))