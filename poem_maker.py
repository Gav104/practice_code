from random import choice


def random_words():
    nouns1 = choice(nouns)
    nouns2 = choice(nouns)
    nouns3 = choice(nouns)
    while nouns1 == nouns2:
        nouns2 = choice(nouns)
    while nouns1 == nouns3 or nouns2 == nouns3:
        nouns3 = choice(nouns)

    v1 = choice(verbs)
    v2 = choice(verbs)
    v3 = choice(verbs)
    while v1 == v2:
        v2 = choice(verbs)
    while v1 == v3 or v2 == v3:
        v3 = choice(verbs)

    adj1 = choice(adjectives)
    adj2 = choice(adjectives)
    adj3 = choice(adjectives)
    while adj1 == adj2:
        adj2 = choice(adjectives)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = choice(adjectives)

    prep1 = choice(prepositions)
    prep2 = choice(prepositions)
    while prep1 == prep2:
        prep2 = choice(prepositions)

    adv1 = choice(adverbs)

    if adj1[0] in vowels:
        article = "An"
    else:
        article = "A"

    poem = f"{article} {adj1} {nouns1}\n\n"
    poem = poem + f"{article} {adj1} {nouns1} {v1} {prep1} the {adj2} {nouns2}\n"
    poem = poem + f"{adv1}, the {nouns1} {v2}\n"
    poem = poem + f"the {nouns2} {v3} {prep2} a {adj3} {nouns3}"

    return poem


vowels = [
    'a', 'e', 'i', 'o', 'u'
]

nouns = [
    'fossil', 'horse', 'aardvark', 'judge', 'chef', 'mango',
    'extrovert', 'gorilla'
]

verbs = [
    'kicks', 'jingles', 'bounces', 'slurps', 'meows',
    'explodes', 'curdles'
]

adjectives = [
    'furry', 'balding', 'incredulous', 'fragrant', 'exuberant', 'glistening'
]

prepositions = [
    'against', 'after', 'into', 'beneath', 'upon',
    'for', 'in', 'like', 'over', 'within'
]

adverbs = [
    'curiously', 'extravagantly', 'tantalizingly', 'furiously', 'sensuously'
]


print(random_words())
