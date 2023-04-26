# team_a = ["A-" + str(s) for s in range(1, 12)]    # instead of ["A-1", "A-2", "A-3", etc...]
# team_b = ["B-" + str(s) for s in range(1, 12)]

team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

players = input().split()

game_was_terminated = False

for player in players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:    # we stop reading the input in the for loop after one of
        # the teams is left with less than 7 people (this is a hidden Judge test)
        game_was_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if game_was_terminated:
    print("Game was terminated")

# Variant 2
# total_players_list = set(input().split())
#
# a_players = 11
# b_players = 11
#
# for player in total_players_list:
#     if "A" in player:
#         a_players -= 1
#         if a_players < 7:
#             break
#     elif "B" in player:    # always use elif to save resources
#         b_players -= 1
#         if b_players < 7:
#             break
#
# print(f"Team A - {a_players}; Team B - {b_players}")
#
# if a_players < 7 or b_players < 7:
#     print("Game was terminated")
#
# # Variant 3
# cards = input().split()
#
# first_team_sent_off_players = []
# second_team_sent_off_players = []
#
# should_terminate = False
#
# for card in cards:
#     if card in first_team_sent_off_players or card in second_team_sent_off_players:
#         continue
#
#     card_args = card.split("-")
#     team_name = card_args[0]
#     player_number = card_args[1]
#
#     is_first_team = team_name == "A"    # is_first_team == "A", True of False
#
#     if is_first_team:
#         first_team_sent_off_players.append(card)
#     else:
#         second_team_sent_off_players.append(card)
#
#     if len(first_team_sent_off_players) > 4 or len(second_team_sent_off_players) > 4:
#         should_terminate = True
#         break
#
# initial_player_count = 11
#
# print(f"Team A - {initial_player_count - len(first_team_sent_off_players)}; Team B - "
#       f"{initial_player_count - len(second_team_sent_off_players)}")
#
# if should_terminate:
#     print("Game was terminated")
