def tribonacci(num):
    tribonacci_list = [1, 1]
    for number in range(1, num + 1):
        if number == 1 or number == 2:
            print(tribonacci_list[number - 1], end=" ")
            continue
        else:
            last_number = 0
            if len(tribonacci_list) > 2:
                last_number = tribonacci_list.pop(0)
        print(sum(tribonacci_list) + last_number, end=" ")
        tribonacci_list.append(sum(tribonacci_list) + last_number)


input_number = int(input())
tribonacci(input_number)