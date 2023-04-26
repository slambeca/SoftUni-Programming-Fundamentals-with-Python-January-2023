def representation_data(data, last_position):
    result = [x for x in data if x == 0]
    print(f"Cupid's last position was {last_position}.")
    if len(result) != len(data):
        diff = abs(len(data) - len(result))
        print(f"Cupid has failed {diff} places.")
    else:
        print(f"Mission was successful.")


def heart_delivery(data):
    current_index_position = 0
    cupids_last_position = 0

    while True:
        command = input().split()

        if command[0] == "Love!":
            break

        index = int(command[1]) + current_index_position

        if index >= len(data):
            index = 0

        if -1 < index < len(data):
            if data[index] > 0:
                data[index] -= 2
                if data[index] == 0:
                    print(f"Place {index} has Valentine's day.")
            else:
                print(f"Place {index} already had Valentine's day.")

        cupids_last_position = index
        current_index_position = index

    representation_data(data, cupids_last_position)


nums = list(map(int, input().split("@")))
heart_delivery(nums)

# Variant 2
# neighbourhood = [int(hearts) for hearts in input().split('@')]
# position = 0
#
# while True:
#     command = input()
#
#     if command == 'Love!':
#         break
#
#     command = command.split()
#     jump_length = int(command[1])
#
#     if position + jump_length in range(len(neighbourhood)):
#         position += jump_length
#         if neighbourhood[position] == 0:
#             print(f"Place {position} already had Valentine's day.")
#         else:
#             neighbourhood[position] -= 2
#             if neighbourhood[position] == 0:
#                 print(f"Place {position} has Valentine's day.")
#
#     else:
#         position = 0
#         if neighbourhood[position] == 0:
#             print(f"Place {position} already had Valentine's day.")
#         else:
#             neighbourhood[position] -= 2
#             if neighbourhood[position] == 0:
#                 print(f"Place {position} has Valentine's day.")
#
#
# print(f"Cupid's last position was {position}.")
#
# if sum(neighbourhood) == 0:
#     print('Mission was successful.')
# else:
#     counter = 0
#     for house in neighbourhood:
#         if house > 0:
#             counter += 1
#     print(f'Cupid has failed {counter} places.')
#
# # Variant 3
# neighbourhood = list(map(int, input().split("@")))
# index = 0
#
# while True:
#
#     command = input()
#     if command == "Love!":
#         break
#
#     token = command.split()
#     jump = int(token[1])
#     jump_length = index + jump
#
#     if jump_length >= len(neighbourhood):
#         jump_length = 0
#
#     if neighbourhood[jump_length] == 0:
#         print(f"Place {jump_length} already had Valentine's day.")
#     else:
#         neighbourhood[jump_length] -= 2
#         if neighbourhood[jump_length] == 0:
#             print(f"Place {jump_length} has Valentine's day.")
#     index = jump_length
#
# if command == "Love!":
#     print(f"Cupid's last position was {index}.")
#     successful = [i for i in neighbourhood if i != 0]
#
#     if len(successful) == 0:
#         print(f"Mission was successful.")
#     else:
#         print(f"Cupid has failed {len(successful)} places.")