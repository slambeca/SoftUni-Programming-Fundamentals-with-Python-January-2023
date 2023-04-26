tank_capacity = 255

number = int(input())

total_liters_poured = 0

for _ in range(number):
    liters_poured = int(input())

    if tank_capacity < liters_poured:
        print(f"Insufficient capacity!")
        continue
    else:
        total_liters_poured += liters_poured
        tank_capacity -= liters_poured

print(total_liters_poured)
