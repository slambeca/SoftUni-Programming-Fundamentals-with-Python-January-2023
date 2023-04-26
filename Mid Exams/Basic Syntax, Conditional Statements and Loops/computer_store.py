input_line = input()

total_sum = 0

while input_line != "special" and input_line != "regular":
    current_sum = float(input_line)

    if current_sum < 0:
        print("Invalid price!")
        input_line = input()
        continue
    else:
        total_sum += current_sum

    input_line = input()

price_with_tax = total_sum * 1.20

taxes_added = price_with_tax - total_sum

if input_line == "special":
    price_with_tax *= 0.9

if total_sum == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!"
          f"\nPrice without taxes: {total_sum:.2f}$"
          f"\nTaxes: {taxes_added:.2f}$"
          f"\n-----------"
          f"\nTotal price: {price_with_tax:.2f}$")


# # Variant 2:
# total_price = 0
#
# while True:
#     command = input()
#
#     if command == "regular" or command == "special":
#         break
#
#     current_price = float(command)
#
#     if current_price < 0:
#         print("Invalid price!")
#         continue
#
#     total_price += current_price
#
# total_price_with_taxes = total_price * 1.20
# taxes = total_price_with_taxes - total_price
#
# if command == "special":
#     total_price_with_taxes *= 0.9
#
# if not total_price:
#     print("Invalid order!")
# else:
#     print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price:.2f}$\n"
#           f"Taxes: {taxes:.2f}$\n-----------\nTotal price: {total_price_with_taxes:.2f}$")
#
# # Variant 3 with using a list
# total_price = []
#
# while True:
#     command = input()
#
#     if command == "regular" or command == "special":
#         break
#
#     current_price = float(command)
#
#     if current_price < 0:
#         print("Invalid price!")
#         continue
#
#     total_price.append(current_price)
#
# total_price_with_taxes = sum(total_price) * 1.20
# taxes = total_price_with_taxes - sum(total_price)
#
# if command == "special":
#     total_price_with_taxes *= 0.9
#
# if not total_price:
#     print("Invalid order!")
# else:
#     print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {sum(total_price):.2f}$\n"
#           f"Taxes: {taxes:.2f}$\n-----------\nTotal price: {total_price_with_taxes:.2f}$")
#
# # Variant 4
# customer_type = ''
# total_price_without_taxes = 0
# total_amount_of_taxes = 0
#
# while True:
#     command = input()
#
#     if command == 'special':
#         customer_type = 'special'
#         break
#     elif command == 'regular':
#         break
#
#     price = float(command)
#
#     if price < 0:
#         print('Invalid price!')
#     else:
#         total_price_without_taxes += price
#         total_amount_of_taxes += price * 0.2
#
# total_price = total_price_without_taxes + total_amount_of_taxes
#
# if total_price == 0:
#     print('Invalid order!')
# else:
#     if customer_type == 'special':
#         total_price -= total_price * 0.1
#
#     print("Congratulations you've just bought a new computer!")
#     print(f'Price without taxes: {total_price_without_taxes:.2f}$')
#     print(f'Taxes: {total_amount_of_taxes:.2f}$')
#     print('-----------')
#     print(f'Total price: {total_price:.2f}$')