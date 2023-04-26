number_of_cars = int(input())
cars = {}

for number in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    cars[car] = []
    cars[car].extend([int(mileage), int(fuel)])

while True:
    command = input()

    if command == 'Stop':
        break

    command = command.split(' : ')
    action = command[0]

    if action == 'Drive':
        current_car = command[1]
        distance = int(command[2])
        fuel_required = int(command[3])
        if cars[current_car][1] < fuel_required:
            print('Not enough fuel to make that ride')
        else:
            cars[current_car][0] += distance
            cars[current_car][1] -= fuel_required
            print(f'{current_car} driven for {distance} kilometers. {fuel_required} liters of fuel consumed.')
            if cars[current_car][0] >= 100_000:
                print(f'Time to sell the {current_car}!')
                del cars[current_car]

    elif action == 'Refuel':
        current_car = command[1]
        fuel_to_refill = int(command[2])
        tank_maximum = 75

        if cars[current_car][1] + fuel_to_refill > tank_maximum:
            fuel_to_refill = (tank_maximum - cars[current_car][1])
        cars[current_car][1] += fuel_to_refill
        print(f'{current_car} refueled with {fuel_to_refill} liters')

    elif action == 'Revert':
        current_car = command[1]
        kilometers = int(command[2])

        if cars[current_car][0] - kilometers >= 10_000:
            cars[current_car][0] -= kilometers
            print(f'{current_car} mileage decreased by {kilometers} kilometers')
        else:
            cars[current_car][0] = 10_000

sorted_cars = sorted(cars.items(), key=lambda data: (-data[1][0], data[0]))

for car, data in sorted_cars:
    print(f'{car} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.')

