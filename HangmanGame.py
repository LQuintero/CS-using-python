# 
# Hangman game
#

# -----------------------------------


import random
import string

WORDLIST_FILENAME = "H:/repos/CS-using-python/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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

def hangman(secretWord):  
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guessesLeft = 8
    lettersGuessed = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord))
    + ' letters long.')
    while guessesLeft > 0:
        print('-------------')
        print('You have ' + str(guessesLeft) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        newLetter = raw_input('Please guess a letter: ').strip().lower()
        if newLetter in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else: 
            lettersGuessed.append(newLetter)
            if newLetter in secretWord:
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed):
                    print('-------------')
                    print('Congratulations, you won!')
                    break
            else:
                guessesLeft -= 1
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                if guessesLeft == 0:
                    print('-------------')
                    print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
                    break
    
