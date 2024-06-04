import random

# Define word list
word_list = ["Apple", "Banana", "Strawberry", "Melon", "Kiwi"]

# Select a random word
word = str.lower(random.choice(word_list))

# Define variables

word_guessed = ["_"] * len(word)
num_letters = len(set(word))
list_of_guesses = []

# Print variables for code testing only
print(word)
print(num_letters)

class Hangman:

    # class constructor
    def __init__(self, word_list, num_lives=5):
        self.word = word
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = list_of_guesses

    # Method1: Checks if the users guess is a letter within the random word
    def check_guess(self, guess):
        """Converts guessed letter to lower case"""
        guess = str.lower(guess)
        """
        If guess is correct user gets confimation and the blank spaces in word_guessed are populated with the correct letter
        If guess in not correct the num_lives variable is reduced by 1 and the user is informed the guess was not correct and how many lives they have left
        """
        if guess in word:
            print("Good guess!", guess, "is in the word.")
            for index, letter in enumerate(word):
                if letter == guess:
                    word_guessed[index] = guess
                    print(word_guessed)
        else:
            self.num_lives -= 1
            print("Sorry!", guess, "is not in the word.")
            print("You have", self.num_lives, "lives left.")
    num_letters -= 1
    print(num_letters)    
    
    # Method2: Request user input, user guesses a letter
    #          Checks validity of user input
    #          Checks if user has already attempted that letter
    def ask_for_input(self):
        while True:
            """User inputs a letter and this is stored in the guess variable"""
            guess = input("Please enter a letter: ")
            """
            Checks validity of letter inputted
            Checks if letter has previously been inputted
            Updates list_of_guesses variable to show all user guesses so far and references the check_guess method
            """
            if (len(guess) != 1) or (str.isalpha(guess) == False):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print("You already tried that letter!")
            else:
                list_of_guesses.append(guess) 
                self.check_guess(guess)


hangman = Hangman(word_list)
hangman.ask_for_input()
