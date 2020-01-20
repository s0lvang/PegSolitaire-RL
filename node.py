from direction import Direction


class Node:
    def __init__(self, r, c):
        self.empty = False
        self.coordinates = (r, c)
        self.neighbours = {
            Direction.UP: None,
            Direction.UPRIGHT: None,
            Direction.RIGHT: None,
            Direction.DOWN: None,
            Direction.DOWNLEFT: None,
            Direction.LEFT: None,
        }

    def move(self, direction):
        if self.moveIsLegal(direction):
            direct_neighbour = self.neighbours[direction]
            jump_target = direct_neighbour.neighbours[direction]

            self.empty = True
            direct_neighbour.empty = True
            jump_target.empty = False
        else:
            return False

    def moveIsLegal(self, direction):
        direct_neighbour = self.neighbours[direction]
        if direct_neighbour and not direct_neighbour.empty and not self.empty:
            jump_target = direct_neighbour.neighbours[direction]
            if jump_target and jump_target.empty:
                return True
        return False

    def legalMoves(self):
        return [
            (self.coordinates, direction)
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

    def __str__(self):
        neighbours_representation = [
            n.coordinates
            for n in filter(lambda neighbour: neighbour, self.neighbours.values())
        ]
        return f"Node: ({self.coordinates}),  Empty: {self.empty}, Neighbours: {neighbours_representation}"

    def __repr__(self):
        return self.__str__()
