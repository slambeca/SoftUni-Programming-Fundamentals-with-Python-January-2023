string = input().lower()

counter = 0

counter += string.count("water")
counter += string.count("sand")
counter += string.count("sun")
counter += string.count("fish")

print(counter)