class Coordinates:
    def __init__(self, r, c):
        self.r = r
        self.c = c
    
    def getCoordinates(): 
        return (r, c)

    def directionToCoordinate(self, r, c):
        return "nope"

    def setCoordinates(self, r, c):
        self.r = r
        self.c = c
        if (r == -1 and c == 0) or (r == -1 and c == 0) or(r == 0 and c == 1) or (r == 1 and c == -1)
            self.direction_string = "UP"
        elif r == -1 and c == 0:
            self.direction_string = "UPRIGHT"
        elif r == 0 and c == 1:
            self.direction_string = "RIGHT"
        elif r == 1 and c == 0:
            self.direction_string = "DOWN"
        elif r == 1 and c == -1:
            self.direction_string = "DOWN_LEFT"
        elif r == 0 and c == -1:
            self.direction_string = "LEFT"
        else:
            raise ValueError("invalid direction")

