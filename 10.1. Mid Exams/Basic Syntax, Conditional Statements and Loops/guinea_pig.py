food_quantity_kgs = float(input())
hay_quantity_kgs = float(input())
cover_quantity_kgs = float(input())
guinea_pig_weight_kgs = float(input())

month = 30

count_days = 0

go_to_store = False

for _ in range(month):
    count_days += 1

    food_quantity_kgs -= 0.3

    if count_days % 2 == 0:
        hay_quantity_kgs -= food_quantity_kgs * 0.05

    if count_days % 3 == 0:
        cover_quantity_kgs -= guinea_pig_weight_kgs / 3

    if int(food_quantity_kgs) <= 0 or hay_quantity_kgs <= 0 or cover_quantity_kgs <= 0:
        go_to_store = True
        break

if go_to_store:
    print(f"Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity_kgs:.2f}, Hay: {hay_quantity_kgs:.2f}, "
      f"Cover: {cover_quantity_kgs:.2f}.")

# Variant 2
# food_in_gr = float(input()) * 1000
# hay_in_gr = float(input()) * 1000
# cover_in_gr = float(input()) * 1000
# guinea_pig_weight_gr = float(input()) * 1000
#
# month = 30
#
# go_to_store = False
#
# for day in range(1, month + 1):
#     food_in_gr -= 300
#
#     if day % 2 == 0:
#         hay_in_gr -= food_in_gr * 0.05
#
#     if day % 3 == 0:
#         cover_in_gr -= (guinea_pig_weight_gr / 3)
#
#     if food_in_gr <= 0 or hay_in_gr <= 0 or cover_in_gr <= 0:
#         print(f"Merry must go to the pet store!")
#         go_to_store = True
#         break
#
# if not go_to_store:
#     print(f"Everything is fine! Puppy is happy! Food: {food_in_gr / 1000:.2f}, Hay: {hay_in_gr / 1000:.2f}, "
#         f"Cover: {cover_in_gr / 1000:.2f}.")