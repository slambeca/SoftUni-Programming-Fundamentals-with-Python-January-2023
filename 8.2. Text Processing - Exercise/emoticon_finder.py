single_string = input()

for index in range(len(single_string)):
    if single_string[index] == ":":    # and index != len(single_string) - 1
        # to check if the index is not the last one so that we do not get the IndexError
        print(f":{single_string[index + 1]}")