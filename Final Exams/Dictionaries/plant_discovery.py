number = int(input())  # 3

dictionary = {}  # {'Arnoldii': [4, []], 'Woodii': [7, [10]], 'Welwitschia': [2, []]}

for _ in range(number):
    command = input().split("<->")  # ["Arnoldii", "4"]

    plant = command[0]  # "Arnoldii"
    rarity = int(command[1])  # 4
    rating = []

    if plant not in dictionary.keys():
        dictionary[plant] = []
        dictionary[plant].append(rarity)
        dictionary[plant].append(rating)
    else:
        dictionary[plant][0] = rarity

while True:
    command = input()

    if command == "Exhibition":
        break

    command = command.split()  # ["Rate", "Woodii"]

    action = command[0]  # "Rate"
    plant = command[1]  # "Woodii"

    if plant in dictionary.keys():
        if action == "Rate:":
            rating = int(command[3])
            dictionary[plant][1].append(rating)

        elif action == "Update:":
            new_rarity = command[3]
            dictionary[plant][0] = new_rarity

        elif action == "Reset:":
            dictionary[plant][1].clear()

    else:
        print("error")

print(f"Plants for the exhibition:")

for plant in dictionary.keys():
    rarity = dictionary[plant][0]
    rating = 0
    if len(dictionary[plant][1]):
        rating = sum(dictionary[plant][1]) / len(dictionary[plant][1])
    print(f"- {plant}; Rarity: {rarity}; Rating: {rating:.2f}")

