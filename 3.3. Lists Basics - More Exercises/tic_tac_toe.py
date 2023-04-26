line_1 = [int(x) for x in input().split()]
line_2 = [int(x) for x in input().split()]
line_3 = [int(x) for x in input().split()]

player_one_wins = False
player_two_wins = False
draw_game = False

# horizontally, vertically, diagonally

if (line_1[0] == 1 and line_1[1] == 1 and line_1[2] == 1) or \
    (line_2[0] == 1 and line_2[1] == 1 and line_2[2] == 1) or \
    (line_3[0] == 1 and line_3[1] == 1 and line_3[2] == 1) or \
    (line_1[0] == 1 and line_2[0] == 1 and line_3[0] == 1) or \
    (line_1[1] == 1 and line_2[1] == 1 and line_3[1] == 1) or \
    (line_1[2] == 1 and line_2[2] == 1 and line_3[2] == 1) or \
    (line_1[0] == 1 and line_2[1] == 1 and line_3[2] == 1) or \
    (line_1[2] == 1 and line_2[1] == 1 and line_3[0] == 1):

    player_one_wins = True

elif (line_1[0] == 2 and line_1[1] == 2 and line_1[2] == 2) or \
    (line_2[0] == 2 and line_2[1] == 2 and line_2[2] == 2) or \
    (line_3[0] == 2 and line_3[1] == 2 and line_3[2] == 2) or \
    (line_1[0] == 2 and line_2[0] == 2 and line_3[0] == 2) or \
    (line_1[1] == 2 and line_2[1] == 2 and line_3[1] == 2) or \
    (line_1[2] == 2 and line_2[2] == 2 and line_3[2] == 2) or \
    (line_1[0] == 2 and line_2[1] == 2 and line_3[2] == 2) or \
    (line_1[2] == 2 and line_2[1] == 2 and line_3[0] == 2):

    player_two_wins = True

else:
    draw_game = True

if player_one_wins:
    print("First player won")
elif player_two_wins:
    print("Second player won")
elif draw_game:
    print("Draw!")