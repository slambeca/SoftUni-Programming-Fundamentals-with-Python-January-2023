quantity = int(input())     # of products to buy
days = int(input())    # left to Christmas

total_spending = 0
total_spirit = 0

days_counter = 0    # this checks if the last day is a tenth day

for _ in range(days, 0, -1):    # days_counter instead of _ to determine which day it is
    days_counter += 1

    if days_counter % 11 == 0:
        quantity += 2

    if days_counter % 2 == 0:
        total_spending += 2 * quantity
        total_spirit += 5
    if days_counter % 3 == 0:
        total_spending += 5 * quantity + 3 * quantity
        total_spirit += 3 + 10
    if days_counter % 5 == 0:
        total_spending += 15 * quantity
        total_spirit += 17
        if days_counter % 3 == 0:
            total_spirit += 30

    if days_counter % 10 == 0:
        total_spirit -= 20
        total_spending += 5 + 3 + 15

if days_counter % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_spending}")
print(f"Total spirit: {total_spirit}")