first_char = input()
second_char = input()
third_char = input()

print(f"{first_char}{second_char}{third_char}")    # this is not a concatenation

# Variant 2
# a = input()
# b = input()
# c = input()
#
# print(a + b + c)    # this is concatenation
#
# # With delimiter
# first_char = input()
# second_char = input()
# third_char = input()
#
# delimiter = input()
#
# result = first_char + delimiter + second_char + delimiter + third_char
#
# result2 = f"{first_char}{delimiter}{second_char}{delimiter}{third_char}"
#
# # Variant 3
# a = input()
# b = input()
# c = input()
#
# delimiter = input()
#
# print(a, b, c, sep=delimiter)
#
# # Variant 4
# a = input()
# b = input()
# c = input()
#
# print(a, b, c, sep="")