countries = input().split(", ")
capitals = input().split(", ")

dictionary = {}    # {'Bulgaria': 'Sofia', 'Romania': 'Bucharest', 'Germany': 'Berlin', 'England': 'London'}

for i in range(len(countries)):
    dictionary[countries[i]] = capitals[i]

for key, value in dictionary.items():
    print(f"{key} -> {value}")

# Variant 2 with dictionary comprehension
# countries = input().split(", ")
# capitals = input().split(", ")
#
# dictionary = {countries[i]: capitals[i] for i in range(len(countries))}
#
# for key, value in dictionary.items():
#     print(f"{key} -> {value}")
#
# # Variant 3 with zip() and dict()
# countries = input().split(", ")
# capitals = input().split(", ")
#
# dictionary = dict(zip(countries, capitals))  # zip without dict() returns a zip object
#
# for key, value in dictionary.items():
#     print(f"{key} -> {value}")