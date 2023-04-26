user_input = input().split()    # turn string input directly into list

list_of_opposites = []

for i in range(len(user_input)):
    list_of_opposites.append(-int(user_input[i]))    # add opposite int values of user_input list to opposites list

print(list_of_opposites)

# Variant 2
# list_of_numbers = input().split()
#
# opposite_numbers = []
#
# for element in list_of_numbers:
#     current_number = -int(element)
#     opposite_numbers.append(current_number)
#
# print(opposite_numbers)
#
# # Variant 3
# string = input().split()
#
# result = []
#
# for element in string:
#     result.append(-int(element))
#
# print(result)
#
# # Variant 4 with LIST COMPREHENSION
# string = input().split()
#
# print([int(num) * -1 for num in string])    # int(num) because num is still a str
