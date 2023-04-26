# number to be checked for prime
# one is not a prime number

number = int(input())    # 7

if number > 1:    # True
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            print("False")
            break
    else:
        print("True")

else:
    print("False")