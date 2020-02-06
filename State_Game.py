import random


capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}


def capital_game():
    def try_again():
        choice = input("Would you like to play again? y/n ")
        if choice == "y" or choice == "Y":
            capital_game()
        elif choice == "n" or choice == "N":
            print("Thank for playing")
            quit()
        else:
            print("Try again")
            try_again()

    while True:
        state = random.choice(list(capitals_dict.keys()))
        capital = capitals_dict[state]
        guess = input(f"What is the capital of '{state}'? ").lower()
        if guess == "exit":
            print(f"The capital of '{state}' is '{capital}'.")
            print("Goodbye")
            quit()
        if guess != capital.lower():
            print("    Whoops - Please try again!")
        elif guess == capital.lower():
            print("Correct! Nice job.")
            try_again()


capital_game()


