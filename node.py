from direction import Direction


class Node:
    def __init__(self, r, c):
        self.empty = False
        self.r = r
        self.c = c
        self.neighbours = {
            Direction.UP: None,
            Direction.UPRIGHT: None,
            Direction.RIGHT: None,
            Direction.DOWN: None,
            Direction.DOWNLEFT: None,
            Direction.LEFT: None,
        }

    def clear(self):
        self.empty = True

    def getNeighbours(self):
        return self.neighbours

    def moveIsLegal(self, direction):
        direct_neighbour = self.neighbours[direction]
        if direct_neighbour and not direct_neighbour.empty:
            jump_target = direct_neighbour.neighbours[direction]
            if jump_target and jump_target.empty:
                return True
        return False

    def legalMoves(self):
        return [
            direction
            for direction in filter(
                lambda direction: self.moveIsLegal(direction), self.neighbours.keys()
            )
        ]

    def setNeighbours(self, neighbours):
        for direction in neighbours:
            self.setNeighbour(direction, neighbours[direction])

    def setNeighbour(self, direction, neighbour):
        if neighbour:
            self.neighbours[direction] = neighbour
            return True
        else:
            return False

    def getCoordinates(self):
        return (self.r, self.c)

    def __str__(self):
        neighbours_representation = [
            n.getCoordinates()
            for n in filter(lambda neighbour: neighbour, self.neighbours.values())
        ]
        return f"Node: ({self.r}, {self.c}),  Empty: {self.empty}, Neighbours: {neighbours_representation}"

    def __repr__(self):
        return self.__str__()
