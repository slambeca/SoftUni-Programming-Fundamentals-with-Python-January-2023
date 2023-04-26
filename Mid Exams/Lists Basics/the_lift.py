people = int(input())  # 15
lift = [int(x) for x in input().split()]  # [0, 0, 0, 0]

for wagon in range(len(lift)):  # 0 1 2 3
    if people >= 4:
        if lift[wagon] == 0:
            lift[wagon] += 4
            people -= 4
        else:
            people -= 4 - lift[wagon]
            lift[wagon] += 4 - lift[wagon]

    else:
        lift[wagon] += people
        people = 0

count_free_places = 0

for element in lift:
    if element < 4:
        count_free_places += 1

if not people and count_free_places:
    print(f"The lift has empty spots!")
    print(*lift)
elif people and not count_free_places:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*lift)
elif not people and not count_free_places:
    print(*lift)