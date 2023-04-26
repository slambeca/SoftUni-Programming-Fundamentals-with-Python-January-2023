from math import floor

group_size = int(input())
days = int(input())

coins_earned = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    coins_earned += 50 - (2 * group_size)

    if day % 3 == 0:
        coins_earned -= (3 * group_size)

    if day % 5 == 0:
        coins_earned += (20 * group_size)
        if day % 3 == 0:
            coins_earned -= (2 * group_size)

print(f"{group_size} companions received {floor(coins_earned / group_size)} coins each.")

# Variant 2
# group_size = int(input())
# days = int(input())
#
# coins_earned = 0
#
# for day in range(1, days + 1):
#     if day % 10 == 0:
#         group_size -= 2
#
#     if day % 15 == 0:
#         group_size += 5
#         coins_earned -= (2 * group_size)
#
#     coins_earned += 50 - (2 * group_size)
#
#     if day % 3 == 0:
#         coins_earned -= (3 * group_size)
#
#     if day % 5 == 0:
#         coins_earned += (20 * group_size)
#
# print(f"{group_size} companions received {coins_earned // group_size} coins each.")
#
# # Variant 3
# import math
#
# group = int(input())
# days = int(input())
# gold = 0
#
# for i in range(1, days + 1):
#     gold += 50
#
#     if i % 15 == 0:
#         group += 5
#
#     if i % 10 == 0:
#         group -= 2
#
#     gold -= group * 2
#
#     if i % 3 == 0:
#         gold -= group * 3
#
#     if i % 5 == 0:
#         gold += group * 20
#         if i % 3 == 0:
#             gold -= group * 2
#
# print(f"{group} companions received {math.floor(gold / group)} coins each.")