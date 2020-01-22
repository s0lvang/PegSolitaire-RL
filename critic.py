from settings import critic as settings
import random


class Critic:
    def __init__(self):
        self.learningRate = settings["learningRate"]
        self.eligibilityDecayRate = settings["eligibilityDecayRate"]
        self.discountFactor = settings["discountFactor"]
        self.eligibilityMap = {}
        self.values = {}

    def getTDError(self, state, newState, reinforcement):
        return (
            reinforcement
            + self.discountFactor * self.values.get(newState, random.uniform(0,1))
            - self.values.get(state, random.uniform(0,1))
        )

    def updateEligibility(self, state, isCurrentState=False):
        if isCurrentState:
            self.eligibilityMap[state] = 1
        else:
            self.eligibilityMap[state] = (
                self.discountFactor
                * self.eligibilityDecayRate
                * self.eligibilityMap.get(state, random.uniform(0,1))
            )

    def updateValueFunction(self, state, TDerror):
        self.values[state] = (
            self.values.get(state, random.uniform(0,1))
            + self.learningRate * TDerror * self.eligibilityMap.get(state, random.uniform(0,1))
        )
