sequence = [int(x) for x in input().split()]  # [10, 20, 30, 40, 50]

sequence.reverse()

average_number = sum(sequence) / len(sequence)  # 30.0

result = []  # top 5 numbers

for x in range(len(sequence)):
    if sequence[x] > average_number:
        result.append(sequence[x])

result.sort(reverse=True)
result = result[:5]    # list slicing to print only the first 5 letters

if len(result) == 0:
    print("No")
else:
    print(*result)

# # Variant 2
#
#
# def top_5(data):
#     avg = sum(data) / len(data)
#
#     temp_sum = [x for x in sorted(data, reverse=True) if x > avg]
#
#     if len(temp_sum) != 0:
#         return ' '.join(map(str, temp_sum[:5]))
#     else:
#         return 'No'
#
#
# numbers = list(map(int, input().split()))
# print(top_5(numbers))
#
# # Variant 3
# integers = list(map(int, input().split()))
#
# average = sum(integers) / len(integers)
#
# top_5 = []
#
# for i in range(len(integers)):
#     if integers[i] > average:
#         top_5.append(integers[i])
#
# top_5.sort(reverse=True)
# top_5 = top_5[:5]
# top_5 = [str(top_5[i]) for i in range(len(top_5))]
#
# if len(top_5) == 0:
#     print("No")
# else:
#     print(" ".join(top_5))
#
# # Variant 4
# initial_array = input().split()
# initial_array = [int(x) for x in initial_array]
#
# avg_array = sum(initial_array) / len(initial_array)
#
# top_five = [a for a in initial_array if a > avg_array]
#
# final_list = []
#
# sorted_top_five = sorted(top_five, reverse=True)
#
# for i in sorted_top_five:
#     final_list.append(i)
#     if len(final_list) == 5:
#         break
#
# if len(final_list) == 0:
#     print("No")
# else:
#     print(' '.join(map(str, final_list)))