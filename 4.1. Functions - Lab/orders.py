def calculate_order(price, quantity):
    """This function calculates orders."""
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00

    result = price * quantity
    print(f"{result:.2f}")


product = input()
quantity_product = int(input())

calculate_order(product, quantity_product)