# Filter only the valid locations
import re

points = 0
destinations = []

data = input()    # =Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=

# Valid locations are surrounded by / or = on both sides (we use group for that case)
# First letter should be uppercase, next letter could be either upper or lowercase
# The letters must be at least three
pattern = r"(=|\/)[A-Z][A-Za-z]{2,}\1"

result = re.finditer(pattern, data)    # finditer, because we will be working with groups

for destination in result:
    current_destination = re.split("\/|=", destination.group())[1]
    points += len(current_destination)
    destinations.append(current_destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")

# # Variant 2
# import re
#
# world_places = input()
#
# pattern = r'(=|\/)([A-Z][A-Za-z]{2,})\1'
# matches = re.finditer(pattern, world_places)
# destination = []
# travel_points = 0
#
# for match in matches:
#     destination.append(match.group(2))
#     travel_points += len(match.group(2))
#
# print(f"Destinations: {', '.join(destination)}")
# print(f'Travel Points: {travel_points}')
#
# # Variant 3
# import re
#
# destinations = input()
#
# travel_points = 0
#
# pattern = r"(?<=(?P<lb>[=/]))(?P<match>[A-Z]{1}[A-Za-z]{2,})(?=(?P=lb))"
#
# valid_locations = re.finditer(pattern, destinations)
#
# valid_destinations = [location.group() for location in valid_locations]
#
# print(f"Destinations: {', '.join(valid_destinations)}")
#
# for el in valid_destinations:
#     travel_points += len(el)
#
# print(f"Travel Points: {travel_points}")