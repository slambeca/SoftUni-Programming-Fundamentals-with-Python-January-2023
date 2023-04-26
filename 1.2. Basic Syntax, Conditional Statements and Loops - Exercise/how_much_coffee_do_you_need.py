user_input = input()

commands_for_coffee_brake = ("dog", "cat", "movie", "coding", "DOG", "CAT", "MOVIE", "CODING")

coffees_needed = 0

extra_sleep = False

while user_input != "END":
    command = user_input

    if coffees_needed >= 5:
        extra_sleep = True
        break

    if command.islower() and command in commands_for_coffee_brake:
        coffees_needed += 1
    elif command.isupper() and command in commands_for_coffee_brake:
        coffees_needed += 2

    user_input = input()

if extra_sleep:
    print("You need extra sleep")
else:
    print(coffees_needed)

# Variant 2
# coffee_counter = 0
#
# while True:
#     line = input()
#
#     if line == "END":
#         break
#
#     if line == "coding" or line == "cat" or line == "dog" or line == "movie":
#         coffee_counter += 1
#     elif line == "CODING" or line == "CAT" or line == "DOG" or line == "MOVIE":
#         coffee_counter += 2
#
# if coffee_counter > 5:
#     print("You need extra sleep")
# else:
#     print(coffee_counter)
#
# # Variant 3
# command = input()
#
# coffees_needed = 0
#
# commands_lower = ["dog", "cat", "coding", "movie"]
# commands_upper = ["DOG", "CAT", "CODING", "MOVIE"]
#
# while command != "END":
#     if command in commands_lower or command in commands_upper:
#         if command.islower():
#             coffees_needed += 1
#         elif command.isupper():
#             coffees_needed += 2
#
#     if command == "END":
#         break
#
#     command = input()
#
# if coffees_needed > 5:
#     print("You need extra sleep")
# else:
#     print(coffees_needed)