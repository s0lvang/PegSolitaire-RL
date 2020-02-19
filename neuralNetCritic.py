from config import critic as config
import random
from neuralNet import NeuralNet


class NeuralNetCritic:
    def __init__(self):
        self.learningRate = config["learningRate"]
        self.eligibilityDecayRate = config["eligibilityDecayRate"]
        self.discountFactor = config["discountFactor"]
        self.net = NeuralNet(nodes=[15, 10])

    def getTDError(self, state, newState, reinforcement):
        return self.net.criterion(state, newState, reinforcement)

    def updateEligibility(self, state, isCurrentState=False):
        return True

    def updateValueFunction(self, state, TDError):
        self.net.train(state, TDError)
