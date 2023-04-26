numbers = input().split(", ")

numbers_as_integers = []

list_positives = []
list_zeros = []

for number in numbers:
    numbers_as_integers.append(int(number))    # [1, 0, 1, 2, 0, 1, 3]

for num in numbers_as_integers:
    if num != 0:
        list_positives.append(num)
    else:
        list_zeros.append(num)

final_list = list_positives + list_zeros

print(final_list)