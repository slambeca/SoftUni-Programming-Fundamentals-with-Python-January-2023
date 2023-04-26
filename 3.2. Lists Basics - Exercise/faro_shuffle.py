deck_of_cards = input().split()
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    final_deck = []

    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_the_deck]    # from 0 to the middle
    right_part = deck_of_cards[middle_of_the_deck::]    # from the middle to the end

    for card_index in range(len(left_part)):    # or len(right_part)
        final_deck.append(left_part[card_index])
        final_deck.append(right_part[card_index])

    deck_of_cards = final_deck

print(deck_of_cards)

# Variant 2
# cards = input().split()
# counter = int(input())
#
# for _ in range(counter):
#     first_half = []
#     second_half = []
#
#     for idx in range(1, len(cards) - 1):
#         card = cards[idx]
#         if idx < len(cards) / 2:
#             first_half.append(card)
#         else:
#             second_half.append(card)
#
#     shuffled = []
#
#     first_part_idx = 0
#     second_part_idx = 0
#
#     for idx in range(len(first_half) * 2):
#         if idx % 2 == 0:
#             shuffled.append(second_half[second_part_idx])
#             second_part_idx += 1
#         else:
#             shuffled.append((first_half[first_part_idx]))
#             first_part_idx += 1
#
#     cards = [cards[0]] + shuffled + [cards[-1]]
#
# print(cards)
#
# # Variant 3
# cards = list(input().split())
# faro_shuffle = int(input())
#
# d = int(len(cards) / 2)
#
# new_list = cards
#
# for _ in range(faro_shuffle):
#     first_half = new_list[:d]
#     second_half = new_list[d:]
#     new_list.clear()
#
#     for i in range(len(first_half)):
#         new_list.append(first_half[i])
#         new_list.append(second_half[i])
#
# print(new_list)
#
# # Variant 4
# string = input().split()
# shuffles_count = int(input())
#
# for shuffle in range(shuffles_count):
#     deck = []
#     middle_of_deck = len(string) // 2
#     left_part = string[0:middle_of_deck]
#     right_part = string[middle_of_deck::]
#
#     for card in range(len(left_part)):
#         deck.append(left_part[card])
#         deck.append(right_part[card])
#
#     string = deck
#
# print(string)
