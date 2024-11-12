# Elijah Edwards
# CIS256 Fall 2024
# EX_4

# This file contains unit testing for the guess_the_word file.
# Note, when using pytest for the test cases, -s must be used due to the input

from guess_the_word import guess_word, word_bank, guess, attempts

def test_select():
    assert guess_word in word_bank

def test_good_guess():
    if guess in guess_word:
        assert guess in guess_word

def test_bad_guess():
    if guess not in guess_word:
        assert guess not in guess_word