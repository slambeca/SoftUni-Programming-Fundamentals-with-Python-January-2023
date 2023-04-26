sequence = [int(x) for x in input().split()]    # distances to the pokemons

result = []

while sequence:
    index = int(input())    # 1 - they correspond to the sequence

    if index < 0:
        value_of_removed_element = sequence.pop(0)
        last_element = sequence[-1]
        sequence.insert(0, last_element)
    elif index > len(sequence) - 1:    # if it`s greater than the last index of the sequence
        value_of_removed_element = sequence.pop()
        sequence.append(sequence[0])
    else:
        value_of_removed_element = sequence.pop(index)

    result.append(value_of_removed_element)

    for item in range(len(sequence)):
        if sequence[item] <= value_of_removed_element:
            sequence[item] += value_of_removed_element
        elif sequence[item] > value_of_removed_element:
            sequence[item] -= value_of_removed_element

print(sum(result))