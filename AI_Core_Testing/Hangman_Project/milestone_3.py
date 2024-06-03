# Create loop for user to guess a letter and validate that this is a singe alpha character

random_word = str.lower("Apple")

# Check if letter is in random word

def check_guess(guess):
    guess = str.lower(guess)
    if guess in random_word:
      print("Good guess!", guess, "is in the word.")
    else:
      print("Sorry,", guess, "is not in the word. Try again.")

# Requests user input. User needs to guess a letter

def ask_for_input():
    while True:
        guess = input("Please enter a letter: ")
        if (len(guess) == 1) and (str.isalpha(guess) == True):
            print("Good guess!")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()
