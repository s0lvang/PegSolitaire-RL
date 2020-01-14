from node import Node


class Diamond:
    board = []

    def __init__(self, size):
        self.board = [[Node(i, j) for j in range(size)] for i in range(size)]

        self.setAllNeigbours(self.board)

    def positionIsOnBoard(self, r, c):
        # This needs to be generalized for boards that are triangular. The two sides are not neccesarily of equal length
        return 0 <= r and len(self.board) >= r and 0 <= c and len(self.board) >= c

    def setAllNeigbours(self, board):
        for row in board:
            for node in row:
                self.setNeighbours(node)

    def setNeighbours(self, node):
        r = node.r
        c = node.c
        upNeighbour = self.upNeighbour(node)
        if upNeighbour:
            node.setNeighbour(upNeighbour)
        print(node)

    def upNeighbour(self, node):
        if self.positionIsOnBoard(node.r - 1, node.c):
            return self.board[node.r - 1][node.c]

    # def getNeighbours(self, node):
    #     r = node.r
    #     c = node.c
    #     neighbours = []
    #     if self.isIndex(r - 1, c):
    #         neighbours.append(self.board[r - 1][c])
    #     if self.isIndex(r - 1, c + 1):
    #         neighbours.append(self.board[r - 1][c + 1])
    #     if self.isIndex(r, c + 1):
    #         neighbours.append(self.board[r][c + 1])
    #     if self.isIndex(r + 1, c):
    #         neighbours.append(self.board[r + 1][c])
    #     if self.isIndex(r + 1, c - 1):
    #         neighbours.append(self.board[r + 1][c - 1])
    #     if self.isIndex(r, c - 1):
    #         neighbours.append(self.board[r][c - 1])
    #     return neighbours


Diamond(4)
