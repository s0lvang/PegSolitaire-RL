from diamond import Diamond


class Game:
    def __init__(self, size, boardType="D"):
        if boardType == "D":
            self.board = Diamond(size)

