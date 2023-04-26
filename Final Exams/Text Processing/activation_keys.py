activation_key = input()  # abcdefghijklmnopqrstuvwxyz

while True:
    command = input()

    if command == "Generate":
        break

    command_args = command.split(">>>")

    type_of_action = command_args[0]

    if type_of_action == "Contains":  # We check if the activation_key has the substring in itself
        substring = command_args[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif type_of_action == "Flip":  # change the letters in the given range to Uppercase or Lowercase
        upper_or_lower = command_args[1]
        start_index = int(command_args[2])
        end_index = int(command_args[3])

        if upper_or_lower == "Upper":    # The end index is exclusive
            range_to_upper = activation_key[start_index:end_index]
            range_to_upper = range_to_upper.upper()
            activation_key = activation_key[:start_index] + range_to_upper + activation_key[end_index:]

        elif upper_or_lower == "Lower":    # The end index is exclusive
            range_to_lower = activation_key[start_index:end_index]
            range_to_lower = range_to_lower.lower()
            activation_key = activation_key[:start_index] + range_to_lower + activation_key[end_index:]

        print(activation_key)

    elif type_of_action == "Slice":  # Deletes the characters between the start and end indices
        # (the end index is exclusive) and prints the activation key
        start_index = int(command_args[1])  # 2
        end_index = int(command_args[2])  # 6
        item_to_slice = activation_key[start_index:end_index]
        empty_string = ""
        activation_key = activation_key.replace(item_to_slice, empty_string, 1)

        print(activation_key)

print(f"Your activation key is: {activation_key}")

# # Variant 2
#
#
# def contains():
#     if substring in raw_activation_key:
#         print(f"{raw_activation_key} contains {substring}")
#     else:
#         print(f"Substring not found!")
#
#
# def flip_to_upper():
#     global raw_activation_key
#     range_to_upper = raw_activation_key[start_index:end_index]
#     range_to_upper = range_to_upper.upper()
#     raw_activation_key = raw_activation_key[:start_index] + range_to_upper + raw_activation_key[end_index:]
#     print(raw_activation_key)
#
#
# def flip_to_lower():
#     global raw_activation_key
#     range_to_lower = raw_activation_key[start_index:end_index]
#     range_to_lower = range_to_lower.lower()
#     raw_activation_key = raw_activation_key[:start_index] + range_to_lower + raw_activation_key[end_index:]
#     print(raw_activation_key)
#
#
# def slice():
#     global raw_activation_key
#     item_to_slice = raw_activation_key[start_index:end_index]
#     empty_string = ""
#     raw_activation_key = raw_activation_key.replace(item_to_slice,empty_string)
#     print(raw_activation_key)
#
#
# raw_activation_key = input()
# command = input()
#
# while command != "Generate":
#     current_command = command.split(">>>")
#     action = current_command[0]
#     if action == "Contains":
#         substring = current_command[1]
#         contains()
#     elif action == "Flip":
#         type_action = current_command[1]
#         start_index = int(current_command[2])
#         end_index = int(current_command[3])
#         if type_action == "Upper":
#             flip_to_upper()
#         elif type_action == "Lower":
#             flip_to_lower()
#
#     elif action == "Slice":
#         start_index = int(current_command[1])
#         end_index = int(current_command[2])
#         slice()
#     command = input()
#
# if command == "Generate":
#     print(f"Your activation key is: {raw_activation_key}")
#
# # Variant 3
# activation_key = input()
#
# while True:
#     command = input()
#
#     if command == 'Generate':
#         break
#
#     command = command.split('>>>')
#     action = command[0]
#
#     if action == 'Contains':
#         substring = command[1]
#         if substring in activation_key:
#             print(f'{activation_key} contains {substring}')
#         else:
#             print('Substring not found!')
#
#     elif action == 'Flip':
#         start_index = int(command[2])
#         end_index = int(command[3])
#         substring = ''
#
#         for index in range(len(activation_key)):
#             if index in range(start_index, end_index):
#                 substring += activation_key[index]
#
#         if command[1] == 'Upper':
#             activation_key = activation_key.replace(substring, substring.upper())
#         elif command[1] == 'Lower':
#             activation_key = activation_key.replace(substring, substring.lower())
#
#         print(activation_key)
#
#     elif action == 'Slice':
#         start_index = int(command[1])
#         end_index = int(command[2])
#         substring = ''
#
#         for index in range(len(activation_key)):
#             if index in range(start_index, end_index):
#                 substring += activation_key[index]
#
#         activation_key = activation_key.replace(substring, '')
#         print(activation_key)
#
# print(f'Your activation key is: {activation_key}')
#
# # Variant 4
# activation_key = input()
#
#
# def is_contains(a_key, substring):
#     if substring in a_key:
#         return f"{a_key} contains {substring}"
#     return "Substring not found!"
#
#
# def flip_part(a_key, action, index_1, index_2):
#     index_1 = int(index_1)
#     index_2 = int(index_2)
#     part_for_flip = a_key[index_1:index_2]
#     if action == "Upper":
#         a_key = a_key.replace(part_for_flip, part_for_flip.upper(), 1)
#         print(a_key)
#         return a_key
#     elif action == "Lower":
#         a_key = a_key.replace(part_for_flip, part_for_flip.lower(), 1)
#         print(a_key)
#         return a_key
#
#
# def slice_part(a_key, index_1, index_2):
#     index_1 = int(index_1)
#     index_2 = int(index_2)
#     part_for_slice = a_key[index_1:index_2]
#     a_key = a_key.replace(part_for_slice, "", 1)
#     print(a_key)
#     return a_key
#
#
# while True:
#     command = input()
#     if command == "Generate":
#         break
#
#     instruction = command.split(">>>")
#
#     if instruction[0] == "Contains":
#         print(is_contains(activation_key, instruction[1]))
#     elif instruction[0] == "Flip":
#         activation_key = flip_part(activation_key, instruction[1], instruction[2], instruction[3])
#     elif instruction[0] == "Slice":
#         activation_key = slice_part(activation_key, instruction[1], instruction[2])
#
# print(f"Your activation key is: {activation_key}")