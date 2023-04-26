text = input()

check_wolf = text.split(", ")

check_position = len(check_wolf) - 1

message = ""

for wolf in check_wolf:
    if wolf == "wolf" and check_position == 0:
        print(f"Please go away and stop eating my sheep")
    elif wolf == "wolf":
        print(f"Oi! Sheep number {check_position}! You are about to be eaten by a wolf!")

    check_position -= 1

print(message)