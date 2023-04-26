first = input()
second = input()

result = first

for idx in range(len(first)):
    if first[idx] == second[idx]:    # so that we can print only unique results
        continue

    result = second[:idx + 1] + first[idx + 1:]   # + 1 because we want the index to be included

    print(result)