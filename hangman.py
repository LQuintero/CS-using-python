# Hangman game
#

import random
import string

#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    for char in secretWord:
        if not char in lettersGuessed:
            return False
    return True
        
def getGuessedWord(secretWord, lettersGuessed):
    guessedWord = ''
    for char in secretWord:
        if char in lettersGuessed:
            guessedWord = guessedWord + char
        else:
            guessedWord = guessedWord + '_ ' 
    return guessedWord
            
   
def getAvailableLetters(lettersGuessed):
    availLetters = string.ascii_lowercase
    for char in lettersGuessed:
        if char in availLetters:
            availLetters = availLetters.replace(char,'')
    return availLetters
