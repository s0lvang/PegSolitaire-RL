import networkx as nx
import matplotlib.pyplot as plt


class Drawer:
    def draw(self, board):
        G = nx.Graph()
        labels = {}
        nodes = [node for sublist in board for node in sublist]
        labels = [node.coordinates for node in nodes]
        G.add_nodes_from(labels)
        for node in nodes:
            for neighbour in node.neighbours.values():
                if neighbour:
                    G.add_edge(node.coordinates, neighbour.coordinates)
        emptyNodes = list(
            map(lambda node: node.coordinates, filter(lambda node: node.empty, nodes))
        )
        fullNodes = list(
            map(
                lambda node: node.coordinates,
                filter(lambda node: not node.empty, nodes),
            )
        )

        pos = self.generate_pos(board, fullNodes)
        fig, ax = plt.subplots()
        nx.draw_networkx_nodes(G, ax=ax, pos=pos, nodelist=fullNodes, node_color="gray")
        nx.draw_networkx_nodes(G, ax=ax, pos=pos, nodelist=emptyNodes, node_color="r")
        nx.draw_networkx_edges(G, ax=ax, pos=pos)
        nx.draw_networkx_labels(G, ax=ax, pos=pos, font_color="blue")
        ax.invert_yaxis()
        plt.axis("off")
        plt.show()

    def generate_pos(self, board, fullNodes):
        pos = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                pos[board[i][j].coordinates] = [300 + i * -30 + j * 30, 30 * i + 30 * j]
        return pos
