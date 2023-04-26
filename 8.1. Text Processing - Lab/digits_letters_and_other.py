string = input()

digits, letters, other = [], [], []

for symbol in string:
    if symbol.isdigit():
        digits.append(symbol)
    elif symbol.isalpha():
        letters.append(symbol)
    else:
        other.append(symbol)

print(*digits, sep="")
print(*letters, sep="")
print(*other, sep="")