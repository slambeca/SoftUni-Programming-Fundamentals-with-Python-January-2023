count_lines = int(input())

for _ in range(count_lines):    # 2
    sentences = input()    # Here is a name @George| and an age #18*

    name_start_index = sentences.rfind("@")    # returns the last occurrence of the searched symbol
    name_end_index = sentences.index("|")    # returns the first occurrence of the searched symbol
    age_start_index = sentences.rfind("#")
    age_end_index = sentences.index("*")

    name = sentences[name_start_index + 1: name_end_index]
    age = sentences[age_start_index + 1: age_end_index]

    print(f"{name} is {age} years old.")