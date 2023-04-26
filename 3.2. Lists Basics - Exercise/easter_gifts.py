gifts = input().split()  # ['Eggs', 'StuffedAnimal', 'Cozonac', 'Sweets']

while True:
    line = input()

    if line == "No Money":
        break

    # OutOfStock Eggs
    # command - OutOfStock
    # args - Eggs

    command_args = line.split()
    command = command_args[0]
    gift = command_args[1]

    # each of the commands have different arguments
    if command == "OutOfStock":
        for idx in range(len(gifts)):
            if gifts[idx] == gift:
                gifts[idx] = "None"

    elif command == "Required":
        idx = int(command_args[2])  # we should not forget the int(), we are working with a number, not a str
        if 0 <= idx < len(gifts):
            gifts[idx] = gift

    elif command == "JustInCase":
        gifts[-1] = gift

for gift in gifts:
    if gift == "None":
        continue
    print(gift, end=" ")

# Variant 2
# list_of_gifts = input().split()
# command = input()
#
# counter = 0
#
# while command != "No Money":
#     current_command = command.split()
#     current_gift = current_command[1]
#
#     if current_command[0] == "OutOfStock":
#         for index in range(len(list_of_gifts)):
#             if list_of_gifts[index] == current_gift:
#                 list_of_gifts[index] = "None"
#                 counter += 1
#
#     elif current_command[0] == "Required":
#         index_command = int(current_command[2])
#
#         if 0 <= index_command < len(list_of_gifts):
#             list_of_gifts[index_command] = current_gift
#
#     elif current_command[0] == "JustInCase":
#         list_of_gifts[-1] = current_gift
#
#     command = input()
#
# for none in range(counter):
#     if "None" in list_of_gifts:
#         list_of_gifts.remove("None")
#
# print(*list_of_gifts)