items = {"shards": 0, "fragments": 0, "motes": 0}

current_items = input().split()

obtained = False

needed_parts = 250

while not obtained:
    for index in range(0, len(current_items), 2):
        key = current_items[index + 1].lower()
        value = int(current_items[index])

        if key not in items.keys():
            items[key] = 0
        items[key] += value

        if items["shards"] >= needed_parts:
            print(f"Shadowmourne obtained!")
            items[key] -= needed_parts
            obtained = True
        elif items["fragments"] >= needed_parts:
            print(f"Valanyr obtained!")
            items[key] -= needed_parts
            obtained = True
        elif items["motes"] >= needed_parts:
            print(f"Dragonwrath obtained!")
            items[key] -= needed_parts
            obtained = True
        if obtained:
            break
    if obtained:
        break

    current_items = input().split()

for key, value in items.items():
    print(f"{key}: {value}")

# Variant 2 with 3 dictionaries and a function
#
#
# def check_for_item(some_item, some_array):
#     if some_item in some_array:
#         return True
#     return False
#
#
# special_materials = {"shards": 0, "fragments": 0, "motes": 0}
# junk_materials = {}
# legendary_item_by_material = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
#
# crafted = False
#
# while not crafted:
#     line = input()
#
#     materials = line.split()
#
#     for idx in range(0, len(materials), 2):
#         quantity = int(materials[idx])
#         material = materials[idx + 1].lower()
#
#         if check_for_item(material, special_materials):
#             special_materials[material] += quantity
#             if special_materials[material] >= 250:
#                 special_materials[material] -= 250
#                 crafted = True
#                 print(f"{legendary_item_by_material[material]} obtained!")  # no need for if - elif - else
#                 break
#
#         else:
#             if check_for_item(material, junk_materials):
#                 junk_materials[material] += quantity
#             else:
#                 junk_materials[material] = quantity
#
# special_materials.update(junk_materials)
#
# for key, item in special_materials.items():
#     print(f"{key}: {item}")