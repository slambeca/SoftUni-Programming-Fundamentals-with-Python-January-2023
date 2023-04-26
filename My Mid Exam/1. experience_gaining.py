xp_needed = float(input())
count_battles = int(input())

total_xp_earned = 0

xp_collected = False

battles = 0

for battle in range(1, count_battles + 1):
    current_xp_gained = float(input())

    battles += 1

    if battle % 3 == 0:
        current_xp_gained *= 1.15

    if battle % 5 == 0:
        current_xp_gained *= 0.9

    if battle % 15 == 0:
        current_xp_gained *= 1.05

    total_xp_earned += current_xp_gained

    if total_xp_earned >= xp_needed:
        xp_collected = True
        break

if xp_collected:
    print(f"Player successfully collected his needed experience for {battles} battles.")
else:
    diff = abs(total_xp_earned - xp_needed)
    print(f"Player was not able to collect the needed experience, {diff:.2f} more needed.")