dictionary = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if "|" in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]

        user_is_part = False

        for value in dictionary.values():
            if force_user in value:    # value is list!
                user_is_part = True
                break

        if not user_is_part:
            if force_side not in dictionary.keys():
                dictionary[force_side] = []
                dictionary[force_side].append(force_user)
            else:
                dictionary[force_side].append(force_user)

    elif "->" in command:
        command = command.split(" -> ")
        force_user = command[0]
        force_side = command[1]

        for key, value in dictionary.items():
            if force_user in value:    # value is list!
                dictionary[key].pop(value.index(force_user))
                break

        if force_side not in dictionary.keys():
            dictionary[force_side] = [force_user]
        else:
            dictionary[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

for side in dictionary.items():
    current_side = side[0]
    current_members = side[1]
    if len(current_members) > 0:
        print(f"Side: {current_side}, Members: {len(current_members)}")

    for member in range(len(current_members)):
        print(f"! {current_members[member]}")