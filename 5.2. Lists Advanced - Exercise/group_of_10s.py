numbers = [int(i) for i in input().split(", ")]

groups = 0

while numbers:
    groups += 10
    print_list = [i for i in numbers if i <= groups]
    numbers = [i for i in numbers if i > groups]
    print(f"Group of {groups}'s: {print_list}")