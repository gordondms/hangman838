import random

# Define word list
word_list = ["Apple", "Banana", "Strawberry", "Melon", "Kiwi"]

# Select a random word
word = random.choice(word_list)

# Define variables

word_guessed = []
num_letters = []
list_of_guesses = []

class Hangman:

    # class constructor
    def __init__(self, word_list, num_lives=5):
        self.word = word
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = list_of_guesses

    # Method1: 
    def check_guess(self, guess):
        guess = str.lower(guess)
        if guess in word:
            print("Good guess!", guess, "is in the word.")
        # elif:
            # print("Sorry,", guess, "is not in the word. Try again.")


    # Method2: 
    def ask_for_input(self):
        while True:
            guess = input("Please enter a letter: ")
            if (len(guess) != 1) or (str.isalpha(guess) == False):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print("You already tried that letter!")
            else:
                list_of_guesses.append(guess) 
                self.check_guess(guess)

hangman = Hangman(word_list)
hangman.ask_for_input()
