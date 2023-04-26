products = {}

command = input()

while command != "statistics":
    key, value = command.split(": ")
    if key not in products.keys():
        products[key] = 0    # we are creating a default 0 value for each key

    products[key] += int(value)

    command = input()

print("Products in stock:")

total_values = 0

for key, value in products.items():
    total_values += value
    print(f"- {key}: {value}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {total_values}")

# Variant 2
# products = {}
#
# command = input()
#
# while command != "statistics":
#     key, value = command.split(": ")
#     if key not in products.keys():
#         products[key] = int(value)  # we are creating a default 0 value for each key
#     else:
#         products[key] += int(value)
#
#     command = input()
#
# print("Products in stock:")
#
# total_values = 0
#
# for key, value in products.items():
#     total_values += value
#     print(f"- {key}: {value}")
#
# print(f"Total Products: {len(products)}")
# print(f"Total Quantity: {total_values}")
#
# # Variant 3
# products = {}
#
# command = input()
#
# while command != "statistics":
#     key, value = command.split(": ")
#     if key not in products.keys():
#         products[key] = int(value)  # we are creating a default 0 value for each key
#     else:
#         products[key] += int(value)
#
#     command = input()
#
# print("Products in stock:")
#
# for key, value in products.items():
#     print(f"- {key}: {value}")
#
# print(f"Total Products: {len(products)}")
# print(f"Total Quantity: {sum(products.values())}")