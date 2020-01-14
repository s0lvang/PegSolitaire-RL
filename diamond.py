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
        neighbours = [
            self.upNeighbour(node),
            self.upRightNeighbour(node),
            self.rightNeighbour(node),
            self.downNeighbour(node),
            self.downLeftNeighbour(node),
            self.leftNeighbour(node),
        ]
        node.setNeighbours(neighbours)
        print(node)

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

    def drawBoard(self):
        G = nx.Graph()
        labels = {}
        # flatten board
        nodes = [node for sublist in self.board for node in sublist]
        labels = [node.getCoordinates() for node in nodes]
        # for i in range(len(nodes)):
        #     labels[nodes[i]] = i
        G.add_nodes_from(labels)
        for node in nodes:
            for neighbour in node.getNeighbours():
                G.add_edge(node.getCoordinates(), neighbour.getCoordinates())
        pos = nx.spring_layout(G, seed=89)
        emptyNodes = list(
            map(
                lambda node: node.getCoordinates(),
                filter(lambda node: node.empty, nodes),
            )
        )
        fullNodes = list(
            map(
                lambda node: node.getCoordinates(),
                filter(lambda node: not node.empty, nodes),
            )
        )

        fig, ax = plt.subplots()
        nx.draw_networkx_nodes(G, ax=ax, pos=pos, nodelist=fullNodes, node_color="b")
        nx.draw_networkx_nodes(G, ax=ax, pos=pos, nodelist=emptyNodes, node_color="r")
        nx.draw_networkx_edges(G, ax=ax, pos=pos)
        nx.draw_networkx_labels(G, ax=ax, pos=pos)
        ax.invert_yaxis()
        plt.axis("off")
        plt.show()


diamond = Diamond(4)
print(diamond.drawBoard())
