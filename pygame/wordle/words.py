from settings import *
from random import randint
import copy

class Words:
    def __init__(self):
        with open(GuessFile, 'r') as file:
            self.words = {line.strip().upper() for line in file}
        self.word = self.get_random_word()
        #print(self.word)

    def get_random_word(self) -> str:
        with open(WordFile, 'r') as file:
            temp = [line.strip().upper() for line in file]
        return temp[randint(0,len(temp)-1)]

    def isValidWord(self, guess: [str]) -> bool:
        return "".join(guess) in self.words

    def evaluateGuess(self, guess: str) -> [int]:
        """
        Evaluates guess:  returns 5-element list
        0 = invalid Letter
        1 = right letter, wrong place
        2 = right letter, right place
        returns true if all 5 letters are right letter, right place
        """
        evaluation = [0] * 5
        # copy guess and hidden word to a list
        guess = [guess[i] for i in range(5)]
        word = [self.word[i] for i in range(5)]

        # look for correct letter in the correct position
        for i in range(5):
            if guess[i] == word[i]:
                evaluation[i] = 2
                guess[i] = ' '
                word[i] = ' '
        
        # look for correct letter in the incorrect position
        for i in range(5):
            if guess[i] != ' ' and guess[i] in word:
                pos = word.index(guess[i])
                if pos != -1:
                    evaluation[i] = 1
                    guess[i] = ' '
                    word[pos]  = ' '
        return evaluation

        
