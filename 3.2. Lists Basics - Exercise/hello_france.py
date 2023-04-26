items_with_prices = input().split("|")  # ['Clothes->43.30', 'Shoes->25.25', 'Clothes->36.52', 'Clothes->20.90',
# 'Accessories->15.60']
budget = float(input())

ticket_price = 150
money_spent = 0

list_new_prices = []

for product in items_with_prices:
    product_args = product.split("->")
    product_type = product_args[0]  # Clothes
    product_price = float(product_args[1])  # 25.25

    if product_type == "Clothes" and product_price > 50.00:
        continue

    if product_type == "Shoes" and product_price > 35.00:
        continue

    if product_type == "Accessories" and product_price > 20.50:
        continue

    if budget < product_price:
        continue

    budget -= product_price
    list_new_prices.append(product_price * 1.4)
    money_spent += product_price

profit = sum(list_new_prices) - money_spent

for number in list_new_prices:
    print(f"{number:.2f}", end=" ")

print(f"\nProfit: {profit:.2f}")

if budget + sum(list_new_prices) >= ticket_price:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")