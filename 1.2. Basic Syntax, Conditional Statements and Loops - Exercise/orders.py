count_orders = int(input())

total_price = 0

for _ in range(count_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    total_capsules_needed = capsules_needed_per_day * days

    total_price_for_capsules = total_capsules_needed * price_per_capsule

    if (0.01 <= price_per_capsule <= 100.00) and (1 <= days <= 31) and (1 <= capsules_needed_per_day <= 2000):
        print(f"The price for the coffee is: ${total_price_for_capsules:.2f}")

        total_price += total_price_for_capsules

print(f"Total: ${total_price:.2f}")

# Variant 2
# orders = int(input())
#
# total_price = 0
#
# for _ in range(orders):
#     price_per_capsule = float(input())
#     days = int(input())
#     capsules_per_day = int(input())
#
#     if price_per_capsule < 0.01 or price_per_capsule > 100:
#         continue
#
#     if days < 1 or days > 31:    # good practice is to use if
#         continue
#
#     if capsules_per_day < 1 or capsules_per_day > 2000:    # good practice is to use if
#         continue
#
#     order_price = days * price_per_capsule * capsules_per_day    # good practice is to use if
#
#     total_price += order_price
#
#     print(f"The price for the coffee is: ${order_price:.2f}")
#
# print(f"Total: ${total_price:.2f}")