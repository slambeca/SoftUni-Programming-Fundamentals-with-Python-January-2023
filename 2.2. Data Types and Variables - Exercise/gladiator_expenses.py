lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0

times_shield_broke = 0

for lost_fight in range(1, lost_fights_count + 1):
    if lost_fight % 2 == 0:
        total_expenses += helmet_price
    if lost_fight % 3 == 0:
        total_expenses += sword_price
    if lost_fight % 2 == 0 and lost_fight % 3 == 0:    # if his helmet and his sword are broken
        times_shield_broke += 1
        total_expenses += shield_price
        if times_shield_broke % 2 == 0:
            total_expenses += armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")

# Variant 2
# lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
#
# helmet_counter = 0
# sword_counter = 0
# shield_counter = 0
# armor_counter = 0
#
# for fight in range(1, lost_fights + 1):
#     if fight % 2 == 0:
#         helmet_counter += 1
#     if fight % 3 == 0:
#         sword_counter += 1
#     if fight % 6 == 0:
#         shield_counter += 1
#     if fight % 12 == 0:
#         armor_counter += 1
#
# total_price = helmet_counter * helmet_price + sword_counter * sword_price + shield_counter * shield_price + \
#               armor_counter * armor_price
#
# print(f"Gladiator expenses: {total_price:.2f} aureus")
#
# # Variant 3
# lost = 0
#
# money = lost // 2 * helmet_price + lost // 3 * sword_price + lost // 6 * shield_price + lost // 12 * armor_price
