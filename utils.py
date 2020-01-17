import itertools
from board import Board

def generateAllStates(size, boardType="D"):
    if boardType=="D":
        return ["".join(seq) for seq in itertools.product("01", repeat=size*size)]
    else:
        raise NotImplementedError

def generateAllSAP(size, boardType):
    SAP = {}
    states = generateAllStates(size, boardType=boardType)
    for state in states:
        board = Board(boardType=boardType, size=size, state=state)
        SAP[state] = {}
        actions = board.allLegalMoves()
        for action in actions:
            SAP[state][action] = 0
    return states, SAP
