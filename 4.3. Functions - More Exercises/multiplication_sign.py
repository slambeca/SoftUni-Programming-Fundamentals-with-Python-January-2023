def check_multiplication(num1, num2, num3):
    if num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"
    elif (num1 > 0 and num2 > 0 and num3 > 0) or \
            (num1 > 0 and num2 < 0 and num3 < 0) or \
            (num2 > 0 and num1 < 0 and num3 < 0) or \
            (num3 > 0 and num1 < 0 and num2 < 0):
        return "positive"
    elif num1 < 0 or num2 < 0 or num3 < 0:
        return "negative"


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(check_multiplication(number_1, number_2, number_3))