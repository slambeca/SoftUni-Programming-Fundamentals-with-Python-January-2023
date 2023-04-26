concealed_message = input()    # heVVodar!gniV

while True:
    command = input()

    if command == "Reveal":
        break

    command_args = command.split(":|:")

    type_of_command = command_args[0]

    if type_of_command == "InsertSpace":    # Insert space at the given index
        index = int(command_args[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]

    elif type_of_command == "Reverse":    # If the message contains the given substring, cut it out,
        # reverse it and add it at the end of the message
        substring = command_args[1]
        if substring in concealed_message:    # We validate that it exists in our string
            concealed_message = concealed_message.replace(substring, "", 1)    # only the first occurrence of the subst
            concealed_message = concealed_message + substring[::-1]
        else:
            print("error")
            continue

    elif type_of_command == "ChangeAll":    # Replace the substring with the replacement value
        substring = command_args[1]
        replacement = command_args[2]
        concealed_message = concealed_message.replace(substring, replacement)

    print(concealed_message)

print(f"You have a new text message: {concealed_message}")

# # Variant 2
#
#
# def insert_space(message, index):
#     message = message[0:index] + ' ' + message[index:]
#     print(message)
#     return message
#
#
# def reverse(message, substring):
#     if substring in message:
#         message = message.replace(substring, '', 1)
#         message = message + substring[::-1]
#         print(message)
#     else:
#         print('error')
#     return message
#
#
# def change_all(message, substring, replacement):
#     if substring in message:
#         message = message.replace(substring, replacement)
#         print(message)
#     return message
#
#
# message = input()
#
# while True:
#     command = input()
#
#     if command == 'Reveal':
#         break
#
#     command = command.split(':|:')
#
#     if command[0] == 'InsertSpace':
#         index = int(command[1])
#         message = insert_space(message, index)
#
#     elif command[0] == 'Reverse':
#         substring = command[1]
#         message = reverse(message, substring)
#
#     elif command[0] == 'ChangeAll':
#         substring = command[1]
#         replacement = command[2]
#         message = change_all(message, substring, replacement)
#
#
# print(f'You have a new text message: {message}')
#
# # Variant 3
# concealed_message = input()
#
#
# def insert_space(message, index):
#     first_part = message[:index]
#     second_part = message[index:]
#     new_message = first_part+" "+second_part
#     print(new_message)
#     return new_message
#
#
# def reverse(message, substring):
#     if substring in message:
#         cut_message = message.replace(substring, "", 1)
#         rev_substring = substring[::-1]
#         new_message = cut_message+rev_substring
#         print(new_message)
#         return new_message
#     else:
#         print("error")
#         return message
#
#
# def change_all(message, substring, replacement):
#     if substring in message:
#         new_message = message.replace(substring, replacement)
#         print(new_message)
#         return new_message
#
#
# while True:
#     command = input()
#     if command == "Reveal":
#         break
#
#     operations = command.split(":|:")
#
#     if operations[0] == "InsertSpace":
#         index = int(operations[1])
#         concealed_message = insert_space(concealed_message, index)
#     elif operations[0] == "Reverse":
#         rev_substring = operations[1]
#         concealed_message = reverse(concealed_message, rev_substring)
#     elif operations[0] == "ChangeAll":
#         change_substring = operations[1]
#         replacement = operations[2]
#         concealed_message = change_all(concealed_message, change_substring, replacement)
#
# print(f"You have a new text message: {concealed_message}")
#
# # Variant 4
# data = input()
#
# while True:
#     command = input().split(":|:")
#
#     current_command = command[0]
#
#     if current_command == "Reveal":
#         print(f"You have a new text message: {data}")
#         break
#
#     elif current_command == "InsertSpace":
#         index = int(command[1])
#         data = data[:index] + " " + data[index:]
#         print(data)
#
#     elif current_command == "Reverse":
#         substring = command[1]
#         if substring in data:
#             data = data.replace(substring, "", 1)
#             data += substring[::-1]
#             print(data)
#         else:
#             print("error")
#
#     elif current_command == "ChangeAll":
#         substring, replacement = command[1], command[2]
#         data = data.replace(substring, replacement)
#         print(data)