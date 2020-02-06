def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return input


x = int(input("How many times do you want to flip the coin?: "))
print(fizz_buzz(x))
