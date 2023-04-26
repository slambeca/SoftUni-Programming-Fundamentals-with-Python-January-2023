array_integers = [int(x) for x in input().split()]    # [23, -2, 321, 87, 42, 90, -123]

while True:
    command = input()

    if command == "end":
        break

    command_args = command.split()
    type_of_command = command_args[0]

    if type_of_command == "swap":
        first_index = int(command_args[1])
        second_index = int(command_args[2])
        array_integers[first_index], array_integers[second_index] = \
            array_integers[second_index], array_integers[first_index]

    elif type_of_command == "multiply":
        first_index = int(command_args[1])
        second_index = int(command_args[2])
        array_integers[first_index] *= array_integers[second_index]

    elif type_of_command == "decrease":
        for element in range(len(array_integers)):
            array_integers[element] -= 1

result = list(map(str, array_integers))

print(*result, sep=", ")

# Variant 2
# numbers = input().split(" ")
# numbers = list(map(int, numbers))
#
# command = input()
#
# while command != "end":
#     if command == "decrease":
#         numbers = list(map(lambda n: n - 1, numbers))  # instead of a for loop
#     else:
#         explode = command.split()
#         type_of_command = explode[0]
#         index1 = int(explode[1])
#         index2 = int(explode[2])
#
#         if type_of_command == "swap":
#             numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
#
#         elif type_of_command == "multiply":
#             numbers[index1] *= numbers[index2]
#
#     command = input()
#
# output = list(map(str, numbers))
# print(*output, sep=", ")
#
# # Variant 3
# initial_array = [int(x) for x in input().split()]
#
# command = input()
#
# while command != "end":
#     token = command.split()
#     cmd = token[0]
#
#     if cmd == "swap":
#         el_1 = int(token[1])
#         el_2 = int(token[2])
#         initial_array[el_1], initial_array[el_2] = initial_array[el_2], initial_array[el_1]
#     elif cmd == "multiply":
#         el_1 = int(token[1])
#         el_2 = int(token[2])
#         initial_array[el_1] = initial_array[el_1] * initial_array[el_2]
#     elif cmd == "decrease":
#         initial_array = [x - 1 for x in initial_array]
#     command = input()
# #print(f"{str(initial_array)[1:-1]}")
# print(', '.join(map(str, initial_array)))