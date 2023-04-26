class Zoo:
    __animals = 0    # total count of the animals

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for i in range(count):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))

# Variant 2 with access to a private class attribute
#
#
# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == "mammal":
#             self.mammals.append(name)
#         elif species == "fish":
#             self.fishes.append(name)
#         elif species == "bird":
#             self.birds.append(name)
#
#         Zoo._Zoo__animals += 1
#
#     def get_info(self, species):
#         if species == "mammal":
#             return f"Mammals in {self.name}: {', '.join(self.mammals)}"
#         elif species == "fish":
#             return f"Fishes in {self.name}: {', '.join(self.fishes)}"
#         elif species == "bird":
#             return f"Birds in {self.name}: {', '.join(self.birds)}"
#
#
# name = input()
# rows = int(input())
#
# zoo = Zoo(name)
#
# for _ in range(rows):
#     species, animal = input().split()
#
#     zoo.add_animal(species, animal)
#
# species = input()
#
# print(zoo.get_info(species))
# print(f"Total animals: {Zoo._Zoo__animals}")