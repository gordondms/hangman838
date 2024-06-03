import random

# Define word list
word_list=["Apple", "Banana", "Strawberry", "Melon", "Kiwi"]
print(word_list)

# Select a random word
word = random.choice(word_list)
print(word)

# User input - guess a letter
guess = input("Please enter a letter: ")
if (len(guess) == 1) and (str.isalpha(guess) == True):
    print("Good guess!")
else:
    print("Oops! That is not a valid input")
   
