def enrollment_stats(list_of_uni):

    total_students = []
    total_tuition = []

    for uni in list_of_uni:
        total_students.append(uni[1])
        total_tuition.append(uni[2])

    return total_students, total_tuition


def mean(my_list):
    if len(my_list) == 0:
        return "This list is empty"
    list_sum = 0
    for i in range(len(my_list)):
        list_sum += float(my_list[i])
    return float(list_sum / len(my_list))


def median(my_list):
    sorts = sorted(my_list)
    length = len(sorts)
    if not length % 2:
        return (sorts[int(length / 2)] + sorts[int(length / 2 - 1)]) / 2.0
    return sorts[int(length / 2)]


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

bacon = [
    ['California Bacon', 12, 25],
    ['Baconator', 9, 20],
    ['Leaning Tower of Bacon', 10, 15]
]
total = enrollment_stats(bacon)
totals = enrollment_stats(universities)

print("\n")
print("x" * 5)
print(f"Total stripes of bacon:   {sum(total[0])}")
print(f"Total cost of bacon:  $ {sum(total[1])}")
print(f"\nBacon mean:     {mean(total[0]):.2f}")
print(f"Bacon median:   {median(total[0])}")
print(f"\nBacon mean:   $ {mean(total[1])}")
print(f"Bacon median: $ {median(total[1])}")
print("x" * 5)
print("\n")

print("\n")
print("x" * 20)
print(f"Total students:   {sum(totals[0])}")
print(f"Total tuition:  $ {sum(totals[1])}")
print(f"\nStudent mean:     {mean(totals[0]):.2f}")
print(f"Student median:   {median(totals[0])}")
print(f"\nTuition mean:   $ {mean(totals[1]):.2f}")
print(f"Tuition median: $ {median(totals[1])}")
print("x" * 20)
print("\n")
