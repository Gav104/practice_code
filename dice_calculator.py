import random


rolled = []

freq = int(input('How many times would you like to roll the dice? '))


def roll():
    rand = random.randrange(1, 7)
    return rand


for i in range(1, freq + 1):
    number = roll()
    rolled.append(number)
    print(rolled)
count = [rolled.count(1), rolled.count(2), rolled.count(3), rolled.count(4), rolled.count(5), rolled.count(6)]


print(count)
print(f"After being rolled {freq:,.0f} times: ")
print(f"1 was rolled {rolled.count(1):,.0f} times")
print(f"2 was rolled {rolled.count(2):,.0f} times")
print(f"3 was rolled {rolled.count(3):,.0f} times")
print(f"4 was rolled {rolled.count(4):,.0f} times")
print(f"5 was rolled {rolled.count(5):,.0f} times")
print(f"6 was rolled {rolled.count(6):,.0f} times")




