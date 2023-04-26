rooms = int(input())

free_chairs = 0
count_room = 0

not_enough_chairs = False

for _ in range(rooms):
    current_room = input()

    count_room += 1

    current_room_args = current_room.split()

    number_of_chairs = len(current_room_args[0])
    number_of_people = int(current_room_args[1])

    if number_of_chairs < number_of_people:
        print(f"{number_of_people - number_of_chairs} more chairs needed in room {count_room}")    # or we can use the _
        not_enough_chairs = True

    free_chairs += number_of_chairs - number_of_people

if not not_enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")

# Variant 2 with a function
#
#
# def check_the_rooms(numbers_of_rooms):
#     total_free_chairs = 0
#     total_needed_chairs = 0
#
#     for room in range(1, numbers_of_rooms + 1):
#         free_chairs, visitors = input().split()
#         difference = len(free_chairs) - int(visitors)
#         if difference >= 0:
#             total_free_chairs += difference
#         else:
#             total_needed_chairs += abs(difference)
#             print(f"{abs(difference)} more chairs needed in room {room}")
#
#     return total_free_chairs, total_needed_chairs
#
#
# number_of_rooms = int(input())
#
# free_chairs, needed_chairs = check_the_rooms(number_of_rooms)
#
# if free_chairs >= needed_chairs:
#     print(f"Game On, {free_chairs} free chairs left")
#
# # Variant 3
# rooms = int(input())
#
# free_chairs = 0
#
# game_on = True
#
# for room in range(1, rooms + 1):
#     chairs, guests_as_string = input().split()
#     guests = int(guests_as_string)
#
#     if guests > len(chairs):
#         needed_chairs = guests - len(chairs)
#         print(f"{needed_chairs} more chairs needed in room {room}")
#         game_on = False
#     else:
#         free_chairs_by_row = len(chairs) - guests
#         free_chairs += free_chairs_by_row
#
# if game_on:
#     print(f"Game On, {free_chairs} free chairs left")