string_one = input().split(", ")
string_two = input().split(", ")

new_list = []

for x in string_one:
    for y in string_two:
        if x in y:
            new_list.append(x)

list_as_set = set(new_list)

set_as_list = list(list_as_set)

print(sorted(set_as_list))    # ['arp', 'live', 'strong']

# This may not work correctly, because the result should not be sorted

# Variant 2
# string_one = input().split(", ")
# string_two = input().split(", ")
#
# new_list = []
#
# for x in string_one:
#     for y in string_two:
#         if x in y:    # and x not in new_list:
#             if x not in new_list:
#                 new_list.append(x)
#
# print(new_list)
#
# # Variant 3 with break
# string_one = input().split(", ")
# string_two = input().split(", ")
#
# new_list = []
#
# for x in string_one:
#     for y in string_two:
#         if x in y:
#             new_list.append(x)
#             break    # this will return only the first occurrence
#
# print(new_list)
#
# # Variant 4 with list comprehension, not recommended
# first_sequence = input().split(", ")
# second_sequence = input().split(", ")
#
# substrings = [first for first in first_sequence if any(first in second for second in second_sequence)]
#
# print(substrings)
#
# # Variant 5
# first_list = input().split(", ")
# second_list = input().split(", ")
#
# result = []
#
# for substr in first_list:
#     for word in second_list:
#         found_substr = substr in word
#         if found_substr:
#             result.append(substr)
#             break
#
# print(result)