count_lines = int(input())

brackets = 0

for _ in range(count_lines):
    current_string = input()

    if current_string == "(":
        brackets += 1

    elif current_string == ")":
        brackets -= 1

    if brackets != 0 and brackets != 1:
        print("UNBALANCED")
        break
else:
    print("BALANCED")