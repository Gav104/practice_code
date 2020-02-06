from statistics import mean


def average():
    while True:
        try:
            numbers = list(map(int, input('Enter numbers: ').split()))
        except ValueError:
            print("The input was not a valid integer.")
        else:
            print(mean(numbers))


average()

