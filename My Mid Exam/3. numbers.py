numbers_sequence = [int(num) for num in input().split()]

while True:
    input_line = input()

    if input_line == "Finish":
        break

    command_args = input_line.split()

    type_of_command = command_args[0]
    value_of_command = int(command_args[1])

    if type_of_command == "Add":
        numbers_sequence.append(value_of_command)

    elif type_of_command == "Remove":
        if value_of_command in numbers_sequence:
            numbers_sequence.remove(value_of_command)

    elif type_of_command == "Replace":
        replacement_value = int(command_args[2])
        if value_of_command in numbers_sequence:
            value_index = numbers_sequence.index(value_of_command)
            numbers_sequence[value_index] = replacement_value

    elif type_of_command == "Collapse":
        numbers_sequence = [int(num) for num in numbers_sequence if int(num >= value_of_command)]

print(*numbers_sequence)