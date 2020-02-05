import random


def coin_flip():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


heads_tally = 0
tails_tally = 0

flips = int(input("How many times do you want to flip the coin?: "))


for trial in range(flips):
    if coin_flip() == "heads":
        heads_tally = heads_tally + 1

    else:
        tails_tally = tails_tally + 1
print("-")
print(f"Number of times tails was landed: {tails_tally}")
print(f"Number of times heads was landed: {heads_tally}")
