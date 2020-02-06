num = int(input("What number do you want to find integers for? "))
for divide in range(1, num + 1):
    if num % divide == 0:
        print(divide, "is a divisor of", num)
