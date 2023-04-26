version = [int(num) for num in input().split(".")]

if version[-1] != 9:
    version[-1] += 1
else:
    version[-1] = 0

if version[-1] == 0:
    if version[1] != 9:
        version[1] += 1
    else:
        version[1] = 0

if version[1] == 0 and version[-1] == 0:
    if version[0] != 9:
        version[0] += 1

new_version = [str(char) for char in version]

print(*new_version, sep=".")

# Variant 2
# version = [int(number) for number in input().split(".")]
#
# version[-1] += 1
#
# for index in range(len(version) - 1, -1, -1):
#     if version[index] > 9:
#         version[index] = 0
#         if index - 1 >= 0:    # so that we don`t get IndexError
#             version[index - 1] += 1
#
# print(".".join(str(number) for number in version))
#
# # Variant 3
# new_versions = str(int("".join(input().split("."))) + 1)
# print(f"{new_versions[0]}.{new_versions[1]}.{new_versions[2]}")
#
# # Variant 4
# version = input().split('.')
# number = int(version[0] + version[1] + version[2]) + 1
# new_version = str(number)
# print(".".join(new_version))
#
# # Variant 5
# major, minor, patch = [int(x) for x in input().split(".")]
#
# patch += 1
#
# if patch == 10:
#     patch = 0
#     minor += 1
#
#     if minor == 10:
#         minor = 0
#         major += 1
#
# print(f"{major}.{minor}.{patch}")