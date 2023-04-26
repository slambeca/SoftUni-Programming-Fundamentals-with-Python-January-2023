first_string, second_string = input().split()

total_sum = 0

if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):    # this is the remaining range
        total_sum += ord(first_string[index])    # we are adding the ord value from the ASCII table
elif len(first_string) < len(second_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])
else:    # len(first_string) == len(second_string):
    for index in range(len(first_string)):    # or len(second_string), because they are equal
        total_sum += ord(first_string[index]) * ord(second_string[index])

print(total_sum)