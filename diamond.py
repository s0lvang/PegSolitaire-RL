from node import Node
from drawer import Drawer


class Diamond:
    board = []

    def __init__(self, size):
        self.board = [[Node(i, j) for j in range(size)] for i in range(size)]
        self.setAllNeigbours(self.board)

    def positionIsOnBoard(self, r, c):
        # This needs to be generalized for boards that are triangular. The two sides are not neccesarily of equal length
        return 0 <= r and len(self.board) > r and 0 <= c and len(self.board) > c

    def setAllNeigbours(self, board):
        for row in board:
            for node in row:
                self.setNeighbours(node)

    def setNeighbours(self, node):
        neighbours = {
            "UP": self.upNeighbour(node),
            "UPRIGHT": self.upRightNeighbour(node),
            "RIGHT": self.rightNeighbour(node),
            "DOWN": self.downNeighbour(node),
            "DOWNLEFT": self.downLeftNeighbour(node),
            "LEFT": self.leftNeighbour(node),
        }
        node.setNeighbours(neighbours)

    def upNeighbour(self, node):
        return self.neighbour(node.r - 1, node.c)

    def upRightNeighbour(self, node):
        return self.neighbour(node.r - 1, node.c + 1)

    def rightNeighbour(self, node):
        return self.neighbour(node.r, node.c + 1)

    def downNeighbour(self, node):
        return self.neighbour(node.r + 1, node.c)

    def downLeftNeighbour(self, node):
        return self.neighbour(node.r + 1, node.c - 1)

    def leftNeighbour(self, node):
        return self.neighbour(node.r, node.c - 1)

    def neighbour(self, r, c):
        if self.positionIsOnBoard(r, c):
            return self.board[r][c]


diamond = Diamond(4)
drawer = Drawer()
drawer.draw(diamond.board)
