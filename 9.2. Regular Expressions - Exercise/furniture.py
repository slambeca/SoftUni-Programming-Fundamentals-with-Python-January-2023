import re

bought_furniture = []
total_money = 0

pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"

# First group is the name of the furniture
# Second group is the price of the furniture
# Third group is the quantity of the furniture

command = input()

while command != "Purchase":
    matches = re.search(pattern, command)

    if matches:
        furniture, price, quantity = matches.groups()    # = matches.groups(1), matches.groups(2), matches.groups(3)

        bought_furniture.append(furniture)
        total_money += float(price) * int(quantity)

    command = input()

print("Bought furniture:")
for furniture in bought_furniture:    # '\n'.join(bought_furniture) (without for loop) is 75/100 in Judge
    print(furniture)
print(f"Total money spend: {total_money:.2f}")

# Variant 2
# import re
#
# pattern = r">>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)"
#
# total_price = 0
# bought_items = []
#
# while True:
#     line = input()
#
#     if line == "Purchase":
#         break
#
#     matches = re.findall(pattern, line)
#
#     if not matches:
#         continue
#
#     for match in matches:
#         item = match[0]
#         price = float(match[1])
#         quantity = int(match[3])
#
#         bought_items.append(item)
#         total_price += price * quantity
#
# print("Bought furniture:")
# for product in bought_items:
#     print(product)
# print(f"Total money spend: {total_price:.2f}")
#
# # Variant 3 with group naming
# import re
#
# pattern = r">>(?P<Furniture>[A-Za-z]+)<<(?P<Price>\d+(\.\d+)?)!(?P<Quantity>\d+)"
#
# total_price = 0
# bought_items = []
#
# while True:
#     line = input()
#
#     if line == "Purchase":
#         break
#
#     match = re.match(pattern, line)
#
#     if not match:
#         continue
#
#     groups = match.groupdict()
#     bought_items.append(groups["Furniture"])
#     total_price += float(groups["Price"]) * int(groups["Quantity"])
#
# print("Bought furniture:")
# for product in bought_items:
#     print(product)
# print(f"Total money spend: {total_price:.2f}")