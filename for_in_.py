def add_underscores(word):
    new_word = "_"
    for char in word:
        new_word = new_word + char + "_"
    return new_word


phrase = input("What is your word? ")

print(add_underscores(phrase))
