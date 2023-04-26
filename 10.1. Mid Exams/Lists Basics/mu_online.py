dungeons_rooms = input().split("|")    # ['rat 10', 'bat 20', 'potion 10', 'rat 10', 'chest 100', 'boss 70',
# 'chest 1000']

initial_health = 100
initial_bitcoins = 0

game_won = True

count_rooms = 0

for room in dungeons_rooms:
    room_args = room.split()

    type_of_room = room_args[0]    # rat
    value_of_room = int(room_args[1])    # 10

    count_rooms += 1

    if type_of_room == "potion":
        current_health = initial_health
        initial_health += value_of_room
        if initial_health > 100:
            initial_health = 100
        gained_health = initial_health - current_health
        print(f"You healed for {gained_health} hp.")
        print(f"Current health: {initial_health} hp.")
    elif type_of_room == "chest":
        initial_bitcoins += value_of_room
        print(f"You found {value_of_room} bitcoins.")
    else:
        if initial_health > value_of_room:
            print(f"You slayed {type_of_room}.")
            initial_health -= value_of_room
        else:
            print(f"You died! Killed by {type_of_room}.")
            print(f"Best room: {count_rooms}")
            game_won = False
            break

if game_won:
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")

# Variant 2
# rooms = input().split("|")
#
# MAX_HEALTH = 100
# health = MAX_HEALTH
# bitcoins = 0
#
# room_number = 0
#
# for room in rooms:
#     room_number += 1
#     command, amount = room.split()
#     # Try with floats if errors
#     amount = int(amount)
#
#     if command == "potion":
#         if health + amount > MAX_HEALTH:
#             print(f"You healed for {MAX_HEALTH - health} hp.")
#             health = MAX_HEALTH
#         else:
#             print(f"You healed for {amount} hp.")
#             health += amount
#         print(f"Current health: {health} hp.")
#
#     elif command == "chest":
#         bitcoins += amount
#         print(f"You found {amount} bitcoins.")
#
#     else:
#         health -= amount
#         if health > 0:
#             print(f"You slayed {command}.")
#         else:
#             print(f"You died! Killed by {command}.")
#             print(f"Best room: {room_number}")
#             exit(0)
#
# print(f"You've made it!")
# print(f"Bitcoins: {bitcoins}")
# print(f"Health: {health}")