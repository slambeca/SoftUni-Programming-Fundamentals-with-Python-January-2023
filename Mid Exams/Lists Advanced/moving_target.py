targets = [int(x) for x in input().split()]    # [52, 74, 23, 44, 96, 110]

while True:
    command = input()

    if command == "End":
        break

    command_args = command.split()
    type_of_command = command_args[0]
    index = int(command_args[1])
    value = int(command_args[2])

    if type_of_command == "Shoot":    # [52, 23, 44, 96, 100]
        if index in range(len(targets)):
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif type_of_command == "Add":    # or add check index here -> if command == "Add" and 0 <= index < len(targets):
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif type_of_command == "Strike":    # [52, 100]
        starting_index = index - value    # 1
        ending_index = index + value    # 3
        if starting_index in range(len(targets)) and ending_index in range(len(targets)):
            targets[starting_index:ending_index + 1] = []    # 3 is exclusive, so we add 1
        else:
            print(f"Strike missed!")

result = [str(x) for x in targets]
print("|".join(result))

# Variant 2
# targets = input().split(" ")
# targets = list(map(int, targets))
#
# line = input()
#
# while line != "End":
#     command_list = line.split(" ")
#     command = command_list[0]
#     index = int(command_list[1])
#     value = int(command_list[2])
#
#     if command == "Shoot" and 0 <= index < len(targets):
#         current_target = targets[index]
#         current_target -= value
#         if current_target <= 0:
#             targets.pop(index)
#         else:
#             targets[index] = current_target
#
#     elif command == "Add":
#         if 0 <= index < len(targets):
#             targets.insert(index, value)
#         else:
#             print("Invalid placement!")
#
#     elif command == "Strike":
#         if index - value >= 0 and index + value < len(targets):
#             targets = targets[:index - value] + targets[index + value + 1:]   # this way we are removing the middle part
#         else:
#             print("Strike missed!")
#
#     line = input()
#
# targets = list(map(str, targets))
# output = "|".join(targets)
# print(output)
#
# # Variant 3
#
#
# def shoot(targets, index, power):
#     if index in range(len(targets)):
#         if targets[index] > power:
#             targets[index] -= power
#         else:
#             del targets[index]
#
#
# def add(targets, index, value):
#     if index in range(len(targets)):
#         targets.insert(index, value)
#     else:
#         print('Invalid placement!')
#
#
# def strike(targets, index, radius):
#     start_index = index - radius
#     end_index = index + radius
#
#     if start_index in range(len(targets)) and end_index in range(len(targets)):
#         targets = targets[0:start_index] + targets[end_index + 1:]
#     else:
#         print('Strike missed!')
#
#     return targets
#
#
# sequence_of_targets = [int(target) for target in input().split()]
#
# while True:
#     command = input()
#
#     if command == 'End':
#         break
#
#     command = command.split()
#
#     if command[0] == 'Shoot':
#         index = int(command[1])
#         power = int(command[2])
#         shoot(sequence_of_targets, index, power)
#
#     elif command[0] == 'Add':
#         index = int(command[1])
#         value = int(command[2])
#         add(sequence_of_targets, index, value)
#
#     elif command[0] == 'Strike':
#         index = int(command[1])
#         radius = int(command[2])
#         sequence_of_targets = strike(sequence_of_targets, index, radius)
#
# print('|'.join(str(target) for target in sequence_of_targets))
