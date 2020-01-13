from peg_node import peg_node
import math


class Diamond():
    board = []

    def __init__(self, size):
        self.board = [[peg_node() for j in range(size)] for i in range(size)]

    def isIndex(self, x, y):
        return (0 <= x and len(self.board) >= x and
                0 <= y and len(self.board) >= y)


    def getNeighbours(self, peg_node):
        x = peg_node.x
        y = peg_node.y
        neighbours = []
        if(self.isIndex(x-1, y)):
            neighbours.append(self.board[x-1][y])
        if(self.isIndex(x-1, y+1)):
            neighbours.append(self.board[x-1][y+1])
        if(self.isIndex(x, y+1)):
            neighbours.append(self.board[x][y+1])
        if(self.isIndex(x+1, y)):
            neighbours.append(self.board[x+1][y])
        if(self.isIndex(x+1, y-1)):
            neighbours.append(self.board[x+1][y-1])
        if(self.isIndex(x, y-1)):
            neighbours.append(self.board[x][y-1])
        return neighbours

    def getLegalMoves(self, peg_node):
        if(peg_node.empty):
            return []
        legalMoves = []
        neighbours = list(filter(lambda x: not x.empty), self.getNeighbours())
        for neighbour in neighbours:
            delta_x = peg_node.x - neighbour.x
            delta_y = peg_node.y - neighbour.y
            adjacentX = 
            if(isIndex(delta_x*2, delta_y*2) and board[2*delta_x][2*delta_y].empty):
                legalMoves.append(2*delta_x, 2*delta_y)
