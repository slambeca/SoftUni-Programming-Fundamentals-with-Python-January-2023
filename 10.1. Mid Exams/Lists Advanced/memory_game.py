def is_index_in_range(index, cards_count):
    if 0 <= index < cards_count:
        return True
    return False


def check_indexes_are_valid(index1, index2, count_cards):
    if (
            is_index_in_range(index1, count_cards)
            and is_index_in_range(index2, count_cards)
            and index1 != index2
    ):
        return True
    return False


cards = input().split()

command = input()
n_moves = 0

while command != "end":
    n_moves += 1
    index1, index2 = [int(el) for el in command.split()]
    # if (0 <= index1 < len(cards)) and (0 <= index2 < len(cards)) and (index1 != index2):
    if check_indexes_are_valid(index1, index2, len(cards)):
        if cards[index1] == cards[index2]:
            element = cards[index1]
            cards.pop(index1)
            # Elements are reordered after pop, so we need to use the .remove,
            # because the index is no longer accurate
            cards.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print("Try again!")
    else:
        # punish the player
        element_to_add = f"-{n_moves}a"
        index = len(cards) // 2
        cards.insert(index, element_to_add)
        cards.insert(index, element_to_add)
        print("Invalid input! Adding additional elements to the board")

    if not cards:
        print(f"You have won in {n_moves} turns!")
        exit(0)

    command = input()

print(f"Sorry you lose :(")
print(*cards, sep=' ')

# Variant 2
# sequence_of_elements = input().split()
#
# moves_count = 0
#
# while True:
#     command = input()
#
#     if command == 'end':
#         break
#
#     command = command.split()
#     first_index = int(command[0])
#     second_index = int(command[1])
#
#     moves_count += 1
#
#     if (first_index == second_index) or (first_index < 0) or (second_index < 0) or (first_index >= len(sequence_of_elements)) or (second_index >= len(sequence_of_elements)):
#         index = len(sequence_of_elements) // 2
#         sequence_of_elements.insert(index, f'-{moves_count}a')
#         sequence_of_elements.insert(index, f'-{moves_count}a')
#         print("Invalid input! Adding additional elements to the board")
#
#     elif sequence_of_elements[first_index] == sequence_of_elements[second_index]:
#         print(f'Congrats! You have found matching elements - {sequence_of_elements[first_index]}!')
#         element = sequence_of_elements.pop(first_index)
#         sequence_of_elements.remove(element)
#     else:
#         print("Try again!")
#
#     if len(sequence_of_elements) == 0:
#         print(f'You have won in {moves_count} turns!')
#         break
#
# if len(sequence_of_elements) > 0:
#     print("Sorry you lose :(")
#     print(' '.join(sequence_of_elements))