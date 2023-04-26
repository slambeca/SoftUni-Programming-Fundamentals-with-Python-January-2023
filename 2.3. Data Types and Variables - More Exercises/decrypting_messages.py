key = int(input())
number_of_lines = int(input())

for _ in range(number_of_lines):
    current_letter = input()

    decrypted_letter = ord(current_letter) + key

    print(chr(decrypted_letter), end="")