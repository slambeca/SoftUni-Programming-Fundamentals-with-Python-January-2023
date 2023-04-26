dictionary = {}

count_cars = int(input())

for car in range(count_cars):
    command = input().split()

    action = command[0]
    name = command[1]

    if action == "register":
        reg_number = command[2]
        if name not in dictionary:
            print(f"{name} registered {reg_number} successfully")

            dictionary[name] = reg_number

        else:
            print(f"ERROR: already registered with plate number {reg_number}")

    else:
        if name in dictionary:
            print(f"{name} unregistered successfully")
            dictionary.pop(name)
        else:
            print(f"ERROR: user {name} not found")

for key, value in dictionary.items():
    print(f"{key} => {value}")

# Variant 2
# parking = {}
#
# numbers_of_cars = int(input())
#
# for car in range(numbers_of_cars):
#     current_driver = input().split()
#
#     action = current_driver[0]
#     username = current_driver[1]
#
#     if action == "register":
#         license_plate_number = current_driver[2]
#         if username in parking.keys():
#             print(f"ERROR: already registered with plate number {license_plate_number}")
#         else:
#             parking[username] = license_plate_number
#             print(f"{username} registered {license_plate_number} successfully")
#     else:
#         if username not in parking:
#             print(f"ERROR: user {username} not found")
#         else:
#             print(f"{username} unregistered successfully")
#             # parking.pop(username)
#             del parking[username]
#
# for username, license_plate_number in parking.items():
#     print(f"{username} => {license_plate_number}")
#
# # Variant 3 with a function
#
#
# def check_for_item(some_item, some_array):
#     if some_item not in some_array:
#         return True
#     return False
#
#
# dictionary = {}
#
# count_cars = int(input())
#
# for _ in range(count_cars):
#     command = input().split()
#
#     action = command[0]
#     name = command[1]
#
#     if action == "register":
#         registration = command[2]
#
#         if check_for_item(name, dictionary.keys()):
#             dictionary[name] = registration
#             print(f"{name} registered {registration} successfully")
#         else:
#             print(f"ERROR: already registered with plate number {registration}")
#
#     elif action == "unregister":
#         if check_for_item(name, dictionary.keys()):
#             print(f"ERROR: user {name} not found")
#         else:
#             del dictionary[name]
#             print(f"{name} unregistered successfully")
#
# for key, value in dictionary.items():
#     print(f"{key} => {value}")