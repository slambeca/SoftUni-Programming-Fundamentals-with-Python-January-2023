number_of_wagons = int(input())

train = [0] * number_of_wagons    # [0, 0, 0]

# for i in range(number_of_wagons):
#     train.append(0)

command = input()

while command != "End":
    action = command.split()[0]

    if action == "add":    # if command startswith "add"
        number_of_people = int(command.split()[1])
        train[-1] += number_of_people
    elif action == "insert":
        index = int(command.split()[1])
        number_of_people = int(command.split()[2])
        train[index] += number_of_people
    elif action == "leave":
        index = int(command.split()[1])
        number_of_people = int(command.split()[2])
        train[index] -= number_of_people

    command = input()

print(train)

# Variant 2
# number_of_wagons = int(input())
#
# train = []
#
# for wagon in range(number_of_wagons):
#     train.append(0)
#
# command = input()
#
# while command != "End":
#     command_args = command.split()
#
#     type_of_command = command_args[0]
#
#     if type_of_command == "add":
#         number_of_people = int(command_args[1])
#         train[-1] += number_of_people
#     elif type_of_command == "insert":
#         wagon_index = int(command_args[1])
#         number_of_people = int(command_args[2])
#         train[wagon_index] += number_of_people
#     elif type_of_command == "leave":
#         wagon_index = int(command_args[1])
#         number_of_people = int(command_args[2])
#         train[wagon_index] -= number_of_people
#
#     command = input()
#
# print(train)