from actor import Actor
from critic import Critic
from game import Game
from utils import generateAllSAP
from settings import game as settings
from matplotlib import pyplot as plt
from drawer import Drawer
import numpy as np
from board import Board


class Agent:
    def __init__(self):
        # states, SAP = generateAllSAP(settings["size"], settings["boardType"])
        self.actor = Actor()
        self.critic = Critic()
        self.drawer = Drawer()

    def runEpisodes(self, numberOfEpisodes):
        pegsLeft = []
        for episodeNumber in range(numberOfEpisodes):
            self.runEpisode(episodeNumber, pegsLeft)
        self.displayResults(pegsLeft)

    def takeMove(self, action, board):
        newState, reinforcement = board.move(action)
        return newState, reinforcement

    def initalizeEpisode(self):
        board = Board(settings["size"], settings["boardType"], settings["state"])
        state = board.bitString
        action = None
        SAPpairs = []
        return board, state, action, SAPpairs

    def chooseNextAction(self, board, action, newState):
        legalMoves = board.allLegalMoves()
        if board.isInEndState():
            newAction = action
        else:
            newAction = self.actor.chooseAction(newState, legalMoves)

        return newAction

    def runEpisode(self, episodeNumber, pegsLeft):
        board, state, action, SAPpairs = self.initalizeEpisode()
        while not board.isInEndState():
            newState, reinforcement = self.takeMove(action, board)
            newAction = self.chooseNextAction(board, action, newState)
            self.actor.updateEligibility(newState, newAction, isCurrentState=True)
            TDError = self.critic.getTDError(state, newState, reinforcement)
            self.critic.updateEligibility(newState, isCurrentState=True)

            if action:
                SAPpairs.append((state, action))

            for (s, a) in SAPpairs:
                self.critic.updateValueFunction(s, TDError)
                self.critic.updateEligibility(s)
                self.actor.updatePolicy(s, a, TDError)
                self.actor.updateEligibility(s, a)

            state, action = newState, newAction

        if reinforcement == 3000:
            pegsLeft.append(24)
        else:
            pegsLeft.append(reinforcement)

    def displayResults(self, pegsLeft):
        a = np.convolve(pegsLeft, np.ones((100,)) / 100, mode="valid")
        plt.plot(a)
        plt.show()
        print(pegsLeft)


agent = Agent()
agent.runEpisodes(100)
