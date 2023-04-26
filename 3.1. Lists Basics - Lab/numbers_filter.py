n = int(input())

numbers = []    # first we create an empty list
filtered = []    # then we create a list which will be our final result

for _ in range(n):
    current_number = int(input())

    numbers.append(current_number)    # for each iteration we add the current_number in our first list

command = input()

if command == "even":    # we check the command and iterate through our list of numbers
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)    # with each iteration, if the condition is met, we add the number to the result
elif command == "odd":
    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)
elif command == "negative":
    for number in numbers:
        if number < 0:
            filtered.append(number)
else:
    for number in numbers:
        if number >= 0:
            filtered.append(number)

print(filtered)

# Variant 2 with constant values
# number_of_lines = int(input())
#
# # constant values
# COMMAND_EVEN = "even"
# COMMAND_ODD = "odd"
# COMMAND_POSITIVE = "positive"
# COMMAND_NEGATIVE = "negative"
#
# numbers = []
#
# for _ in range(number_of_lines):
#     current_number = int(input())
#     numbers.append(current_number)
#
# command = input()
#
# filtered_numbers = []
#
# # number filtering
# for number in numbers:
#     filtered_passes = (    # or call it condition
#         (command == COMMAND_EVEN and number % 2 == 0) or
#         (command == COMMAND_ODD and number % 2 != 0) or
#         (command == COMMAND_NEGATIVE and number < 0) or
#         (command == COMMAND_POSITIVE and number >= 0)
#     )
#     if filtered_passes:    # if condition
#         filtered_numbers.append(number)
#
# print(filtered_numbers)
#
# # Variant 3
# n = int(input())
#
# positive_nums = []
# negatives_nums = []
# even_nums = []
# odd_nums = []
#
# for _ in range(n):
#     current_number = int(input())
#
#     if current_number >= 0:
#         positive_nums.append(current_number)
#     else:
#         negatives_nums.append(current_number)    # if < 0
#
#     if current_number % 2 == 0:
#         even_nums.append(current_number)
#     else:    # if % 2 != 0
#         odd_nums.append(current_number)
#
# command = input()
#
# if command == "even":
#     print(even_nums)
# elif command == "odd":
#     print(odd_nums)
# elif command == "positive":
#     print(positive_nums)
# else:
#     print(negatives_nums)
#
# # Variant 4
# number = int(input())
#
# all_numbers = []
# filtered_numbers = []
#
# for _ in range(number):
#     integer = int(input())
#
#     all_numbers.append(integer)
#
# command = input()
#
# for number in all_numbers:
#     if command == "positive":
#         if number >= 0:
#             filtered_numbers.append(number)
#     elif command == "negative":
#         if number < 0:
#             filtered_numbers.append(number)
#     elif command == "even":
#         if number % 2 == 0:
#             filtered_numbers.append(number)
#     else:
#         if number % 2 != 0:
#             filtered_numbers.append(number)
#
# print(filtered_numbers)