# # Variant 2
#
# count_plants = int(input())
#
# all_plants = {}
#
# for _ in range(count_plants):
#     plant, rarity = input().split("<->")
#     if plant in all_plants:
#         all_plants[plant]['rarity'] = rarity
#         continue
#     all_plants[plant] = all_plants.get(plant, {'rarity': rarity, 'rating': []})
#
# command = input()
#
# while command != "Exhibition":
#     command = command.split()
#     action = command[0]
#     current_plant = command[1]
#
#     if current_plant not in all_plants:
#         print("error")
#         command = input()
#         continue
#
#     if action == "Rate:":
#         rating = int(command[3])
#         all_plants[current_plant]['rating'].append(rating)
#
#     elif action == "Update:":
#         new_rarity = int(command[3])
#         all_plants[current_plant]['rarity'] = new_rarity
#
#     elif action == "Reset:":
#         all_plants[current_plant]['rating'] = []
#
#     command = input()
#
# print(f"Plants for the exhibition:")
#
# for plant in all_plants:
#     rarity = all_plants[plant]['rarity']
#     rating = 0
#
#     if len(all_plants[plant]['rating']):
#         rating = sum(all_plants[plant]['rating']) / len(all_plants[plant]['rating'])
#     print(f"- {plant}; Rarity: {rarity}; Rating: {rating:.2f}")
#
# # Variant 3
#
#
# class Plant:
#     def __init__(self, name, rarity):
#         self.name = name
#         self.rarity = rarity
#         self.ratings = []
#
#     def rating(self):
#         if self.ratings:
#             return sum(self.ratings) / len(self.ratings)
#         return 0
#
#
# plants = {}
#
# n = int(input())
# for num in range(n):
#     token = input().split('<->')
#     plant_name = token[0]
#     plant_rarity = token[1]
#     plants[plant_name] = Plant(plant_name, int(plant_rarity))
#
# command = input()
# while command != 'Exhibition':
#     token_2 = command.split(': ')
#     token_3 = token_2[1].split(' - ')
#     plant_name = token_3[0]
#     command_type = token_2[0]
#
#     if plant_name not in plants:
#         print('error')
#
#     elif command_type == 'Rate':
#         rating = token_3[1]
#         plants[plant_name].ratings.append(int(rating))
#
#     elif command_type == 'Update':
#         new_rarity = int(token_3[1])
#         plants[plant_name].rarity = new_rarity
#
#     elif command_type == 'Reset':
#         plants[plant_name].ratings.clear()
#
#     else:
#         print('error')
#
#     command = input()
#
# sorted_plants = sorted(plants.values(), key=lambda p: (p.rarity, p.rating()), reverse=True)
#
# print(f'Plants for the exhibition:')
# for plant in sorted_plants:
#     print(f'- {plant.name}; Rarity: {plant.rarity}; Rating: {plant.rating():.2f}')
#
# # Variant 4
# number_of_plants = int(input())
# plants_data = {}
#
# for _ in range(number_of_plants):
#     [plant, rarity] = input().split("<->")
#     rarity = int(rarity)
#     if plant not in plants_data:
#         plants_data[plant] = {"rarity": rarity, "rating": []}
#     else:
#         plants_data[plant]["rarity"] += rarity
#
# while True:
#     command = input()
#     if command == "Exhibition":
#         break
#
#     actions = command.split(":")
#     current_action = actions[0]
#     current_data = actions[1].split(" - ")
#
#     if current_action == "Rate":
#         current_plant = current_data[0].strip()
#         current_rating = int(current_data[1])
#         if current_plant not in plants_data:
#             print("error")
#             continue
#         plants_data[current_plant]["rating"].append(current_rating)
#     elif current_action == "Update":
#         current_plant = current_data[0].strip()
#         new_rarity = int(current_data[1])
#         if current_plant not in plants_data:
#             print("error")
#             continue
#         plants_data[current_plant]["rarity"] = new_rarity
#     elif current_action == "Reset":
#         current_plant = current_data[0].strip()
#         if current_plant not in plants_data:
#             print("error")
#             continue
#         plants_data[current_plant]["rating"].clear()
#     else:
#         print("error")
#
# for rating in plants_data.values():
#     if len(rating["rating"]) > 0:
#         rating["rating"] = (sum(rating["rating"]) / len(rating["rating"]))
#     else:
#         rating["rating"] = 0
#
# filtered_plants = sorted(plants_data.items(), key=lambda x: (-x[1]["rarity"], -x[1]["rating"]))
#
# print("Plants for the exhibition:")
#
# for plant, data in filtered_plants:
#     print(f"- {plant}; Rarity: {data['rarity']}; Rating: {data['rating']:.2f}")
#
# # Variant 5 only with functions
#
#
# def create_plants_data(plants, number):
#     for _ in range(number):
#         data = input().split("<->")
#         name_of_plant = data[0]
#         rarity = int(data[1])
#
#         if name_of_plant not in plants:
#             plants[name_of_plant] = {"rarity": rarity, "rating": []}
#         else:
#             plants[name_of_plant]["rarity"] += rarity
#
#     return plants
#
#
# def additional_plants_data(plants):
#     while True:
#         command = input().split(": ")
#
#         if command[0] == "Exhibition":
#             break
#
#         data = command[1].split(" - ")
#         type_of_command = command[0]
#         plant = data[0]
#
#         if plant not in plants:
#             print("error")
#             continue
#
#         if type_of_command == "Rate":
#             rating = int(data[1])
#             plants[plant]["rating"].append(rating)
#
#         elif type_of_command == "Update":
#             new_rarity = int(data[1])
#             plants[plant]["rarity"] = new_rarity
#
#         elif type_of_command == "Reset":
#             plants[plant]["rating"].clear()
#
#     return plants
#
#
# def print_function(plants):
#     print(f"Plants for the exhibition:")
#
#     for dict_el in plants:
#         if len(plants[dict_el]["rating"]) > 0:
#             average_rating = sum(plants[dict_el]["rating"]) / len(plants[dict_el]["rating"])
#         else:
#             average_rating = 0
#         rarity = plants[dict_el]["rarity"]
#         print(f"- {dict_el}; Rarity: {rarity}; Rating: {average_rating:.2f}")
#
#
# def plant_discovery(number):
#     plants = {}
#
#     create_plants_data(plants, number)
#     additional_plants_data(plants)
#     print_function(plants)
#
#
# n = int(input())
# plant_discovery(n)