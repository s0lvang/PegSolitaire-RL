from peg_node import peg_node
from diamond import Diamond


class peg_solitaire():

    def __init__(self, size, boardType="D"):
        if(boardType == "D"):
            self.board = Diamond(size)

    def get_legal_moves():
