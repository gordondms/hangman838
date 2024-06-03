import random

# Define word list
word_list=["Apple", "Banana", "Strawberry", "Melon", "Kiwi"]
print(word_list)

# Select a random word
random_word = random.choice(word_list)
print(random_word)

# User input - guess a letter
user_guess = input("Please enter a letter: ")
if (len(user_guess) == 1) and (str.isalpha(user_guess) == True):
    print("Good guess!")
else:
    print("Oops! That is not a valid input")
   
