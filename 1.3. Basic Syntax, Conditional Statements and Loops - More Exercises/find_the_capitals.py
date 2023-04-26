string = input()

my_list = []

for i in range(len(string)):
    if string[i].isupper():
        my_list.append(i)

print(my_list)

# Variant 2
# string = input()
#
# my_list = []
#
# for i in range(len(string)):
#     if ord("A") <= ord(string[i]) <= ord("Z"):
#         my_list.append(i)    # we append the indexes of the capital letters of the string to the list
#
# print(my_list)

# Variant e, not for Judge
# string = input()
#
# my_list = []
#
# for i in range(len(string)):
#     if ord("A") <= ord(string[i]) <= ord("Z"):
#         my_list.append(string[i])    # we append the capital letters from the string to the list, not their indexes
#
# print(my_list)


