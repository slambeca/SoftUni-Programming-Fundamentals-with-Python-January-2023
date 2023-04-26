food_and_quantities = input().split()    # ['bread', '10', 'butter', '4', 'sugar', '9', 'jam', '12']

bakery = {}    # we are creating an empty dictionary

for item in range(0, len(food_and_quantities), 2):
    key = food_and_quantities[item]
    value = food_and_quantities[item + 1]
    bakery[key] = int(value)

print(bakery)

# Variant 2
# items = input().split()
#
# bakery = {}
#
# for index in range(0, len(items), 2):
#     key = items[index]
#     value = int(items[index + 1])
#     bakery[key] = value  # this is like append
#
# print(bakery)
#
# # Variant 3
# items = input().split()
#
# bakery = {}
#
# for index in range(0, len(items), 2):
#     bakery[items[index]] = int(items[index + 1])
#
# print(bakery)