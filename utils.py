import itertools
from board import Board
import pickle


def generateAllStates(size, boardType="D"):
    if boardType == "D":
        return ["".join(seq) for seq in itertools.product("01", repeat=size * size)]
    else:
        raise NotImplementedError


def generateAllSAP(size, boardType):
    try:
        with open("SAP.pkl", "rb") as picklefile:
            SAP = pickle.load(picklefile)
        with open("states.pkl", "rb") as picklefile:
            states = pickle.load(picklefile)
    except:
        SAP = None
        states = None
    if not (SAP and states):
        SAP = {}
        states = generateAllStates(size, boardType=boardType)
        for state in states:
            board = Board(boardType=boardType, size=size, state=state)
            SAP[state] = {}
            actions = board.allLegalMoves()
            for action in actions + [None]:
                SAP[state][action] = 0
        with open("SAP.pkl", "wb") as picklefile:
            pickle.dump(SAP, picklefile)
        with open("states.pkl", "wb") as picklefile:
            pickle.dump(states, picklefile)

    return states, SAP
