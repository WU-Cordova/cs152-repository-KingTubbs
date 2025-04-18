from grid import Grid
from gamecontroller import GameController
from cell import Cell
import random

def main():
    grid = Grid(20,20)
    game = GameController(grid)
    game.run()

if __name__ == '__main__':
    main()
