def perfect_number_check(num):    # perfect numbers are 6 = 1 + 2 + 3 = 6, 28 = 1 + 2 + 4 + 7 + 14 = 28
    """This functions searches for a perfect number."""
    total_sum = 0                 # other perfect numbers are 496 and 8128
    for x in range(1, num):    # 6 is exclusive
        if num % x == 0:
            total_sum += x

    return total_sum == num    # returns True if total_sum is equal to num, 6 = 1 + 2 + 3


number = int(input())

result = perfect_number_check(number)

if result:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

# Variant 2, which is shorter
#
#
# def is_perfect(some_number):
#     """This functions searches for a perfect number."""
#     total_sum = 0
#     for divisor in range(1, some_number):    # or ((some_number // 2) + 1)
#         if some_number % divisor == 0:
#             total_sum += divisor
#
#     if total_sum == some_number:
#         return "We have a perfect number!"
#
#     return "It's not so perfect."
#
#
# number = int(input())
#
# print(is_perfect(number))