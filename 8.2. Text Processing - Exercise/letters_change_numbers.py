data = input().split()  # ['A12b', 's17G']

alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']

total_sum = 0

for current_string in data:
    current_number = int(current_string[1:len(current_string) - 1])
    if current_string[0].isupper():
        total_sum += current_number / (alphabet_upper.index(current_string[0]) + 1)
    elif current_string[0].islower():
        total_sum += current_number * (alphabet_lower.index(current_string[0]) + 1)

    if current_string[-1].isupper():
        total_sum -= (alphabet_upper.index(current_string[-1]) + 1)
    elif current_string[-1].islower():
        total_sum += (alphabet_lower.index(current_string[-1]) + 1)

print(f"{total_sum:.2f}")