# Variant 2
# num_cars = int(input())
#
# cars_data = {}
#
#
# def drive(car, type, distance, fuel):
#     if car[type]["fuel"] < fuel:
#         print("Not enough fuel to make that ride")
#         return car
#     else:
#         car[type]["fuel"] -= fuel
#         car[type]["mileage"] += distance
#         print(f"{type} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
#         if car[type]["mileage"] >= 100000:
#             print(f"Time to sell the {type}!")
#             del car[type]
#         return car
#
#
# def refuel(car, type, fuel):
#     req_fuel = 75-car[type]["fuel"]
#     car[type]["fuel"] += fuel
#     if car[type]["fuel"] >= 75:
#         car[type]["fuel"] = 75
#         print(f"{type} refueled with {req_fuel} liters")
#         return car
#     else:
#         print(f"{type} refueled with {fuel} liters")
#         return car
#
#
# def revert(car, type, kilometers):
#     car[type]["mileage"] -= kilometers
#     if car[type]["mileage"] < 10000:
#         car[type]["mileage"] = 10000
#         return car
#     else:
#         print(f"{type} mileage decreased by {kilometers} kilometers")
#         return car
#
#
# for cars in range(num_cars):
#     [type, mileage, fuel] = input().split("|")
#     mileage = int(mileage)
#     fuel = int(fuel)
#     cars_data[type] = {"mileage": mileage, "fuel": fuel}
#
# while True:
#     command = input()
#     if command == "Stop":
#         break
#
#     action = command.split(" : ")
#
#     if action[0] == "Drive":
#         cars_data = drive(cars_data, action[1], int(action[2]), int(action[3]))
#     elif action[0] == "Refuel":
#         cars_data = refuel(cars_data, action[1], int(action[2]))
#     elif action[0] == "Revert":
#         cars_data = revert(cars_data, action[1], int(action[2]))
#
# filtered_cars = sorted(cars_data.items(), key=lambda x: (-x[1]["mileage"], x[0]))
#
# for car, data in filtered_cars:
#     print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")
#
# # Variant 3
# number_of_cars = int(input())
#
# dictionary = {}    # {'Audi A6': [38000, 62], 'Mercedes CLS': [11000, 35], 'Volkswagen Passat CC': [45678, 5]}
#
# MAX_FUEL = 75
#
# for _ in range(number_of_cars):
#     current_car = input().split("|")
#
#     car = current_car[0]    # Audi A6
#     distance = int(current_car[1])    # 38000
#     fuel = int(current_car[2])    # 62
#
#     dictionary[car] = [distance, fuel]
#
# while True:
#     command = input()
#
#     if command == "Stop":
#         break
#
#     command_args = command.split(" : ")
#
#     type_of_action = command_args[0]
#     car = command_args[1]
#
#     if type_of_action == "Drive":
#         current_distance = int(command_args[2])
#         needed_fuel = int(command_args[3])
#         if needed_fuel > dictionary[car][1]:
#             print(f"Not enough fuel to make that ride")
#         else:
#             dictionary[car][0] += current_distance
#             dictionary[car][1] -= needed_fuel
#             print(f"{car} driven for {current_distance} kilometers. {needed_fuel} liters of fuel consumed.")
#
#         if dictionary[car][0] >= 100000:
#             print(f"Time to sell the {car}!")
#             del dictionary[car]
#
#     elif type_of_action == "Refuel":
#         added_fuel = int(command_args[2])
#         if dictionary[car][1] + added_fuel <= MAX_FUEL:
#             dictionary[car][1] += added_fuel
#             print(f"{car} refueled with {added_fuel} liters")
#         else:
#             fuel_diff = MAX_FUEL - dictionary[car][1]
#             dictionary[car][1] = MAX_FUEL
#             print(f"{car} refueled with {fuel_diff} liters")
#
#     elif type_of_action == "Revert":
#         kilometers = int(command_args[2])
#         dictionary[car][0] -= kilometers
#         if dictionary[car][0] < 10000:
#             dictionary[car][0] = 10000
#         else:
#             print(f"{car} mileage decreased by {kilometers} kilometers")
#
# # sorted_cars = sorted(cars.items(), key=lambda data: (-data[1][0], data[0]))
#
# # sorted by their mileage in decscending order, then by their name in ascending order
#
# sorted_cars = sorted(dictionary.items(), key=lambda data: (-data[1][0], data[0]))
#
# for car, data in sorted_cars:
#     print(f'{car} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.')
#
# # Variant 4 with no sorting
# number_of_cars = int(input())
#
# dictionary = {}  # {'Audi A6': [38000, 62], 'Mercedes CLS': [11000, 35], 'Volkswagen Passat CC': [45678, 5]}
#
# MAX_FUEL = 75
#
# for _ in range(number_of_cars):
#     current_car = input().split("|")
#
#     car = current_car[0]  # Audi A6
#     distance = int(current_car[1])  # 38000
#     fuel = int(current_car[2])  # 62
#
#     dictionary[car] = [distance, fuel]
#
# while True:
#     command = input()
#
#     if command == "Stop":
#         break
#
#     command_args = command.split(" : ")
#
#     type_of_action = command_args[0]
#     car = command_args[1]
#
#     if type_of_action == "Drive":
#         current_distance = int(command_args[2])
#         needed_fuel = int(command_args[3])
#         if needed_fuel > dictionary[car][1]:
#             print(f"Not enough fuel to make that ride")
#         else:
#             dictionary[car][0] += current_distance
#             dictionary[car][1] -= needed_fuel
#             print(f"{car} driven for {current_distance} kilometers. {needed_fuel} liters of fuel consumed.")
#
#         if dictionary[car][0] >= 100000:
#             print(f"Time to sell the {car}!")
#             del dictionary[car]
#
#     elif type_of_action == "Refuel":
#         added_fuel = int(command_args[2])
#         if dictionary[car][1] + added_fuel <= MAX_FUEL:
#             dictionary[car][1] += added_fuel
#             print(f"{car} refueled with {added_fuel} liters")
#         else:
#             fuel_diff = MAX_FUEL - dictionary[car][1]
#             dictionary[car][1] = MAX_FUEL
#             print(f"{car} refueled with {fuel_diff} liters")
#
#     elif type_of_action == "Revert":
#         kilometers = int(command_args[2])
#         dictionary[car][0] -= kilometers
#         if dictionary[car][0] < 10000:
#             dictionary[car][0] = 10000
#         else:
#             print(f"{car} mileage decreased by {kilometers} kilometers")
#
# for car, data in dictionary.items():
#     print(f'{car} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.')
#
# # Variant 5
# cars_count = int(input())
#
# fuel_by_car = {}
# mileage_by_car = {}
#
# COMMAND_STOP = "Stop"
# COMMAND_DRIVE = "Drive"
# COMMAND_REFUEL = "Refuel"
# COMMAND_REVERT = "Revert"
# MAXIMUM_FUEL = 75
# MAXIMUM_MILEAGE = 100000
# MINIMUM_MILEAGE = 10000
#
# for _ in range(cars_count):
#     car_arguments = input().split("|")
#     car = car_arguments[0]
#     mileage = int(car_arguments[1])
#     fuel = int(car_arguments[2])
#
#     fuel_by_car[car] = fuel
#     mileage_by_car[car] = mileage
#
# while True:
#     line = input()
#
#     if line == COMMAND_STOP:
#         break
#
#     command_args = line.split(" : ")
#
#     command = command_args[0]
#     car = command_args[1]
#
#     if command == COMMAND_DRIVE:
#         distance = int(command_args[2])
#         fuel = int(command_args[3])
#         if fuel > fuel_by_car[car]:
#             print(f"Not enough fuel to make that ride")
#             continue
#         else:
#             fuel_by_car[car] -= fuel
#             mileage_by_car[car] += distance
#             print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
#
#             if mileage_by_car[car] >= MAXIMUM_MILEAGE:
#                 del mileage_by_car[car]  # mileage_by_car.pop(car)
#                 del fuel_by_car[car]  # fuel_by_car.pop(car)
#                 print(f"Time to sell the {car}!")
#
#     elif command == COMMAND_REFUEL:
#         fuel = int(command_args[2])
#         current_fuel = fuel_by_car[car]
#         fuel_by_car[car] = min(fuel_by_car[car] + fuel, MAXIMUM_FUEL)
#         print(f"{car} refueled with {fuel_by_car[car] - current_fuel} liters")
#
#     elif command == COMMAND_REVERT:
#         kilometers = int(command_args[2])
#         updated_mileage = mileage_by_car[car] - kilometers
#         if updated_mileage < MINIMUM_MILEAGE:
#             mileage_by_car[car] = MINIMUM_MILEAGE
#         else:
#             mileage_by_car[car] = updated_mileage
#             print(f"{car} mileage decreased by {kilometers} kilometers")
#
# for car in fuel_by_car.keys():
#     fuel = fuel_by_car[car]
#     mileage = mileage_by_car[car]
#     print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")