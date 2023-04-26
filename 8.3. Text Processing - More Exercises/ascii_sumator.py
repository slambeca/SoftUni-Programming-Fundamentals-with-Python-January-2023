first_character = input()    # ?
last_character = input()    # E

string = input()    # @ABCEF

total_sum = 0

for letter in range(len(string)):
    if ord(first_character) < ord(string[letter]) < ord(last_character):
        total_sum += ord(string[letter])

print(total_sum)