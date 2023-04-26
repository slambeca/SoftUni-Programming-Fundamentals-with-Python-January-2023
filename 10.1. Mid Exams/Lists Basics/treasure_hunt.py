treasure_chest = input().split("|")    # ['Gold', 'Silver', 'Bronze', 'Medallion', 'Cup']

while True:
    command = input()

    result = []

    if command == "Yohoho!":
        break

    command_args = command.split()

    type_of_command = command_args[0]

    if type_of_command == "Loot":
        command_elements = command_args[1:]    # the elements start from index 1 and end at the end of the command
        for element in command_elements:
            if element not in treasure_chest:
                treasure_chest.insert(0, element)
    elif type_of_command == "Drop":
        index = int(command_args[1])
        if index < len(treasure_chest):    # we check if the index is valid
            removed_item = treasure_chest.pop(index)
            treasure_chest.append(removed_item)
    elif type_of_command == "Steal":
        count = int(command_args[1])
        if count > len(treasure_chest):
            count = len(treasure_chest)
        for element in range(count):
            removed_item = treasure_chest.pop()
            result.append(removed_item)

        result.reverse()
        print(*result, sep=", ")


total_length = 0    # 27

for item in treasure_chest:
    length = len(item)
    total_length += length

if len(treasure_chest) > 0:
    average_treasure_gain = total_length / len(treasure_chest)

if treasure_chest:
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")