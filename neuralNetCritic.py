from config import neuralNet as config
import random
from neuralNet import NeuralNet


class NeuralNetCritic:
    def __init__(self):
        self.net = NeuralNet(nodes=config["nodes"])

    def getTDError(self, state, newState, reinforcement):
        return self.net.criterion(state, newState, reinforcement)

    def updateEligibility(self, state, isCurrentState=False):
        return True

    def updateValueFunction(self, state, TDError):
        self.net.train(state, TDError)
