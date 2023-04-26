def is_valid_idx(idx, seq):
    return 0 <= idx < len(seq)


pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health = int(input())    # max health of ship section

is_running = True

while is_running:
    line = input()

    if line == "Retire":
        break

    command_args = line.split()
    command = command_args[0]

    if command == "Fire":
        idx = int(command_args[1])
        damage = int(command_args[2])
        if not is_valid_idx(idx, warship):
            continue
        warship[idx] -= damage
        if warship[idx] <= 0:
            is_running = False
            print(f"You won! The enemy ship has sunken.")

    elif command == "Defend":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        damage = int(command_args[3])
        if not is_valid_idx(start_idx, pirate_ship) or not is_valid_idx(end_idx, pirate_ship):
            continue
        for idx in range(start_idx, end_idx + 1):
            pirate_ship[idx] -= damage
            if pirate_ship[idx] <= 0:
                print(f"You lost! The pirate ship has sunken.")
                is_running = False
                break

    elif command == "Repair":
        idx = int(command_args[1])
        health = int(command_args[2])
        if not is_valid_idx(idx, pirate_ship):
            continue
        pirate_ship[idx] = min(max_health, pirate_ship[idx] + health)   # to check that maximum health is in limit

    elif command == "Status":
        threshold = max_health * 0.2
        counter = 0
        for section in pirate_ship:
            if section < threshold:
                counter += 1

        print(f"{counter} sections need repair.")

if is_running:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")

# Variant 2
# pirate_ship = [int(x) for x in input().split(">")]    # [12, 13, 11, 20, 66]
# warship = [int(x) for x in input().split(">")]    # [12, 22, 33, 44, 55, 32, 18]
# maximum_health = int(input())    # 70
#
# battle_finished = True
#
# while battle_finished:
#     command = input()
#
#     if command == "Retire":
#         break
#
#     command_args = command.split()
#
#     type_of_command = command_args[0]
#
#     if type_of_command == "Fire":
#         index = int(command_args[1])
#         damage_dealt = int(command_args[2])
#         if 0 <= index < len(warship):    # be sure to add the 0 <= check
#             warship[index] -= damage_dealt
#             if warship[index] <= 0:
#                 print(f"You won! The enemy ship has sunken.")
#                 battle_finished = False
#                 break
#     elif type_of_command == "Defend":
#         start_index = int(command_args[1])
#         end_index = int(command_args[2])
#         taken_damage = int(command_args[3])
#         if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):    # be sure to add the 0 <= check
#             for section in range(start_index, end_index + 1):
#                 pirate_ship[section] -= taken_damage
#                 if pirate_ship[section] <= 0:
#                     print(f"You lost! The pirate ship has sunken.")
#                     battle_finished = False
#                     break
#     elif type_of_command == "Repair":
#         index = int(command_args[1])
#         health = int(command_args[2])
#         if 0 <= index < len(pirate_ship):    # # be sure to add the 0 <= check
#             pirate_ship[index] += health
#             if pirate_ship[index] > maximum_health:
#                 pirate_ship[index] = maximum_health
#     elif type_of_command == "Status":
#         counter = 0
#         threshold = maximum_health * 0.20
#         for section in pirate_ship:
#             if section < threshold:
#                 counter += 1
#
#         print(f"{counter} sections need repair.")
#
# if battle_finished:
#     print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}")