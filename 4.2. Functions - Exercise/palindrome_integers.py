def palindrome_check(numbers):
    """This function checks for palindrome numbers."""
    for num in numbers:
        if str(num) == str(num)[::-1]:
            print("True")
        else:
            print("False")


input_numbers = [int(num) for num in input().split(", ")]

palindrome_check(input_numbers)

# Variant 2
# from typing import List
#
#
# def check_palindrome(numbers: List[str]) -> List[str]:
#     bool_list = []
#     for number in numbers:
#         if number == number[::-1]:
#             bool_list.append("True")
#         else:
#             bool_list.append("False")
#
#     return bool_list
#
#
# numbers_list = input().split(", ")
# result = check_palindrome(numbers_list)
#
# print("\n".join(result))