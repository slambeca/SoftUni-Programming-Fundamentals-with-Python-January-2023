to_do_list = [0] * 10    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

command = input()

while command != "End":
    importance, task = command.split("-")
    importance = int(importance)

    index = importance - 1   # because the indexes in the list start from 0, in our input the numbers start from 1

    to_do_list[index] = task

    command = input()

print([task for task in to_do_list if task != 0])

# Variant 2
# command = input()
#
# to_do_list = [0] * 10
#
# while command != "End":
#     command_args = command.split("-")
#     priority = int(command_args[0])
#     type_of_action = command_args[1]
#
#     to_do_list[priority - 1] = type_of_action    # insert this action at this index in the list
#
#     command = input()
#
# print([x for x in to_do_list if x != 0])