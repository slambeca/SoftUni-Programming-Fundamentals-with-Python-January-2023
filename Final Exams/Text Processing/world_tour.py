initial_stops = input()    # Hawai::Cyprys-Greece

while True:
    command = input()

    if command == "Travel":
        break

    command_args = command.split(":")

    type_of_command = command_args[0]

    if type_of_command == "Add Stop":    # Add stop at the given index (same as place it before the given index)
        index = int(command_args[1])    # 7
        string = command_args[2]    # Rome
        if index in range(len(initial_stops)):    # We validate the index
            initial_stops = initial_stops[0:index] + string + initial_stops[index:]

    elif type_of_command == "Remove Stop":    # Remove the letters between the indexes - inclusive
        start_index = int(command_args[1])    # 11
        end_index = int(command_args[2])    # 16
        if start_index in range(len(initial_stops)) and end_index in range(len(initial_stops)):    # Indexes validation
            initial_stops = initial_stops[0:start_index] + initial_stops[end_index + 1:]
            # initial_stops = initial_stops.replace(destinations[start_index:end_index+1], "", 1)

    elif type_of_command == "Switch":    # Switch values if the old value exists in the string
        old_string = command_args[1]    # "Hawai"
        new_string = command_args[2]    # "Bulgaria"
        if old_string in initial_stops:
            initial_stops = initial_stops.replace(old_string, new_string)

    print(initial_stops)

print(f"Ready for world tour! Planned stops: {initial_stops}")


# # Variant 2
#
#
# def world_tour(destinations):
#     while True:
#         command = input().split(":")
#
#         current_command = command[0]
#
#         if current_command == "Travel":
#             print(f"Ready for world tour! Planned stops: {destinations}")
#             break
#
#         elif current_command == "Add Stop":    # Insert a string at the given index
#             index, string = int(command[1]), command[2]
#
#             if 0 <= index < len(destinations):    # Check if the index is valid
#                 destinations = destinations[:index] + string + destinations[index:]
#
#         elif current_command == "Remove Stop":
#             start_index, end_index = int(command[1]), int(command[2])
#             if 0 <= start_index <= end_index < len(destinations):
#                 destinations = destinations[:start_index] + destinations[end_index + 1:]
#
#         elif current_command == "Switch":
#             old_string, new_string = command[1], command[2]
#             destinations = destinations.replace(old_string, new_string)
#
#         print(destinations)
#
#
# data = input()
# world_tour(data)
#
# # Variant 3
# travel_stops = input()
#
# while True:
#     command = input()
#
#     if command == 'Travel':
#         break
#
#     command = command.split(':')
#
#     if command[0] == 'Add Stop':
#         index = int(command[1])
#         string = command[2]
#
#         if index in range(len(travel_stops)):
#             travel_stops = travel_stops[0:index] + string + travel_stops[index:]
#
#     elif command[0] == 'Remove Stop':
#         start_index = int(command[1])
#         end_index = int(command[2])
#
#         if start_index in range(len(travel_stops)) and end_index in range(len(travel_stops)):
#             travel_stops = travel_stops[0:start_index] + travel_stops[end_index + 1:]
#
#     elif command[0] == 'Switch':
#         old_string = command[1]
#         new_string = command[2]
#
#         if old_string in travel_stops:
#             travel_stops = travel_stops.replace(old_string, new_string)
#
#     print(travel_stops)
#
# print(f'Ready for world tour! Planned stops: {travel_stops}')
#
# # Variant 4
# destinations = input()
# initial_destinations = destinations
#
# while True:
#     command = input()
#     if command == "Travel":
#         break
#
#     action = command.split(":")
#
#     if action[0] == "Add Stop":
#         index = int(action[1])
#         changed_string = action[2]
#         if 0 <= index < len(destinations):
#             destinations = destinations[:index]+changed_string+destinations[index:]
#         print(destinations)
#     elif action[0] == "Remove Stop":
#         index_1 = int(action[1])
#         index_2 = int(action[2])
#         if 0 <= index_1 < len(destinations) and 0 <= index_2 < len(destinations):
#             destinations = destinations.replace(destinations[index_1: index_2+1], "", 1)
#         print(destinations)
#     elif action[0] == "Switch":
#         old_string = action[1]
#         new_string = action[2]
#         if old_string in initial_destinations:
#             destinations = destinations.replace(old_string, new_string)
#         print(destinations)
#
# print(f"Ready for world tour! Planned stops: {destinations}")
#
# # Variant 5
#
#
# def is_valid(index, seq):
#     return 0 <= index < len(seq)
#
#
# COMMAND_TRAVEL = "Travel"
# COMMAND_ADD_STOP = "Add Stop"
# COMMAND_REMOVE_STOP = "Remove Stop"
# COMMAND_SWITCH = "Switch"
#
# text = input()
#
# while True:
#     line = input()
#
#     if line == COMMAND_TRAVEL:
#         break
#
#     command_args = line.split(":")
#
#     command = command_args[0]
#
#     if command == COMMAND_ADD_STOP:
#         idx = int(command_args[1])
#         new_stop = command_args[2]
#         if is_valid(idx, text):
#             text = text[:idx] + new_stop + text[idx:]
#
#     elif command == COMMAND_REMOVE_STOP:
#         start_idx = int(command_args[1])
#         end_idx = int(command_args[2])
#         if is_valid(start_idx, text) and is_valid(end_idx, text):
#             text = text[:start_idx] + text[end_idx + 1:]
#
#     elif command == COMMAND_SWITCH:
#         old_string = command_args[1]
#         new_string = command_args[2]
#         text = text.replace(old_string, new_string)
#
#     print(text)
#
# print(f"Ready for world tour! Planned stops: {text}")