numbers = [int(number) for number in input().split()]
k_number = int(input())

new_list = []

counter = 0
index = 0

while len(numbers) > 0:    # do this until there are people left in the circle
    counter += 1

    if counter % k_number == 0:    # a person is being killed
        new_list.append(numbers[index])    # we add the killed person to the new_list
        numbers.pop(index)    # we remove the person from the initial list

    elif counter % k_number != 0:
        index += 1

    if index >= len(numbers):    # we are restarting the index, if it goes to the end
        index = 0

print(str(new_list).replace(' ', ''))

# Variant 2
# inpt = input().split()
# movingPositions = int(input())
#
# listNumbers = []
# result = []
#
# counter = 0
# index = 0
#
# for i in inpt:
#     listNumbers.append(int(i))
#
# while len(listNumbers) != 0:
#     counter += 1
#     if counter % movingPositions == 0:
#         result.append(listNumbers[index])
#         listNumbers.pop(index)
#     elif counter % movingPositions != 0:
#         index += 1
#
#     if index >= len(listNumbers):
#         index = 0
#
# print(str(result).replace(' ', ''))