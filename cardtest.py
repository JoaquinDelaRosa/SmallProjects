import numpy as np
from enum import Enum
import random
import matplotlib.pyplot as plt

PLAYERS = 3
CYCLES = 200

class Cards(Enum):
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Seven = 6
    Eight = 7
    Ten = 8
    Eleven = 9
    Twelve = 10
    Sorry = 11

class Player:
    def __init__(self, id):
        self.id = id
        self.ctrs = [0 for i in range(1, 12)]
    
    def updateCounter(self, card):
        self.ctrs[card.value - 1] += 1

    def printCounter(self):
        print("Player id: " + str(self.id))

        for i in range(1, 12):
            print(Cards(i).name + ": " + str(self.ctrs[i  - 1]))

        print("======================")


def generateShuffledStack():
    cards = []
    for i in range(1, 12):
        for j in range(0, 4):
            cards.append(Cards(i))
    cards.append(Cards(1))

    random.shuffle(cards)

    return cards

def showPlayerPlot(player):
    xpoints = [Cards(i).name for i in range(1, 12)]
    ypoints = player.ctrs
    
    plot = plt.subplot(1, PLAYERS, player.id)
    plt.bar(xpoints, ypoints)


def main():
    cardStack = []
    players = [Player(i + 1) for i in range(0, PLAYERS)]
    
    for c in range(0, CYCLES):
        for p in range(0, PLAYERS):
            if(len(cardStack) == 0):
                cardStack = generateShuffledStack()
            
            cardDrawn = cardStack.pop()
            players[p].updateCounter(cardDrawn)

    for i in range(0, PLAYERS):
        players[i].printCounter()
        showPlayerPlot(players[i])

    plt.show()

main()