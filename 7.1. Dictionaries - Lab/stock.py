products = input().split()    # ['cheese', '10', 'bread', '5', 'ham', '10', 'chocolate', '3']

stock = {}

for item in range(0, len(products), 2):
    key = products[item]
    value = int(products[item + 1])
    stock[key] = value    # {'cheese': 10, 'bread': 5, 'ham': 10, 'chocolate': 3}

searched_products = input().split()

for product in searched_products:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

# Variant 2
# products = input().split()    # ['cheese', '10', 'bread', '5', 'ham', '10', 'chocolate', '3']
#
# stock = {}
#
# for item in range(0, len(products), 2):
#     stock[products[item]] = int(products[item + 1]) # {'cheese': 10, 'bread': 5, 'ham': 10, 'chocolate': 3}
#
# searched_products = input().split()
#
# for product in searched_products:
#     if product in stock:    # if product in stock.keys()
#         # quantity = stock[product]
#         print(f"We have {stock[product]} of {product} left")    # quantity instead of stock[product]
#     else:
#         print(f"Sorry, we don't have {product}")