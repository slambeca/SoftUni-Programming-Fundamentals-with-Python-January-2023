number_sequence = [int(num) for num in input().split()]

result = filter(lambda x: x % 2 == 0, number_sequence)

print(list(result))

# Variant 2 with a function and list comprehension
#
#
# def even_numbers(num):
#     """A function that checks for even numbers."""
#     if num % 2 == 0:
#         return True
#
#     return False
#
#
# number_sequence = [int(num) for num in input().split()]
#
# print(list(filter(even_numbers, number_sequence)))
#
# # Variant 3
#
#
# def is_even(num):
#     current_result = num % 2 == 0
#     return current_result
#
#
# nums = [int(num) for num in input().split()]
# print(list(filter(is_even, nums)))