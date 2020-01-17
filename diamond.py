from node import Node
from drawer import Drawer
from direction import Direction


class Diamond:
    board = []

    def __init__(self, size):
        self.board = [[Node(i, j) for j in range(size)] for i in range(size)]
        self.setAllNeigbours(self.board)

    def positionIsOnBoard(self, r, c):
        # This needs to be generalized for boards that are triangular. The two sides are not neccesarily of equal length
        return 0 <= r and len(self.board) > r and 0 <= c and len(self.board) > c

    def allLegalMoves(self):
        legalMoves = []
        for row in board:
            for node in row:
                legalMoves.append(node.legalMoves())
        return legalMoves

    def setAllNeigbours(self, board):
        for row in board:
            for node in row:
                self.setNeighbours(node)

    def setNeighbours(self, node):
        neighbours = {
            Direction.UP: self.upNeighbour(node),
            Direction.UPRIGHT: self.upRightNeighbour(node),
            Direction.RIGHT: self.rightNeighbour(node),
            Direction.DOWN: self.downNeighbour(node),
            Direction.DOWNLEFT: self.downLeftNeighbour(node),
            Direction.LEFT: self.leftNeighbour(node),
        }
        node.setNeighbours(neighbours)
        node.legalMoves()

    def upNeighbour(self, node):
        r = node.coordinates[0]
        c = node.coordinates[1]
        return self.neighbour(r - 1, c)

    def upRightNeighbour(self, node):
        r = node.coordinates[0]
        c = node.coordinates[1]
        return self.neighbour(r - 1, c + 1)

    def rightNeighbour(self, node):
        r = node.coordinates[0]
        c = node.coordinates[1]
        return self.neighbour(r, c + 1)

    def downNeighbour(self, node):
        r = node.coordinates[0]
        c = node.coordinates[1]
        return self.neighbour(r + 1, c)

    def downLeftNeighbour(self, node):
        r = node.coordinates[0]
        c = node.coordinates[1]
        return self.neighbour(r + 1, c - 1)

    def leftNeighbour(self, node):
        r = node.coordinates[0]
        c = node.coordinates[1]
        return self.neighbour(r, c - 1)

    def neighbour(self, r, c):
        if self.positionIsOnBoard(r, c):
            return self.board[r][c]


diamond = Diamond(4)
board = diamond.board
board[0][0].empty = True
board[2][2].empty = True
print(diamond.allLegalMoves())
drawer = Drawer()
drawer.draw(diamond.board)
