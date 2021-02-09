import random
import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.impute import SimpleImputer
import os
import math
import numpy as np
import time

# Change direct to program's folder
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Reads the CSV
df = pandas.read_csv("ticWins.csv")
# Main Features to look for
features = ['Row11', 'Row12', 'Row13', 'Row21', 'Row22', 'Row23', 'Row31', 'Row32', 'Row33']
# Set features to find
X = df[features]
# Get whether or not to attend
y = df['Win']
# Create decision tree
dtree = DecisionTreeClassifier().fit(X, y)


class TicTacToe(object):
    def __init__(self, plyr):
        self.board = [3,3,3,3,3,3,3,3,3]
        self.loc = 0
        self.turnCnt = 0
        self.plyr = plyr
    
    def flipPlayers(self):
            if self.plyr == 0:
                self.plyr = 1
            else:
                self.plyr = 0

    def show(self):
        print("[{}][{}][{}]\n[{}][{}][{}]\n[{}][{}][{}]\n".format(self.board[0], self.board[1], self.board[2], self.board[3], self.board[4], self.board[5], self.board[6], self.board[7], self.board[8]))

    def run(self):
        if self.turnCnt <= 8:
            run = True
            while run:
                self.loc = int(input("Playerc{} - Pick location of piece: 1-9: ".format(self.plyr)))
                # self.loc = random.randint(1, 9)
                if self.board[self.loc - 1] == 3:
                    print("Player {} picked a location: {}".format(self.plyr, self.loc))
                    self.board[self.loc - 1] = self.plyr
                    self.show()
                    time.sleep(1)
                    self.flipPlayers()
                    self.turnCnt += 1
                    run = False
                else:
                    print("{} is not a valid option".format(self.loc))
        elif self.turnCnt >= 8:
            if dtree.predict([self.board]) == 1:
                print("Player 1 Wins")
                quit()
            elif dtree.predict([self.board]) == 0:
                print("Player 0 Wins")
                quit()
            else:
                print("Tie")
                quit()


plyr = random.randint(0, 1)
ru = TicTacToe(plyr)

while True:
    ru.run()