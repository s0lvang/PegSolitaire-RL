from config import critic as config
import random


class Critic:
    def __init__(self):
        self.learningRate = config["learningRate"]
        self.eligibilityDecayRate = config["eligibilityDecayRate"]
        self.discountFactor = config["discountFactor"]
        self.eligibilityMap = {}
        self.values = {}

    def getTDError(self, state, newState, reinforcement):
        rewardAtNewState = self.values.get(newState, 0)
        discountedRewardAtNewState = self.discountFactor * rewardAtNewState
        rewardAtCurrentState = self.values.get(state, 0)

        return reinforcement + discountedRewardAtNewState - rewardAtCurrentState

    def updateEligibility(self, state, isCurrentState=False):
        if isCurrentState:
            newEligibilityOfState = 1
        else:
            eligibilityOfState = self.eligibilityMap.get(state, 1)
            newEligibilityOfState = (
                self.discountFactor * self.eligibilityDecayRate * eligibilityOfState
            )

        self.eligibilityMap[state] = newEligibilityOfState

    def updateValueFunction(self, state, TDerror):
        valueOfState = self.values.get(state, 0)
        eligibilityOfState = self.eligibilityMap.get(state, 1)

        self.values[state] = (
            valueOfState + self.learningRate * TDerror * eligibilityOfState
        )
