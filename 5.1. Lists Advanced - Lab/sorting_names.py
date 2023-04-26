names = input().split(", ")

sorted_names = sorted(names, key=lambda x: (-len(x), x))    # -len(x) descending by the length of the names
# (-len(x), x)) - sort by then by
print(sorted_names)