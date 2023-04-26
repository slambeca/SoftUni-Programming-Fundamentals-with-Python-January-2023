resources = []    # ['Gold', '155', 'Silver', '10', 'Copper', '17']

resources_as_dictionary = {}

while True:
    word = input()

    if word == "stop":
        break

    resources.append(word)    # we are adding all the words to a list

for index in range(0, len(resources), 2):
    key = resources[index]
    value = int(resources[index + 1])
    if key in resources_as_dictionary.keys():
        resources_as_dictionary[key] += value
        continue

    resources_as_dictionary[key] = value

for key, value in resources_as_dictionary.items():
    print(f"{key} -> {value}")

# Variant 2
# resources = {}
#
# while True:
#     current_resource = input()
#
#     if current_resource == "stop":
#         break
#
#     current_quantity = int(input())
#
#     if current_resource not in resources.keys():
#         resources[current_resource] = 0
#     resources[current_resource] += current_quantity
#
# for resource, quantity in resources.items():
#     print(f"{resource} -> {quantity}")
#
# # Variant 3
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
#     if command == "stop":
#         break
#
#     quantity = int(input())
#
#     if check_for_item(command, dictionary):
#         dictionary[command] = quantity
#     else:
#         dictionary[command] += quantity
#
# for key, value in dictionary.items():
#     print(f"{key} -> {value}")
#
# # Variant 4 with dictionary comprehension
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
#     if command == "stop":
#         break
#
#     quantity = int(input())
#
#     if check_for_item(command, dictionary):
#         dictionary[command] = quantity
#     else:
#         dictionary[command] += quantity
#
# results = [f"{resource} -> {quantity}" for resource, quantity in dictionary.items()]
#
# print("\n".join(results))