from node import Node
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


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
        r = node.r
        c = node.c
        upNeighbour = self.upNeighbour(node)
        if upNeighbour:
            node.setNeighbour(upNeighbour)
        print(node)

    def upNeighbour(self, node):
        if self.positionIsOnBoard(node.r - 1, node.c):
            return self.board[node.r - 1][node.c]

    def getNeighbours(self, node):
        r = node.r
        c = node.c
        neighbours = []
        if self.positionIsOnBoard(r - 1, c):
            neighbours.append(self.board[r - 1][c])
        if self.positionIsOnBoard(r - 1, c + 1):
            neighbours.append(self.board[r - 1][c + 1])
        if self.positionIsOnBoard(r, c + 1):
            neighbours.append(self.board[r][c + 1])
        if self.positionIsOnBoard(r + 1, c):
            neighbours.append(self.board[r + 1][c])
        if self.positionIsOnBoard(r + 1, c - 1):
            neighbours.append(self.board[r + 1][c - 1])
        if self.positionIsOnBoard(r, c - 1):
            neighbours.append(self.board[r][c - 1])
        return neighbours

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
        pos = nx.spring_layout(G, seed=89)
        emptyNodes = list(
            map(lambda node: labels[node], filter(lambda node: node.empty, nodes))
        )
        fullNodes = list(
            map(lambda node: labels[node], filter(lambda node: not node.empty, nodes))
        )

        fig, ax = plt.subplots()
        nx.draw_networkx_nodes(G, ax=ax, pos=pos, nodelist=fullNodes, node_color="b")
        nx.draw_networkx_nodes(G, ax=ax, pos=pos, nodelist=emptyNodes, node_color="r")
        nx.draw_networkx_edges(G, ax=ax, pos=pos)
        ax.invert_yaxis()
        plt.axis("off")
        plt.show()


diamond = Diamond(4)
print(diamond.drawBoard())
