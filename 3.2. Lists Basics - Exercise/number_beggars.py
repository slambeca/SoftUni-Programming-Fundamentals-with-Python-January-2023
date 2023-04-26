money_list = input().split(", ")    # ["1", "2", "3", "4", "5"]
money_list_as_digit = []

for element in money_list:
    money_list_as_digit.append(int(element))    # we convert the elements from strings to numbers
    # [1, 2, 3, 4, 5]

count_of_beggars = int(input())

final_sums = []    # this is our final print

starting_index = 0

while starting_index < count_of_beggars:
    sum_for_current_beggar = 0    # so that is shows 0 for the final beggar if there is no money for him

    for current_index in range(starting_index, len(money_list_as_digit), count_of_beggars):
        sum_for_current_beggar += money_list_as_digit[current_index]
    # we are using for loop so that we do not receive an IndexError

    final_sums.append(sum_for_current_beggar)
    starting_index += 1

print(final_sums)

# Variant 2
# numbers_list = [int(x) for x in input().split(", ")]
# number_of_beggars = int(input())
#
# beggars_list = [0] * number_of_beggars
#
# for num in range(len(beggars_list)):
#     current_beggar = num
#     for n in range(len(numbers_list)):
#         current_num = n % number_of_beggars
#         if current_num == current_beggar:
#             if beggars_list[num] == 0:
#                 if numbers_list[n] == 0:
#                     beggars_list[current_num] = 0
#                     break
#                 beggars_list[current_num] = numbers_list[n]
#             else:
#                 beggars_list[current_num] += numbers_list[n]
#
# print(beggars_list)
#
# # Variant 3
# string_of_integers = input().split(", ")    # ['1', '2', '3', '4', '5']
# beggars = int(input())
#
# money_list_as_digits = []    # [1, 2, 3, 4, 5]
#
# for element in string_of_integers:
#     money_list_as_digits.append(int(element))
#
# result = []
#
# for beggar in range(beggars):
#     current_sum = 0
#     for i in range(beggar, len(money_list_as_digits), beggars):
#         current_sum += money_list_as_digits[i]
#
#     result.append(current_sum)
#
# print(result)
#
# # Variant 4
# money = [int(x) for x in input().split(", ")]
#
# beggars_count = int(input())
#
# sums_for_beggars = [0] * beggars_count
#
# while len(money) != 0:
#     for beggar in range(beggars_count):
#         sums_for_beggars[beggar] += money[0]
#         money.pop(0)
#
#         if len(money) == 0:
#             break
#
# print(sums_for_beggars)
#
# # Variant 5
# numbers = input().split(", ")
# beggars_count = int(input())
#
# beggars = [0] * beggars_count    # [0] * 2 == [0, 0]
#
# for idx in range(len(numbers)):
#     beggar_idx = idx % beggars_count
#     num = int(numbers[idx])
#     beggars[beggar_idx] += num
#
# print(beggars)