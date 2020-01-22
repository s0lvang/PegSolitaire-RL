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
        # the board represented in a bitstring maybe initalize as None
        action = None  # No action should be done initially.
        SAPpairs = []
        return board, state, action, SAPpairs

    def chooseNextAction(self, board, action, newState):
        legalMoves = board.allLegalMoves()
        if board.isInEndState():
            newAction = action
        else:
            newAction = self.actor.chooseAction(
                newState, legalMoves
            )  # The article about reinforcement learning, just states that the actor chooses an action, but i think it should know which actions are legal.

        return newAction

    def runEpisode(self, episodeNumber, pegsLeft):
        # Initialize s and a
        board, state, action, SAPpairs = self.initalizeEpisode()
        while not board.isInEndState():
            # Do action a from state s moving system to newState and receiving reinforcement r.
            newState, reinforcement = self.takeMove(action, board)
            newAction = self.chooseNextAction(board, action, newState)
            self.actor.updateEligibility(
                newState, newAction, isCurrentState=True
            )  # This should update the eligibility of the SAP to 1, but that will be handled in the function
            TDError = self.critic.getTDError(state, newState, reinforcement)
            self.critic.updateEligibility(
                newState, isCurrentState=True
            )  # Should be updated to 1
            if action:
                SAPpairs.append((state, action))

            for SAP in SAPpairs:
                s, a = SAP
                self.critic.updateValueFunction(
                    s, TDError
                )  # updates the entry for s in the valuefunction
                self.critic.updateEligibility(s)  # should be Y * gamma * e(s)
                self.actor.updatePolicy(
                    s, a, TDError
                )  # update the entry for the sap in the actor
                self.actor.updateEligibility(
                    s, a
                )  # update the eligibility y * gamma * e(s,a)
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
