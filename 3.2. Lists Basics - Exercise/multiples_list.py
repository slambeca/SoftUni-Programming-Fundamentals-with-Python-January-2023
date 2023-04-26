factor = int(input())
count = int(input())

my_list = []

for num in range(1, count + 1):
    my_list.append(num * factor)

print(my_list)

# Variant 2
# factor = int(input())    # 2
# count = int(input())    # 5
#
# result = []
#
# for i in range(factor, factor * count + 1, factor):    # the range is from 2, until 10 included, step is 2
#     result.append(i)
#
# print(result)    # [2, 4, 6, 8, 10]