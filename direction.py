from enum import Enum


class Direction(Enum):
    UP = ((-1, 0),)
    UPRIGHT = (-1, 1)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    DOWNLEFT = (1, -1)
    LEFT = (0, -1)


# class Direction:
#     def __init__(self, r, c):
#         try:
#             self.setDirection(r, c)
#         except ValueError as err:
#             print(err.args)

#     def setDirection(self, r, c):
#         self.r = r
#         self.c = c
#         if r == -1 and c == 0:
#             self.direction_string = "UP"
#         elif r == -1 and c == 0:
#             self.direction_string = "UPRIGHT"
#         elif r == 0 and c == 1:
#             self.direction_string = "RIGHT"
#         elif r == 1 and c == 0:
#             self.direction_string = "DOWN"
#         elif r == 1 and c == -1:
#             self.direction_string = "DOWN_LEFT"
#         elif r == 0 and c == -1:
#             self.direction_string = "LEFT"
#         else:
#             raise ValueError("invalid direction")

