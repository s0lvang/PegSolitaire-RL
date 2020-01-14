from peg_node import peg_node
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import time


class Diamond:
    board = []

    def __init__(self, size):
        self.board = [[peg_node(j, i) for j in range(size)] for i in range(size)]

    def isIndex(self, x, y):
        return 0 <= x and len(self.board) > x and 0 <= y and len(self.board) > y

    def getNeighbours(self, peg_node):
        y = peg_node.x
        x = peg_node.y
        neighbours = []
        if self.isIndex(x - 1, y):
            neighbours.append(self.board[x - 1][y])
        if self.isIndex(x - 1, y + 1):
            neighbours.append(self.board[x - 1][y + 1])
        if self.isIndex(x, y + 1):
            neighbours.append(self.board[x][y + 1])
        if self.isIndex(x + 1, y):
            neighbours.append(self.board[x + 1][y])
        if self.isIndex(x + 1, y - 1):
            neighbours.append(self.board[x + 1][y - 1])
        if self.isIndex(x, y - 1):
            neighbours.append(self.board[x][y - 1])
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
