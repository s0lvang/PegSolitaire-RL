from board import Board
from drawer import Drawer
from settings import game as settings

class Game:
    def __init__(self):
            self.board = Board(settings["size"], settings["boardType"], settings["state"])

game = Game() 
drawer = Drawer()
drawer.draw(game.board.board)