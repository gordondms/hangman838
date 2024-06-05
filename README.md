# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

## Project Title: Hangman

## Table of Contents

## Project Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Installation instructions
Not applicable

## Usage instructions
User guesses the name of a fruit based on a predefined list of fruits
User has 5 attempts

## File structure of the project

milstone_3.py file contains functions to:
- Request user input, user guesses a letter
- Checks if letter is present in the random word

### milstone_4.py file contains functions to:
#### check_guess:
- checks if the guessed letter is present in the word
- if it is present it replaces blanks in word_guessed with the guessed letter and provides user confirmation
- if it is not present it informs the user and reduces their number of lives by 1- 

#### ask_for_input:
- Request user input, user guesses a letter
- Checks validity of user input
- Checks if user has already attempted that letter

### milstone_5.py file contains functions to:
Builds on milestone_4 functions and adds:

#### play_game:
- Coding the logic of the game
- Creates an instance of the Hangman class and assigns it to game variable
- Passes word_list and num_lives as arguments to the game object
- Checks if num_lives counter has reached 0 = end of game (user loses)
- Checks if the num_letters variable is still > 0 = game continues
- Otherwise the user has found the word and has won the game

## License information
Not applicable
