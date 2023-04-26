fire_cells = input().split("#")    # ['High = 89', 'Low = 28', 'Medium = 77', 'Low = 23']
initial_water = int(input())

total_fire = 0

processed_cells = []

for fire in fire_cells:
    fire_args = fire.split(" = ")

    type_of_fire = fire_args[0]
    fire_value = int(fire_args[1])

    if type_of_fire == "High" and (fire_value < 81 or fire_value > 125):
        continue

    if type_of_fire == "Medium" and (fire_value < 51 or fire_value > 80):
        continue

    if type_of_fire == "Low" and (fire_value < 1 or fire_value > 50):
        continue

    if initial_water < fire_value:
        continue

    initial_water -= fire_value
    total_fire += fire_value
    processed_cells.append(fire_value)

total_effort = total_fire * 0.25

print("Cells:")

for value in processed_cells:
    print(f"- {value}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")