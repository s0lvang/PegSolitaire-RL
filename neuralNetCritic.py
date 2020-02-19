from settings import critic as settings
import random
from neuralNet import NeuralNet


class NeuralNetCritic:
    def __init__(self):
        self.learningRate = settings["learningRate"]
        self.eligibilityDecayRate = settings["eligibilityDecayRate"]
        self.discountFactor = settings["discountFactor"]
        self.net = NeuralNet(nodes=[15, 10])

    def getTDError(self, state, newState, reinforcement):
        return self.net.criterion(state, newState, reinforcement)

    def updateEligibility(self, state, isCurrentState=False):
        return True

    def updateValueFunction(self, state, TDError):
        self.net.train(state, TDError)
