from peg_node import peg_node
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class Diamond():
    board = []

    def __init__(self, size):
        self.board = [[peg_node(j, i) for j in range(size)]
                      for i in range(size)]

    def isIndex(self, x, y):
        return (0 <= x and len(self.board) > x and
                0 <= y and len(self.board) > y)

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
        print(len(neighbours))
        return neighbours

    ''' def getLegalMoves(self, peg_node):
        if(peg_node.empty):
            return []
        legalMoves = []
        neighbours = list(filter(lambda x: not x.empty), self.getNeighbours())
        for neighbour in neighbours:
            delta_x = peg_node.x - neighbour.x
            delta_y = peg_node.y - neighbour.y
            if(isIndex(delta_x*2, delta_y*2) and board[2*delta_x][2*delta_y].empty):
                legalMoves.append(2*delta_x, 2*delta_y)
 '''

    def drawBoard(self):
        G = nx.Graph()
        labels = {}
        # flatten board
        nodes = [node for sublist in self.board for node in sublist]
        for i in range(len(nodes)):
            labels[nodes[i]] = i
        G.add_nodes_from(labels.values())
        for node in nodes:
            for neighbour in self.getNeighbours(node):
                G.add_edge(labels[node], labels[neighbour])
        #nx.draw_networkx(G, pos=nx.planar_layout(G), with_labels=False)
        nx.draw_networkx(G)
        plt.show()


diamond = Diamond(4)
print(diamond.drawBoard())
