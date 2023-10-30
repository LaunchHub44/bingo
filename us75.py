import os
import sys
import random
import time

# Colorama:  Decorating text with ANSI escape sequence.
#    - https://pypi.org/project/colorama/
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

round_interval, print_interval = 1,1
max_bingo = 25

class BingoBoard:
    def __init__(self, playerId = None):
        self.grid = self.setUpBoard()
        self.playerId = playerId
    
    def setUpBoard(self):
        grid = []

        numbers = list(range(1,max_bingo + 1))
        random.shuffle(numbers)
        for r in range(0,5):
            row = []
            for s in range(0,5):
                row.append(numbers.pop())
            grid.append(row)
        return grid
    
    def printBoard(self, called: list):
        for row in self.grid:
            print('[', end='')
            for elm in row:
                if elm in called:
                    print(f"{Fore.RED}{elm:3}{Style.RESET_ALL}", end='')
                else:
                    print(f"{elm:3}", end='')
            print(']')
        print()

    def printBoards(self, called: list, players: list):
        for card in players:
            for row in card.grid:
                print('[', end='')
                for elm in row:
                    if elm in called:
                        print(f"{Fore.RED}{elm:3}{Style.RESET_ALL}", end='')
                    else:
                        print(f"{elm:3}", end='')
                print(']', end='    ')
            print()

    def getRowString(self, called: list[int], rowIdx) -> str:
        """
        It will return self.grid[rowIdx] as a string.
        """
        rtn = []
        for elm in self.grid[rowIdx]:
            if elm in called:
                rtn.append(f"{Fore.RED}{elm:3}{Style.RESET_ALL}")
            else:
                rtn.append(f"{elm:3}")

        #return f"[{' '.join(rtn)}]"
        return '[' + ' '.join(rtn) + ']'

    def checkBingoRow(self, called: list) -> bool:
        for row in self.grid:
            matching = 0
            for elm in row:
                if elm in called:
                    matching += 1
            if matching == 5:
                return True
        return False    # If none of the rows are completely filled.

    def checkBingoCol(self, called: list) -> bool:
        for c in range(0,5):
            matching = 0
            for r in range(0,5):
                if self.grid[r][c] in called:
                    matching += 1
            if matching == 5:
                return True
        return False    # If no columns have been completed.

    def checkBingoDiag(self, called: list) -> bool:
        matching = 0
        for s in range(0,5):
            if self.grid[s][s] in called:
                matching += 1
        if matching == 5:
            return True
        
        matching = 0
        for s in range(0,5):
            if self.grid[s][4-s] in called:
                matching += 1
        if matching == 5:
            return True
        return False

    def checkBingo(self, called: list) -> bool:
        return self.checkBingoRow(called) or \
            self.checkBingoCol(called) or \
            self.checkBingoDiag(called)

if __name__ == '__main__':
    colorama_init()
    player1 = BingoBoard(1)
    player2 = BingoBoard(2)
    player3 = BingoBoard(3)
    players = [ player1, player2, player3 ]


    numbers = list(range(1,max_bingo + 1))
    random.shuffle(numbers)
    called = []
    round = 0

    while round < 19:    # finish at 19th round
        round += 1

        # do something
        current_num = numbers.pop()
        called.append(current_num)
        
        print(f"Round: {round}")
        print(f"Current number: {current_num}")
        print("-----")
        time.sleep(round_interval)

        # check
        if player1.checkBingo(called) or player2.checkBingo(called) or player3.checkBingo(called):
            break
        


        # do other thing
        #player1.printBoard(called)
        #player2.printBoard(called)
        #player3.printBoard(called)
        #player1.printBoards(called, players)

        # Brute Force

        """
        print( player1.getRowString(called, 0) + "  " + player2.getRowString(called, 0) + "  " + player3.getRowString(called, 0))
        print( player1.getRowString(called, 1) + "  " + player2.getRowString(called, 1) + "  " + player3.getRowString(called, 1))
        print( player1.getRowString(called, 2) + "  " + player2.getRowString(called, 2) + "  " + player3.getRowString(called, 2))
        print( player1.getRowString(called, 3) + "  " + player2.getRowString(called, 3) + "  " + player3.getRowString(called, 3))
        print( player1.getRowString(called, 4) + "  " + player2.getRowString(called, 4) + "  " + player3.getRowString(called, 4))        
        """
        
        # Jake's Optimized
        for n in range(0, 5):
            print(player1.getRowString(called, n) + "  " + \
                  player2.getRowString(called, n) + "  " + \
                  player3.getRowString(called, n))

        print("-----")
        time.sleep(print_interval)

    winners = []
    for player in players:
        if player.checkBingo(called):
            winners.append(player)

    for n in range(0, 5):
        print(player1.getRowString(called, n) + "  " + \
              player2.getRowString(called, n) + "  " + \
              player3.getRowString(called, n))

    if len(winners) > 0:
        for winner in winners:
            print(f"Player {winner.playerId} won!")
    else:
        print("Nobody won...")

    """
    if player1.checkBingo(called):
        print(f"BINGO!! Player won!")
    else:
        print(f"Alas.. No bingo.")
    """
