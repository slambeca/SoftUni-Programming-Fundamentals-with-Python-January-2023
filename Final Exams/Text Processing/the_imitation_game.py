encrypted_message = input()    # zzHe

while True:
    command = input()

    if command == "Decode":
        break

    command_args = command.split("|")

    type_of_action = command_args[0]    # ChangeAll

    if type_of_action == "Move":    # Move the first n letters to the back of the string (slicing and concatenation)
        number_of_letters = int(command_args[1])    # 3
        first_letters = encrypted_message[0:number_of_letters]    # llo
        encrypted_message = encrypted_message[number_of_letters:] + first_letters

    elif type_of_action == "Insert":    # Place the value before the given index (slicing and string concatenation)
        index = int(command_args[1])    # 2 - this is the same as place the value at the given index
        value = command_args[2]    # o
        encrypted_message = encrypted_message[0:index] + value + encrypted_message[index:]

    elif type_of_action == "ChangeAll":    # Replace the given value in the string with the new value
        substring = command_args[1]    # "z"
        replacement = command_args[2]    # "l"
        encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")

# # Variant 2
#
# encrypted_msg = input()
#
#
# def move(msg, num_ch):
#     moved_msg, left_msg = msg[:num_ch], msg[num_ch:]
#     result = left_msg+moved_msg
#     return result
#
#
# def insert(msg, i, val):
#     msg_before, msg_after = msg[:i], msg[i:]
#     result = msg_before+val+msg_after
#     return result
#
#
# def change_all(msg, sub_s, text):
#     result = msg.replace(sub_s, text)
#     return result
#
#
# while True:
#     instruction = input()
#     if instruction == "Decode":
#         break
#
#     operations = instruction.split("|")
#     curr_operation = operations[0]
#
#     if curr_operation == "Move":
#         num_chars = int(operations[1])
#         encrypted_msg = move(encrypted_msg, num_chars)
#     elif curr_operation == "Insert":
#         index = int(operations[1])
#         value = operations[2]
#         encrypted_msg = insert(encrypted_msg, index, value)
#     elif curr_operation == "ChangeAll":
#         substring = operations[1]
#         replacement_text = operations[2]
#         encrypted_msg = change_all(encrypted_msg, substring, replacement_text)
#
# print(f"The decrypted message is: {encrypted_msg}")
#
# # Variant 3
# message = input()
#
# while True:
#     command = input()
#
#     if command == 'Decode':
#         break
#
#     command = command.split('|')
#
#     if command[0] == 'Move':
#         number_of_letters = int(command[1])
#         characters_to_move = message[0:number_of_letters]
#         message = message.replace(characters_to_move, '') + characters_to_move
#
#     elif command[0] == 'Insert':
#         index = int(command[1])
#         value = command[2]
#         message = message[0:index] + value + message[index:]
#
#     elif command[0] == 'ChangeAll':
#         substring = command[1]
#         replacement = command[2]
#         message = message.replace(substring, replacement)
#
# print(f'The decrypted message is: {message}')