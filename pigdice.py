"""
File: pigdice.py

Pops up a window that allows the user to play pig.
"""

import random
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter import messagebox
from die import Die

class PigDice(EasyFrame):
    def __init__(self):
        """Creates the dice, and sets up the Images and labels
        for the two dice to be displayed, the state label,
        and the two command buttons."""
        EasyFrame.__init__(self, title = "Dice Demo", background = "green")
        self.setSize(400, 370)
        self.die1 = Die()
        self.compDie1 = Die()
        self.total = 0
        self.compTotal = 0
        self.dieLabel1 = self.addLabel("", row = 0,
                                       column = 0,
                                       sticky = "NSEW", 
                                       columnspan = 3, 
                                       background = "green", foreground = "white")
        self.stateLabel = self.addLabel("", row = 1, column = 0,
                                        sticky = "NSEW", 
                                        background = "green", foreground = "white")
        self.totalLabel = self.addLabel("", row = 1, column = 1, sticky = "NSEW", 
                                        background = "green", foreground = "white")
        self.compStatus = self.addLabel("", row = 2, column = 0, sticky = "NSEW", 
                                        background = "green", foreground = "white")
        self.compTotalLabel = self.addLabel("", row = 2, column = 1, sticky = "NSEW", 
                                        background = "green", foreground = "white")
        self.rollButt = self.addButton(row = 3, column = 0,
                       text = "Roll",
                       command = self.nextRoll,
                       state = "disabled")
        self.passButt = self.addButton(row = 3, column = 1,
                       text = "Pass turn",
                       command = self.passTurn, 
                       state = "disabled")
        self.addButton(row = 3, column = 2, 
                       text = "New game", 
                       command = self.newGame)
        #figure out how to disable button, then turn them on with line 117
        self.rollButt["state"] = "disabled"
        self.passButt["state"] = "disabled"
        self.refreshImages()

    def nextRoll(self):
        """Rolls the dice and updates the view with
        the results."""
        self.die1.roll()

        self.turnTotal = self.die1.getValue()
        if self.die1.getValue() == 1:
            self.turnTotal = 0
            self.total = 0
            self.rollButt["state"] = "disabled"
            self.passTurn()
        else:
            self.total += self.turnTotal

        self.stateLabel["text"] = "Turn Total = " + str(self.turnTotal)
        self.totalLabel["text"] = "Game Total = " + str(self.total)

        if self.total >= 50:
            answer = messagebox.askyesno("You Win!","Do you want to play again?")
            if answer == 1:
                self.newGame()
            else: 
                self.quit()
        self.refreshImages()

    def passTurn(self):
        self.passButt["state"] = "disabled"
        self.compStatus["text"] = ""
        max = random.randint(1, 50)
        counter = 0
        while counter < max:
            self.compDie1.roll()
    
            self.compTurnTotal = self.compDie1.getValue()
            if self.compDie1.getValue() == 1:
                self.compTurnTotal = 0
                self.compTotal = 0
                self.compStatus["text"] = "The opponent rolled a 1!"
                self.rollButt["state"] = "normal"
                self.passButt["state"] = "normal"
                break
            else:
                self.compTotal += self.compTurnTotal
            if self.compTotal >= 50:
                answer = messagebox.askyesno("You Lost!","Do you want to play again?")
                if answer == 1:
                    self.newGame()
                else: 
                    self.quit()
            counter += 1
        self.compTotalLabel["text"] = "Opponent's Score = " + str(self.compTotal)
        self.rollButt["state"] = "normal"
        self.passButt["state"] = "normal"

    def newGame(self):
        """Create a new craps game and updates the view."""
        self.rollButt["state"] = "normal"
        self.passButt["state"] = "normal"
        self.die1 = Die()
        self.compDie1 = Die()
        self.compStatus["text"] = ""
        self.stateLabel["text"] = ""
        self.totalLabel["text"] = ""
        self.compTotalLabel["text"] = ""
        self.total = 0
        self.compTotal = 0
        self.refreshImages()
        
    def refreshImages(self):
        """Updates the images in the window."""
        fileName1 = "DICE/" + str(self.die1) + ".gif"
        self.image1 = PhotoImage(file = fileName1)
        self.dieLabel1["image"] = self.image1

def main():
    help = messagebox.askyesno("Pig Game","Roll a dice against an opponent. Try to get to a total of 50 before your opponent. But BEWARE, roll a 1 and your score is reset! Would you like to play?")
    if help == 1:
        PigDice().mainloop()
    else:
        quit()

if __name__ == "__main__":
    main()
