from board import Board
from drawer import Drawer


class Game:
    def __init__(self, size, boardType="D"):
        if boardType == "D":
            self.board = Board(size, boardType="D", state="1111111111101111")
        elif boardType=="T":
            self.board = Board(size=size, boardType="T", state="1111011111" )

game = Game(4, boardType="D")
drawer = Drawer()
drawer.draw(game.board.board)