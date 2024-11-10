# Elijah Edwards
# CIS256 Fall 2024
# EX_4

# This program simulates  a simple guess-the-word game using the console. A word from the word bank is chosen at random and the user
# must attempt to guess the word one character at a time. If the character is in the word, the character is revealed in the word. 
# If the guesses all of the characters, they win. If the user makes too many mistakes, they lose and have the word revealed to them. 

import random

# This word bank is where the random choices come from.
word_bank = ['python', 'programming', 'software', 'test', 'student', 'master']

# Chooses a word at random from the word bank 
guess_word = random.choice(word_bank)

print("Guess the characters in the word. Good Luck!")

# The number of attempts is initally ten
guesses = ''
attempts = 10


# This while loop handles the main logic of the game so long as attempts remains above 0
while attempts > 0:

    # Hides the characters of the word to be guessed initally
    hidden = 0

    for char in guess_word:
        
        # Reveals correctly guessed characters in the word
        if char in guesses:
            print(char, end = "\n")

        # Hides character that are not yet guessed
        else:
            print("_")
            hidden += 1

    # The victory condition, if all characters have been guessed, the player wins.
    if hidden == 0:
        print("Congrats! You Win!")
        print("The word is: ", guess_word)
        break

    print()
    guess = input("Guess a character: ")

    guesses += guess

    # Handles incorrect inputs
    if guess not in guess_word:

        # Subtracts an attempt every time the guess is incorrect.
        attempts -= 1
        print("Incorrect. You have", + attempts, "guesses left.")

        # The defeat condition, if all attempts are used, the game ends and the word is revealed.
        if attempts == 0:
            print("Sorry, but you lose. The word was: ", guess_word)
