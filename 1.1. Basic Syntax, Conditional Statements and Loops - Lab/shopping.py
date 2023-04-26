budget = int(input())

money_left = budget

no_more_money = False

input_line = input()

while input_line != "End":
    current_prices = int(input_line)

    money_left -= current_prices

    if money_left < 0:
        no_more_money = True
        break

    input_line = input()

if no_more_money:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")

# Variant 2
# budget = int(input())
#
# current_price_as_string = input()
#
# while current_price_as_string != "End":
#     current_price = int(current_price_as_string)
#
#     budget -= current_price
#
#     if budget < 0:
#         print("You went overdraft!")
#         exit()
#
#     current_price_as_string = input()
#
# print("You bought everything needed.")