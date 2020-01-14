class Node:
    def __init__(self, r, c):
        self.empty = False
        self.r = r
        self.c = c
        self.neighbours = {*()}

    def clear(self):
        self.empty = True

    def getNeighbours(self):
        return self.neighbours

    def getNeighbour(self, direction):
        return direction

    def setNeighbours(self, neighbours):
        for neighbour in neighbours:
            self.setNeighbour(neighbour)

    def setNeighbour(self, neighbour):
        if neighbour:
            self.neighbours.add(neighbour)
            return True
        else:
            return False

    def getCoordinates(self):
        return (self.r, self.c)

    def __str__(self):
        if len(self.neighbours) > 0:
            neighbours_representation = [n.getCoordinates() for n in self.neighbours]
        else:
            neighbours_representation = "no neighbours"
        return f"Node: (r{self.r} c{self.c}),  Empty: {self.empty}, Neighbours: {neighbours_representation}"

    def __repr__(self):
        return self.__str__()
