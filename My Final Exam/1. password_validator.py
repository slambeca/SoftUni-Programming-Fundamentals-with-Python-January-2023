import re


def check_idx(idx, some_array):
    if idx in range(len(some_array)):
        return True

    return False


password = input()    # invalidpassword*

COMMAND_COMPLETE = "Complete"

while True:
    command = input()

    if command == COMMAND_COMPLETE:
        break

    command_args = command.split()    # ["Add", 2, "p"]

    action = command_args[0]

    if action == "Make":
        upper_or_lower = command_args[1]    # Upper
        index = int(command_args[2])
        if upper_or_lower == "Upper":
            letter_to_upper = password[index].upper()
            password = password[:index] + letter_to_upper + password[index + 1:]
            print(password)
        elif upper_or_lower == "Lower":
            letter_to_lower = password[index].lower()
            password = password[:index] + letter_to_lower + password[index + 1:]
            print(password)
    elif action == "Insert":
        index = int(command_args[1])
        char = command_args[2]
        if check_idx(index, password):
            password = password[:index] + char + password[index:]
            print(password)
        else:
            continue
    elif action == "Replace":
        char = command_args[1]
        value = int(command_args[2])
        if char not in password:
            continue
        else:
            ascii_value = ord(char)    # 105
            current_sum = ascii_value + value    # 55
            new_symbol = chr(current_sum)    # 7
            password = password.replace(char, new_symbol)
            print(password)
    elif action == "Validation":
        if not len(password) > 7:
            print(f"Password must be at least 8 characters long!")
        if not re.match(r'^[A-Za-z0-9_]+$', password):
            print(f"Password must consist only of letters, digits and _!")

        upper_letters = []
        lower_letters = []
        digits = []

        for letter in password:
            if letter.islower():
                lower_letters.append(letter)
            elif letter.isupper():
                upper_letters.append(letter)
            elif letter.isdigit():
                digits.append(letter)

        if not upper_letters:
            print(f"Password must consist at least one uppercase letter!")
        if not lower_letters:
            print(f"Password must consist at least one lowercase letter!")
        if not digits:
            print(f"Password must consist at least one digit!")