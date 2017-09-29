
handle = open("Hangman.py")
from random import *
from Hangman import *

seed()

def letterInWord(x, y):  
    indexes = []
    for i in range(len(y)):
        if x == y[i]:
            indexes.append(i)       
    return indexes
    

class Game():
    def __init__(self):
        self.listing = []
        self.secretWord = ""
        self.Underscore = []
        self.hidden = []
        self.c = Hangman()
        self.c.start()
        self.userPick = ['1','2','3','4']
        self.userPick = input("Please type a number from the word bank themes:\n (1) animals \n (2) clothes\n (3) transportation\n (4) veggies\n   Enter here: ")
        while self.userPick not in ['1','2','3','4']:
            self.userPick = input("Please enter number between 1 and 4: ")
        print("Let the game begin!")
                
            
    def chooseWord(self):
         handle = 0
         self.listing = []
         self.Underscore = []
         self.hidden = []
         if self.userPick == '1':
             handle = open ("animals.txt")
         elif self.userPick == '2':
             handle = open("clothes.txt")
         elif self.userPick == '3':
             handle = open("transportation.txt")
         else:
             handle = open("veggies.txt")
         for line in handle:
            self.listing.append(line.rstrip())
         handle.close()
         num = randint(0, len(self.listing)-1)  
         self.secretWord = self.listing[num] 

    def printGuess(self): 
        hiddenString = "__ " * len(self.secretWord)
        self.Underscore = hiddenString.split() 
        self.hidden.extend(self.secretWord) 
   
    def playGame(self):    
        print(self.Underscore)
        numTries = 6
        lettersUsed = []
        while numTries > 0:
            letter = input("Please guess a letter: ")
            if letter not in lettersUsed:
                lettersUsed.append(letter)
            if letter in self.secretWord:
                index = letterInWord(letter, self.hidden) 
                for i in index:
                    self.Underscore[i] = letter
                print(self.Underscore)
                if self.Underscore == self.hidden:
                    print ("You won! Congratulations!")               
                    break                   
            else:
                numTries -= 1 
                self.c.draw(numTries+1)
            print("\n")
            print("You have ", numTries, "tries left. ")
            print("You have used: ", lettersUsed)
            print(self.Underscore)
        print(self.secretWord)
        print("\n")
               
    def playLoop(self):
        userInput = "y"
        while userInput == "y":
            self.chooseWord()
            self.printGuess()
            self.playGame()
            userInput = input("Would you like to play again? Type 'y' or 'n': ")
            if userInput == "y":
                self.c.erase()
                self.c.start()
        print("Thank you for playing. Come back soon!")
        
        

#driver:
g = Game()
g.playLoop()


