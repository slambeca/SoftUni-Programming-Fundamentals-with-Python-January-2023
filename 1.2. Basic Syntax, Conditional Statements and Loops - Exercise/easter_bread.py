budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) * 0.25

loaf_price = eggs_price + flour_price + milk_price

loafs_counter = 0

colored_eggs_counter = 0

while loaf_price <= budget:    # keep making loaves until you have enough budget
    loafs_counter += 1
    budget -= loaf_price
    colored_eggs_counter += 3

    if loafs_counter % 3 == 0:
        colored_eggs_counter -= (loafs_counter - 2)

print(f"You made {loafs_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs "
      f"and {budget:.2f}BGN left.")

# Variant 2 (the same)
# budget = float(input())
# price_for_kg_flour = float(input())
#
# price_pack_eggs = price_for_kg_flour * 0.75
# price_liter_milk = price_for_kg_flour * 1.25
#
# price_one_loaf_bread = price_for_kg_flour + price_pack_eggs + (price_liter_milk * 0.25)    # 2.578125
#
# easter_loaves_made = 0
# eggs_received = 0
#
# while price_one_loaf_bread <= budget:    # keep making loaves until you have enough budget
#     budget -= price_one_loaf_bread
#     easter_loaves_made += 1
#
#     eggs_received += 3
#
#     if easter_loaves_made % 3 == 0:
#         eggs_received -= (easter_loaves_made - 2)
#
# print(f"You made {easter_loaves_made} loaves of Easter bread! Now you have {eggs_received} eggs "
#       f"and {budget:.2f}BGN left.")