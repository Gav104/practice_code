import random


def coin_flip():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


heads_tally = 0
tails_tally = 0

for trial in range(100):
    if coin_flip() == "heads":
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1

ratio = heads_tally / tails_tally
ratio2 = tails_tally / heads_tally

print(f"{heads_tally:,.0f} is the heads tally")
print(f"{tails_tally:,.0f}, is the tails tally")

if heads_tally > tails_tally:
    print("Heads came out on top")
else:
    print("Tails came out on top")

print(f"The ratio of heads to tails is {ratio}")
print(f"The ratio of tails to heads is {ratio2}")
