max_message_capacity = int(input())

dictionary = {}

while True:
    command = input()

    if command == "Statistics":
        break

    command_args = command.split("=")

    action = command_args[0]

    if action == "Add":
        username = command_args[1]
        if username in dictionary.keys():
            continue
        else:
            sent_messages = int(command_args[2])
            received_messages = int(command_args[3])
            dictionary[username] = [sent_messages, received_messages]

    elif action == "Message":
        sender = command_args[1]
        receiver = command_args[2]
        if sender in dictionary.keys() and receiver in dictionary.keys():

            dictionary[sender][0] += 1
            if dictionary[sender][0] + dictionary[sender][1] == max_message_capacity:
                print(f"{sender} reached the capacity!")
                del dictionary[sender]

            dictionary[receiver][1] += 1
            if dictionary[receiver][0] + dictionary[receiver][1] == max_message_capacity:
                print(f"{receiver} reached the capacity!")
                del dictionary[receiver]

    elif action == "Empty":
        username = command_args[1]
        if username == "All":
            dictionary.clear()
        else:
            if username in dictionary.keys():
                del dictionary[username]

print(f"Users count: {len(dictionary)}")

for username, messages in dictionary.items():
    print(f'{username} - {sum(messages)}')