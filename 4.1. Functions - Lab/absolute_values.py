# input is -0 1 10 -6.66
numbers = [abs(float(x)) for x in input().split()]    # this is not a good practice!

print(numbers)    # [0.0, 1.0, 10.0, 6.66]

# Variant 2
# numbers = input().split()
#
# abs_numbers = []
#
# for num in numbers:
#     abs_numbers.append(abs(float(num)))
#
# print(abs_numbers)
#
# # Variant 3
# numbers = list(map(float, input().split()))
#
# result = [abs(num) for num in numbers]
#
# print(result)