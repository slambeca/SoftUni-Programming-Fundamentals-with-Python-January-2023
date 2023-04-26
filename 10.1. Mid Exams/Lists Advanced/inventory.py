journal = input().split(", ")    # ['Iron', 'Wood', 'Sword']

while True:
    command = input()

    if command == "Craft!":
        break

    command_args = command.split(" - ")    # ['Collect', 'Gold']

    type_of_action = command_args[0]
    item = command_args[1]

    if type_of_action == "Collect":
        if item not in journal:
            journal.append(item)
    elif type_of_action == "Drop":
        if item in journal:
            journal.remove(item)
    elif type_of_action == "Combine Items":    # Combine Items - Sword:Bow
        item_args = item.split(":")    # ["Sword", "Bow"]
        first_item = item_args[0]    # "Sword"
        second_item = item_args[1]    # "Bow"
        if first_item in journal:
            first_item_index = journal.index(first_item)    # 1
            journal.insert(first_item_index + 1, second_item)    # add the second item at the next index
    elif type_of_action == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)

print(*journal, sep=", ")