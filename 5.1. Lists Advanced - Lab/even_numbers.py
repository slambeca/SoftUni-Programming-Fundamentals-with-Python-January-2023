nums = [int(el) for el in input().split(", ") if int(el) % 2 == 0]

print(nums)

# print([int(el) for el in input().split(", ") if int(el) % 2 == 0])
# this variant is not recommended

# Variant 2
# nums = list(map(int, input().split(", ")))
#
# print(list(filter(lambda x: x % 2 == 0, nums)))
#
# # Variant 3
# print([index for index in range(len(nums)) if nums[index] % 2 == 0])
#
# # Variant 4
# print(list(map(lambda x: nums.index(x), list(filter(lambda x: x % 2 == 0, nums)))))