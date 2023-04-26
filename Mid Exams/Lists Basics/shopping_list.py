initial_list = input().split("!")    # ['Tomatoes', 'Potatoes', 'Bread']

while True:
    command = input()

    if command == "Go Shopping!":
        break

    command_args = command.split()

    type_of_command = command_args[0]
    item = command_args[1]

    if type_of_command == "Urgent":    # ['Milk', 'Tomatoes', 'Potatoes', 'Bread']
        if item not in initial_list:
            initial_list.insert(0, item)    # add the item at the beginning of the list
    elif type_of_command == "Unnecessary":
        if item in initial_list:
            initial_list.remove(item)    # ['Tomatoes', 'Potatoes', 'Bread'] - remove the item from the list
    elif type_of_command == "Correct":
        second_item = command_args[2]
        for list_item in range(len(initial_list)):
            if initial_list[list_item] == item:
                initial_list[list_item] = second_item    # replace the item with another item
    elif type_of_command == "Rearrange":
        if item in initial_list:    # move the item from its index to the last index
            initial_list.remove(item)
            initial_list.append(item)

print(", ".join(initial_list))    # print the list as a string

# Variant 2
# products = input().split("!")
#
# while True:
#     line = input()
#     if line == "Go Shopping!":
#         break
#
#     command_args = line.split()
#     command = command_args[0]
#     product = command_args[1]
#
#     if command == "Urgent":
#         if product not in products:
#             products.insert(0, product)
#     elif command == "Unnecessary":
#         if product in products:
#             products.remove(product)
#     elif command == "Correct":
#         new_product = command_args[2]
#         if product in products:
#             idx = products.index(product)
#             products[idx] = new_product
#     elif command == "Rearrange":
#         if product in products:
#             idx = products.index(product)
#             products.pop(idx)
#             products.append(product)
#
# print(", ".join(products))
#
# # Variant 3
# def urgent(item, items):
#     if item not in items:
#         items.insert(0, item)
#
#
# def unnecessary(item, items):
#     if item in items:
#         items.remove(item)
#
#
# def correct(old_item, new_item, items):
#     if old_item in items:
#         index = items.index(old_item)
#         items[index] = new_item
#
#
# def rearrange(item, items):
#     if item in items:
#         items.remove(item)
#         items.append(item)
#
#
# shopping_list = input().split('!')
#
# while True:
#     command = input()
#
#     if command == 'Go Shopping!':
#         break
#
#     command = command.split()
#     action = command[0]
#
#     if action == 'Urgent':
#         grocery = command[1]
#         urgent(grocery, shopping_list)
#
#     elif action == 'Unnecessary':
#         grocery = command[1]
#         unnecessary(grocery, shopping_list)
#
#     elif action == 'Correct':
#         old_grocery = command[1]
#         new_grocery = command[2]
#         correct(old_grocery, new_grocery, shopping_list)
#
#     elif action == 'Rearrange':
#         grocery = command[1]
#         rearrange(grocery, shopping_list)
#
# print(', '.join(shopping_list))