password = input()    # Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr

while True:
    command = input()

    if command == "Done":
        break

    command_args = command.split()

    action = command_args[0]

    if action == "TakeOdd":
        new_password = ""
        for indice in range(len(password)):
            if indice % 2 != 0:
                new_password += password[indice]
        password = new_password
        print(password)

    elif action == "Cut":    # Gets the substring with the given length starting from the given index from the
        # password and removes its first occurrence, then prints the password on the console
        index = int(command_args[1])    # Those indexes will always be valid (says the exercise)
        length = int(command_args[2])
        password = password.replace(password[index:index + length], "", 1)   # We remove the first occurrence
        print(password)

    elif action == "Substitute":
        substring = command_args[1]
        substitute = command_args[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print(f"Nothing to replace!")

print(f"Your password is: {password}")

# # Variant 2
#
#
# def take_odd(password):
#     new_password = ''
#     for char_index in range(len(password)):
#         if char_index % 2 != 0:
#             new_password += password[char_index]
#     return new_password
#
#
# def cut(start_index, string_length, password):
#     password = password.replace(password[start_index:start_index + string_length], '', 1)
#     return password
#
#
# def substitute(old_string, new_string, password):
#     password = password.replace(old_string, new_string)
#     return password
#
#
# raw_password = input()
#
# while True:
#     command = input()
#
#     if command == 'Done':
#         break
#
#     command = command.split()
#     action = command[0]
#
#     if action == 'TakeOdd':
#         raw_password = take_odd(raw_password)
#         print(raw_password)
#
#     elif action == 'Cut':
#         index = int(command[1])
#         length = int(command[2])
#         raw_password = cut(index, length, raw_password)
#         print(raw_password)
#
#     elif action == 'Substitute':
#         substring = command[1]
#         substitute_string = command[2]
#         if substring in raw_password:
#             raw_password = substitute(substring, substitute_string, raw_password)
#             print(raw_password)
#         else:
#             print('Nothing to replace!')
#
#
# print(f'Your password is: {raw_password}')
#
# # Variant 3
# password = input()
#
#
# def take_odd_action(old_pass):
#     new_pass = ""
#     for i in range(len(old_pass)):
#         if i % 2 == 1:
#             new_pass += old_pass[i]
#     return new_pass
#
#
# def cut_action(old_pass, cut_index, length_index):
#     cut_chars = old_pass[cut_index:cut_index+length_index]
#     new_pass = old_pass.replace(cut_chars, "", 1)
#     return new_pass
#
#
# def substitute_action(old_pass, old_char, new_char):
#     if old_char in old_pass:
#         new_pass = old_pass.replace(old_char, new_char)
#         return new_pass
#
#
# while True:
#     command = input()
#     if command == "Done":
#         break
#
#     txt = command.split(" ")
#
#     if txt[0] == "TakeOdd":
#         password = take_odd_action(password)
#         print(password)
#     elif txt[0] == "Cut":
#         index = int(txt[1])
#         length = int(txt[2])
#         password = cut_action(password, index, length)
#         print(password)
#     elif txt[0] == "Substitute":
#         substring = txt[1]
#         substitute = txt[2]
#         if substring in password:
#             password = substitute_action(password, substring, substitute)
#             print(password)
#         else:
#             print("Nothing to replace!")
#
# print(f"Your password is: {password}")
#
# # Variant 4
# password = input()
# command_line = input()
#
# while command_line != "Done":
#     args = command_line.split()
#     command = args[0]
#     if command == "TakeOdd":
#         new_password = ""
#         for i in range(1, len(password), 2):
#             new_password += password[i]
#         password = new_password
#         print(password)
#     elif command == "Cut":
#         index = int(args[1])
#         length = int(args[2])
#         old_part = password[index: index + length]
#         password = password.replace(old_part, "", 1)
#         print(password)
#     elif command == "Substitute":
#         substring = args[1]
#         substitute = args[2]
#
#         if substring not in password:
#             print("Nothing to replace!")
#         else:
#             password = password.replace(substring, substitute)
#             print(password)
#     command_line = input()
#
# print(f'Your password is: {password}')