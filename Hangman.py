from turtle import *

class Hangman:
    def __init__(self):
        self.t = Turtle()
        
    def start(self): #draws scaffold
        self.t.hideturtle()
        self.t.pensize(4)
        self.t.fd(80)
        self.t.up()
        self.t.goto(40, 0)
        self.t.down()
        self.t.left(90)
        self.t.fd(170)
        self.t.right(90)
        self.t.fd(50)
        self.t.right(90)
        self.t.fd(30)
        self.t.right(90)
   
    def draw(self, numTries):
        if numTries == 6: #draws head
            self.t.circle(15) 
        elif numTries == 5: #draws torso
            self.t.left(90)
            self.t.up()
            self.t.goto(90, 110)
            self.t.down()
            self.t.fd(50)
        elif numTries == 4: #draws leg
            self.t.left(45)
            self.t.fd(27)
        elif numTries == 3: #draws leg
            self.t.backward(27)
            self.t.right(90)
            self.t.fd(27)
        elif numTries == 2: #draws arm
            self.t.up()
            self.t.goto(90, 110)
            self.t.down()
            self.t.fd(27)
        elif numTries == 1: #draws arm
            self.t.backward(27)
            self.t.right(-90)
            self.t.fd(27)

    def erase(self):
            self.t.reset()
            


