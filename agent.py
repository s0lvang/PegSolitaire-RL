from actor import Actor
from critic import Critic
from neuralNetCritic import NeuralNetCritic
from config import agent as config
from matplotlib import pyplot as plt
from drawer import Drawer
import numpy as np
from board import Board


class Agent:
    def __init__(self):
        self.actor = Actor()
        self.critic = NeuralNetCritic()
        self.drawer = Drawer()

    def runEpisodes(self, numberOfEpisodes):
        scores = []
        for episodeNumber in range(numberOfEpisodes):
            self.runEpisode(episodeNumber, scores)
        self.displayResults(scores)

    def runEpisode(self, episodeNumber, scores):
        board, state, action, SAPpairs = self.initalizeEpisode()
        while not board.isInEndState():
            newState, reinforcement, score = board.move(action)
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
        scores.append(score)

    def initalizeEpisode(self):
        board = Board(config["size"], config["boardType"], config["state"])
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

    def displayResults(self, scores):
        a = np.convolve(scores, np.ones((100,)) / 100, mode="valid")
        plt.ylim(0, max(a) + 2)
        plt.plot(a)
        plt.show()


agent = Agent()
agent.runEpisodes(config["episodesToRun"])
