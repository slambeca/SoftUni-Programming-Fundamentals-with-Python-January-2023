command = input()

dictionary = {}

while len(command) != 1:
    key, value = command.split("-")

    if key not in dictionary.keys():
        dictionary[key] = value
    else:
        dictionary[key] = value

    command = input()

for name in range(int(command)):
    current_name = input()

    if current_name not in dictionary.keys():
        print(f"Contact {current_name} does not exist.")
    else:
        print(f"{current_name} -> {dictionary[current_name]}")

# Variant 2
# phonebook = {}
#
# while True:
#     entry = input()
#
#     if "-" not in entry:
#         break
#
#     name, phone = entry.split("-")
#
#     phonebook[name] = phone
#
# for check in range(int(entry)):
#     searched_name = input()
#
#     if searched_name in phonebook.keys():
#         found_number = phonebook[searched_name]
#         print(f"{searched_name} -> {found_number}")
#     else:
#         print(f"Contact {searched_name} does not exist.")
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
# while True:
#     command = input()
#
#     if "-" not in command:
#         break
#
#     name, number = command.split("-")
#
#     if check_for_item(name, dictionary):
#         dictionary[name] = number
#     else:
#         dictionary[name] = number
#
# for _ in range(int(command)):
#     name = input()
#
#     if check_for_item(name, dictionary):
#         print(f"Contact {name} does not exist.")
#     else:
#         print(f"{name} -> {dictionary[name]}")