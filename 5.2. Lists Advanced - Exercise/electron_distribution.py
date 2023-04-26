# 44
# [] -> 0 + 1
# 1 -> 2 * 1 ^ 2 = 2 [2] (42)
# 2 -> 2 * 2 ^ 2 = 8 [2, 8] (34)
# 3 -> 2 * 3 ^ 2 = 18 [2, 8, 18] (16)
# 4 -> 2 * 4 ^ 2 = 32 [2, 8, 18, 16] (0)

electrons = int(input())

result = []

while electrons > 0:
    n = len(result) + 1    # we start from 1, since the initial len(result) is 0
    shell_value = min(2 * (n ** 2), electrons)
    result.append(shell_value)
    electrons -= shell_value

print(result)