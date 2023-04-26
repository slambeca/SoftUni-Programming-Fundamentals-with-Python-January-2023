n = int(input())
word = input()

all_strings = []
filtered_strings = []

for _ in range(n):
    current_string = input()

    all_strings.append(current_string)

    if word in current_string:
        filtered_strings.append(current_string)

print(all_strings)
print(filtered_strings)