number_of_pieces = int(input())

dictionary = {}
# {'Fur Elise': ['Beethoven', 'A Minor'], 'Moonlight Sonata': ['Beethoven', 'C# Minor'],
# 'Clair de Lune': ['Debussy', 'C# Minor']}

for _ in range(number_of_pieces):
    command = input().split("|")  # ['Fur Elise', 'Beethoven', 'A Minor']

    piece = command[0]  # Fur Elise
    composer = command[1]  # Beethoven
    key = command[2]  # A Minor

    dictionary[piece] = []    # or dictionary[piece] = [composer, key]
    dictionary[piece].append(composer)
    dictionary[piece].append(key)

while True:
    command = input()

    if command == "Stop":
        break

    command = command.split("|")

    action = command[0]  # Add
    piece = command[1]  # Sonata No.2

    if action == "Add":
        composer = command[2]
        key = command[3]
        if piece not in dictionary.keys():    # Add the new piece if it does not exist in our collection
            dictionary[piece] = []    # or dictionary[piece] = [composer, key]
            dictionary[piece].append(composer)
            dictionary[piece].append(key)
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":    # Remove the piece if it exists in our collection
        if piece in dictionary.keys():
            print(f"Successfully removed {piece}!")
            del dictionary[piece]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        new_key = command[2]
        if piece in dictionary.keys():    # Change the key if the piece exists in our collection
            dictionary[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in dictionary.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")

# # Variant 2
# # Our core function that navigates our entire program. Each time in it we will accept one element as a parameter
# # (number of pieces)
#
#
# def store_data_func(number):
#     data = {}
#     for _ in range(number):
#         current_data = input().split("|")
#         piece = current_data[0]
#         composer = current_data[1]
#         key = current_data[2]
#
#         data[piece] = [composer, key]
#
#     return data
#
#
# def add_command_function(piece, composer, key, data):
#     if piece not in data:
#         data[piece] = [composer, key]
#         print(f"{piece} by {composer} in {key} added to the collection!")
#     else:
#         print(f"{piece} is already in the collection!")
#
#
# def remove_function(piece, data):
#     if piece in data:
#         print(f"Successfully removed {piece}!")
#         del data[piece]
#     else:
#         print(f"Invalid operation! {piece} does not exist in the collection.")
#
#
# def change_key_function(piece, new_key, data):
#     if piece in data:
#         data[piece][1] = new_key
#         print(f"Changed the key of {piece} to {new_key}!")
#     else:
#         print(f"Invalid operation! {piece} does not exist in the collection.")
#
#
# def print_function(data):
#     result = ""
#     for piece in data:
#         composer = data[piece][0]
#         key = data[piece][1]
#         result += f"{piece} -> Composer: {composer}, Key: {key}\n"
#     return result
#
#
# def the_pianist_function(number):
#     data = store_data_func(number)
#
#     while True:
#         command = input().split("|")
#
#         if command[0] == "Stop":
#             print(print_function(data))
#             break
#
#         current_command = command[0]
#         piece = command[1]
#
#         if current_command == "Add":
#             composer = command[2]
#             key = command[3]
#             add_command_function(piece, composer, key, data)
#
#         elif current_command == "Remove":
#             remove_function(piece, data)
#
#         elif current_command == "ChangeKey":
#             new_key = command[2]
#             change_key_function(piece, new_key, data)
#
#
# count_pieces = int(input())
# the_pianist_function(count_pieces)
#
# # Variant 3
#
#
# def add(collection, piece, composer, key):
#     if piece in collection:
#         print(f'{piece} is already in the collection!')
#     else:
#         collection[piece] = [composer, key]
#         print(f'{piece} by {composer} in {key} added to the collection!')
#     return collection
#
#
# def remove(collection, piece):
#     if piece in collection:
#         print(f'Successfully removed {piece}!')
#         collection.pop(piece)
#     else:
#         print(f'Invalid operation! {piece} does not exist in the collection.')
#     return collection
#
#
# def change_key(collection, piece, new_key):
#     if piece in collection:
#         collection[piece][1] = new_key
#         print(f'Changed the key of {piece} to {new_key}!')
#     else:
#         print(f'Invalid operation! {piece} does not exist in the collection.')
#     return collection
#
#
# number_of_pieces = int(input())
# collection = {}
#
# for piece in range(number_of_pieces):
#     title, composer, key = input().split('|')
#     collection[title] = [composer, key]
#
# while True:
#     command = input()
#
#     if command == 'Stop':
#         break
#
#     command = command.split('|')
#
#     if command[0] == 'Add':
#         piece, composer, key = command[1], command[2], command[3]
#         add(collection, piece, composer, key)
#
#     elif command[0] == 'Remove':
#         piece = command[1]
#         remove(collection, piece)
#
#     elif command[0] == 'ChangeKey':
#         piece, new_key = command[1], command[2]
#         change_key(collection, piece, new_key)
#
# sorted_collection = sorted(collection.items(), key=lambda pieces: (pieces[0], pieces[1][0]))
#
# for piece in sorted_collection:
#     print(f'{piece[0]} -> Composer: {piece[1][0]}, Key: {piece[1][1]}')
#
# # Variant 4
# num_of_pieces = int(input())
# pieces_data = {}
#
# for pieces in range(num_of_pieces):
#     [piece, composer, key] = input().split("|")
#     pieces_data[piece] = {"composer": composer, "key": key}
#
#
# def add(data, piece, composer, key):
#     if piece not in data:
#         data[piece] = {"composer": composer, "key": key}
#         print(f"{piece} by {composer} in {key} added to the collection!")
#         return data
#     else:
#         print(f"{piece} is already in the collection!")
#         return data
#
#
# def remove(data, piece):
#     if piece not in data:
#         print(f"Invalid operation! {piece} does not exist in the collection.")
#         return data
#     else:
#         del data[piece]
#         print(f"Successfully removed {piece}!")
#         return data
#
#
# def change(data, piece, key):
#     if piece not in data:
#         print(f"Invalid operation! {piece} does not exist in the collection.")
#         return data
#     else:
#         data[piece]["key"] = key
#         print(f"Changed the key of {piece} to {key}!")
#         return data
#
#
# while True:
#     command = input()
#     if command == "Stop":
#         break
#
#     actions = command.split("|")
#     action = actions[0]
#     if action == "Add":
#         curr_piece = actions[1]
#         curr_composer = actions[2]
#         curr_key = actions[3]
#         pieces_data = add(pieces_data, curr_piece, curr_composer, curr_key)
#     elif action == "Remove":
#         curr_piece = actions[1]
#         pieces_data = remove(pieces_data, curr_piece)
#     elif action == "ChangeKey":
#         curr_piece = actions[1]
#         new_key = actions[2]
#         pieces_data = change(pieces_data, curr_piece, new_key)
#
# filtered_pieces = sorted(pieces_data.items(), key=lambda x: (x[0], x[1]["composer"]))
#
# for piece, data in filtered_pieces:
#     print(f"{piece} -> Composer: {data['composer']}, Key: {data['key']}")