import random

word_list = ["Apple", "Banana", "Strawberry", "Melon", "Kiwi"]

word = random.choice(word_list)

word_guessed = ["_"] * len(word)

guess = "e"

print(word_guessed)

for index, letter in enumerate("test"):
    if letter == guess:
        word_guessed[index] = guess 
        print(index)
        print(letter)
        print(word_guessed)