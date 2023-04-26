def check_for_phone(item, sequence):
    if item in sequence:
        return True
    return False


list_of_phones = input().split(", ")

while True:
    input_line = input()

    if input_line == "End":
        break

    command_args = input_line.split(" - ")

    type_of_command = command_args[0]

    if type_of_command == "Add":
        phone = command_args[1]
        if not check_for_phone(phone, list_of_phones):
            list_of_phones.append(phone)

    elif type_of_command == "Remove":
        phone = command_args[1]
        if check_for_phone(phone, list_of_phones):
            list_of_phones.remove(phone)

    elif "Bonus" in type_of_command:
        phones = command_args[1].split(":")
        old_phone = phones[0]
        new_phone = phones[1]
        if check_for_phone(old_phone, list_of_phones):
            first_index = list_of_phones.index(old_phone)
            list_of_phones.insert(first_index + 1, new_phone)

    elif type_of_command == "Last":
        phone = command_args[1]
        if check_for_phone(phone, list_of_phones):
            list_of_phones.remove(phone)
            list_of_phones.append(phone)

print(*list_of_phones, sep=", ")