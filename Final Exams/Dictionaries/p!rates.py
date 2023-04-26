command = input()    # Tortuga||345000||1250

dictionary = {}    # {'Tortuga': [345000, 1250], 'Santo Domingo': [240000, 630], 'Havana': [410000, 1100]}

while command != "Sail":
    cities = command.split("||")    # double pipes ["Tortuga", "345000", "1250"]

    city = cities[0]    # Tortuga
    population = int(cities[1])    # 345 000
    gold = int(cities[2])    # 1250

    if city not in dictionary:
        dictionary[city] = []
        dictionary[city].append(population)    # {"Tortuga": [345000, 1250]}
        dictionary[city].append(gold)
    else:
        dictionary[city][0] += population
        dictionary[city][1] += gold

    command = input()

while True:
    command = input()

    if command == "End":
        break

    command = command.split("=>")

    action = command[0]    # Plunder
    town = command[1]    # Tortuga

    if action == "Plunder":
        people = int(command[2])
        gold = int(command[3])

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        dictionary[town][0] -= people
        dictionary[town][1] -= gold

        if dictionary[town][0] == 0 or dictionary[town][1] == 0:
            print(f"{town} has been wiped off the map!")
            del dictionary[town]

    elif action == "Prosper":
        gold = int(command[2])

        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            dictionary[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {dictionary[town][1]} gold.")

if len(dictionary) < 1:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(dictionary)} wealthy settlements to go to:")
    for key, value in dictionary.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")

# # Variant 2 with nested dictionaries using dict[key][key]
# data = input()
#
# cities = {}
#
# while data != "Sail":
#     splitted_data = data.split("||")
#     city = splitted_data[0]
#     population = int(splitted_data[1])
#     gold = int(splitted_data[2])
#
#     if city not in cities:
#         cities[city] = {"population": population, "gold": gold}
#     else:
#         cities[city]["population"] += population
#         cities[city]["gold"] += gold
#
#     data = input()
#
# data = input()
#
# while data != "End":
#     splitted_data = data.split("=>")
#     command = splitted_data[0]
#     city = splitted_data[1]
#
#     if command == "Plunder":
#         people = int(splitted_data[2])
#         gold = int(splitted_data[3])
#
#         cities[city]["population"] -= people
#         cities[city]["gold"] -= gold
#         print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
#
#         if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
#             del cities[city]
#             print(f"{city} has been wiped off the map!")
#
#     elif command == "Prosper":
#         gold = int(splitted_data[2])
#         if gold < 0:
#             print(f"Gold added cannot be a negative number!")
#         else:
#             cities[city]["gold"] += gold
#             print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
#
#     data = input()
#
# if not cities:
#     print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
# else:
#     print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
#     for city, values in cities.items():
#         print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")
#         # print(f"{city} -> Population: {values['population']} citizens, Gold: {values['gold']} kg")
#
# # Variant 3
# cities = {}
#
# while True:
#     command = input()
#
#     if command == 'Sail':
#         break
#
#     command = command.split('||')
#     city = command[0]
#     population = int(command[1])
#     gold = int(command[2])
#
#     if city in cities:
#         cities[city][0] += population
#         cities[city][1] += gold
#     else:
#         cities[city] = []
#         cities[city].append(population)
#         cities[city].append(gold)
#
# while True:
#     command = input()
#
#     if command == 'End':
#         break
#
#     command = command.split('=>')
#     action = command[0]
#
#     if action == 'Plunder':
#         town = command[1]
#         people = int(command[2])
#         gold = int(command[3])
#
#         print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
#
#         cities[town][0] -= people
#         cities[town][1] -= gold
#
#         if cities[town][0] == 0 or cities[town][1] == 0:
#             del cities[town]
#             print(f'{town} has been wiped off the map!')
#
#     elif action == 'Prosper':
#         town = command[1]
#         gold = int(command[2])
#
#         if gold > 0:
#             cities[town][1] += gold
#             print(f'{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.')
#         else:
#             print('Gold added cannot be a negative number!')
#
# sorted_cities = sorted(cities.items(), key=lambda city: (-city[1][1], city[0]))
#
# if len(sorted_cities) > 0:
#     print(f'Ahoy, Captain! There are {len(sorted_cities)} wealthy settlements to go to:')
#     for city in sorted_cities:
#         print(f'{city[0]} -> Population: {city[1][0]}, Gold: {city[1][1]} kg')
# else:
#     print('Ahoy, Captain! All targets have been plundered and destroyed!')
#
# # Variant 4
# cities_data = {}
#
#
# def is_city_visited(visited_towns, town, people, treasury):
#     if town not in visited_towns:
#         visited_towns[town] = [people, treasury]
#     else:
#         visited_towns[town][0] += people
#         visited_towns[town][1] += treasury
#     return visited_towns
#
#
# def plunder_action(towns, robbed_town, killed_people, robbed_treasury):
#     towns[robbed_town][0] -= killed_people
#     towns[robbed_town][1] -= robbed_treasury
#     print(f"{robbed_town} plundered! {robbed_treasury} gold stolen, {killed_people} citizens killed.")
#     if towns[robbed_town][0] == 0 or towns[robbed_town][1] == 0:
#         towns.pop(robbed_town)
#         print(f"{robbed_town} has been wiped off the map!")
#     return towns
#
#
# def prosper_action(towns, growth_city, increasing_treasury):
#     if increasing_treasury < 0:
#         print("Gold added cannot be a negative number!")
#         return towns
#     towns[growth_city][1] += increasing_treasury
#     print(f"{increasing_treasury} gold added to the city treasury. {growth_city} now has {towns[growth_city][1]} gold.")
#     return towns
#
#
# while True:
#     targets = input()
#     if targets == "Sail":
#         break
#
#     [city, population, gold] = targets.split("||")
#     population = int(population)
#     gold = int(gold)
#
#     cities_data = is_city_visited(cities_data, city, population, gold)
#
# while True:
#     actions_data = input()
#     if actions_data == "End":
#         break
#
#     action = actions_data.split("=>")
#
#     if action[0] == "Plunder":
#         robbed_city = action[1]
#         killed_population = int(action[2])
#         robbed_gold = int(action[3])
#         cities_data = plunder_action(cities_data, robbed_city, killed_population, robbed_gold)
#     elif action[0] == "Prosper":
#         economic_growth_city = action[1]
#         increasing_gold = int(action[2])
#         cities_data = prosper_action(cities_data, economic_growth_city, increasing_gold)
#
# filtered_settlements = sorted(cities_data.items(), key=lambda x: (-x[1][1], x[0][0]))
#
# if len(cities_data) > 0:
#     print(f"Ahoy, Captain! There are {len(cities_data)} wealthy settlements to go to:")
#     for left_town, town_data in filtered_settlements:
#         print(f"{left_town} -> Population: {town_data[0]} citizens, Gold: {town_data[1]} kg")
# else:
#     print(f"Ahoy, Captain! All targets have been plundered and destroyed!")