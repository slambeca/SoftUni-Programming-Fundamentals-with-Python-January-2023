user_input = input()

flag = False

while user_input != "Welcome!":
    name = user_input

    if name == "Voldemort":
        print(f"You must not speak of that name!")
        flag = True
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")

    user_input = input()

if not flag:
    print("Welcome to Hogwarts.")

# Variant 2 with while True
# voldemort = False
#
# while True:
#     name = input()
#
#     if name == "Welcome!":
#         break
#
#     if name == "Voldemort":
#         print(f"You must not speak of that name!")
#         voldemort = True
#         break
#
#     if len(name) < 5:
#         print(f"{name} goes to Gryffindor.")
#     elif len(name) == 5:
#         print(f"{name} goes to Slytherin.")
#     elif len(name) == 6:
#         print(f"{name} goes to Ravenclaw.")
#     else:
#         print(f"{name} goes to Hufflepuff.")
#
# if not voldemort:
#     print(f"Welcome to Hogwarts.")