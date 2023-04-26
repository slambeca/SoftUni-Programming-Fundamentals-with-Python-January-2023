products = {}

while True:
    command = input()

    if command == "buy":
        break

    command = command.split()

    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product not in products:
        products[product] = [price, quantity]

    elif product in products:
        products[product][1] += quantity
        if price != products[product][0]:
            products[product][0] = price

for product in products:
    total_price = products[product][0] * products[product][1]
    print(f"{product} -> {total_price:.2f}")

# Variant 2 with a function
#
#
# def check_for_item(some_item, some_array):
#     if some_item not in some_array:
#         return True
#     return False
#
#
# dictionary = {}  # {'Beer': (2.2, 100), 'IceTea': (1.5, 50), 'NukaCola': (3.3, 80), 'Water': (1.0, 500)}
#
# while True:
#     command = input()
#
#     if command == "buy":
#         break
#
#     product, price, quantity = command.split()
#
#     price = float(price)
#     quantity = int(quantity)
#
#     if check_for_item(product, dictionary):
#         dictionary[product] = [float(price), int(quantity)]
#     else:
#         dictionary[product][1] += quantity
#         if price != dictionary[product][0]:
#             dictionary[product][0] = price
#
# for key, value in dictionary.items():
#     total_price = value[0] * value[1]
#     print(f"{key} -> {total_price:.2f}")
#
# # Variant 3
#
#
# def check_for_item(some_item, some_array):
#     if some_item not in some_array:
#         return True
#     return False
#
#
# def check_price(old_price, new_price):
#     if old_price != new_price:
#         return True
#     return False
#
#
# dictionary = {}    # {'Beer': (2.2, 100), 'IceTea': (1.5, 50), 'NukaCola': (3.3, 80), 'Water': (1.0, 500)}
#
# while True:
#     command = input()
#
#     if command == "buy":
#         break
#
#     product, price, quantity = command.split()
#
#     price = float(price)
#     quantity = int(quantity)
#
#     if check_for_item(product, dictionary):
#         dictionary[product] = [float(price), int(quantity)]
#     else:
#         dictionary[product][1] += quantity
#         if check_price(price, dictionary[product][0]):
#             dictionary[product][0] = price
#
# for key, value in dictionary.items():
#     total_price = value[0] * value[1]
#     print(f"{key} -> {total_price:.2f}")
#
#
# # Variant 4
# price_by_product = {}
# quantity_by_product = {}
#
# while True:
#     line = input()
#
#     if line == "buy":
#         break
#
#     args = line.split()
#
#     product = args[0]
#     price = float(args[1])
#     quantity = int(args[2])
#
#     price_by_product[product] = price  # this will always update the price
#
#     if product in price_by_product:
#         quantity_by_product[product] += quantity
#     else:
#         quantity_by_product[product] = quantity
#
# for product in price_by_product.keys():
#     price = price_by_product[product]
#     quantity = quantity_by_product[product]
#     total_price = price * quantity
#
#     print(f"{product} -> {total_price:.2f}")