import networkx as nx
import matplotlib.pyplot as plt


class Drawer:
    def draw(self, board):
        G = nx.Graph()
        labels = {}
        # flatten board
        nodes = [node for sublist in board for node in sublist]
        labels = [node.getCoordinates() for node in nodes]
        G.add_nodes_from(labels)
        for node in nodes:
            for neighbour in node.getNeighbours():
                G.add_edge(node.getCoordinates(), neighbour.getCoordinates())
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

        pos = self.generate_pos(board, fullNodes)
        fig, ax = plt.subplots()
        nx.draw_networkx_nodes(G, ax=ax, pos=pos, nodelist=fullNodes, node_color="b")
        nx.draw_networkx_nodes(G, ax=ax, pos=pos, nodelist=emptyNodes, node_color="r")
        nx.draw_networkx_edges(G, ax=ax, pos=pos)
        nx.draw_networkx_labels(G, ax=ax, pos=pos)
        ax.invert_yaxis()
        plt.axis("off")
        plt.show()

    def generate_pos(self, board, fullNodes):
        pos = {}
        for i in range(len(board)):
            for j in range(len(board)):
                pos[board[i][j].getCoordinates()] = [
                    300 + i * -30 + j * 30,
                    30 * i + 30 * j,
                ]
        return pos

