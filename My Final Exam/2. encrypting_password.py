import re

pattern = r"(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^\<\>]{3})<(\1)"

for _ in range(int(input())):
    password = input()

    result = re.match(pattern, password)

    if not result:
        print("Try another password!")
    else:
        print(f"Password: {result[2] + result[3] + result[4] + result[5]}")