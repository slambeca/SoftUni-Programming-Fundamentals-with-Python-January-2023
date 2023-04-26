first_number = int(input())
second_number = int(input())
third_number = int(input())

if first_number > second_number and first_number > third_number:
    print(first_number)
elif second_number > first_number and second_number > third_number:
    print(second_number)
else:
    print(third_number)


# Variant 2
# a, b, c = int(input()), int(input()), int(input())
#
# print(max(a, b, c))
#
# # Variant 3
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a <= b:
#     if b <= c:
#         print(c)
#     else:
#         print(b)
# elif a >= b:
#     if a <= c:
#         print(c)
#     else:
#         print(a)