from board import Board
from drawer import Drawer
from settings import game as settings


class Game:
    def __init__(self):
        self.board = Board(settings["size"], settings["boardType"], settings["state"])
    
    def isEndState(self):
        return self.board.isEndState()


