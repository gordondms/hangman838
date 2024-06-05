import random

class Hangman:

    # class constructor
    def __init__(self, word_list, num_lives=5):
        self.word = str.lower(random.choice(word_list))
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    # Method1: Checks if the users guess is a letter within the random word
    def check_guess(self, guess):
        """Converts guessed letter to lower case"""
        guess = str.lower(guess)
        """
        If guess is correct user gets confimation and the blank spaces in word_guessed are populated with the correct letter
        If guess in not correct the num_lives variable is reduced by 1 and the user is informed the guess was not correct and how many lives they have left
        """
        if guess in self.word:
            print("Good guess!", guess, "is in the word.")
            
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
                    print(self.word_guessed)

            self.num_letters -= 1
            print("num_letters =", self.num_letters)

        else:
            self.num_lives -= 1
            print("Sorry!", guess, "is not in the word.")
            print("You have", self.num_lives, "lives left.")
         
    
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
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                print(self.list_of_guesses)
                self.check_guess(guess)
            

def play_game(word_list):
    """

    """
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            print(game.num_letters)
            game.ask_for_input()
        else:
            print("Congratulations. You won the game")
            break

if __name__ == '__main__':
    # Define word list
    word_list = ["Apple", "Banana", "Strawberry", "Melon", "Kiwi"]

    play_game(word_list)
