sequence = [int(x) for x in input().split()]    # targets and their values [24, 50, 36, 70]

count_shot_targets = 0

while True:
    command = input()    # indices (indexes) of the target to be shot

    if command == "End":
        break

    index = int(command)

    if 0 <= index < len(sequence):
        value = sequence[index]
        if sequence[index] != -1:
            sequence[index] = -1
            count_shot_targets += 1

            for list_value in range(len(sequence)):
                if sequence[list_value] != -1:
                    if sequence[list_value] > value:
                        sequence[list_value] -= value
                    elif sequence[list_value] <= value:
                        sequence[list_value] += value

print(f"Shot targets: {count_shot_targets} ->", *sequence)

# Variant 2
# targets = [int(target) for target in input().split()]
#
# while True:
#     command = input()
#
#     if command == 'End':
#         break
#
#     target_index = int(command)
#
#     if target_index in range(len(targets)):
#         current_target = targets[target_index]
#         targets[target_index] = -1
#
#         for target in range(len(targets)):
#             if targets[target] != -1:
#                 if targets[target] > current_target:
#                     targets[target] -= current_target
#                 else:
#                     targets[target] += current_target
#
# print(f"Shot targets: {targets.count(-1)} -> {' '.join(str(target) for target in targets)}")