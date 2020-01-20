import random
from settings import actor as settings


class Actor:
    def __init__(self, SAP):
        self.learningRate = settings["learningRate"]
        self.eligibilityDecayRate = settings["eligibilityDecayRate"]
        self.discountFactor = settings["discountFactor"]
        self.epsilon = settings["epsilon"]
        self.epsilonDecayRate = settings["epsilonDecayRate"]
        self.eligibilityMap = {
            state: {action: 1 for action in SAP[state].keys()} for state in SAP.keys()
        }  # (s, a) -> eligibility"]
        self.policy = (
            SAP
        )  # (s,a) -> z where z is how desirable the action is in the current state

    def updateEligibility(self, state, action, isCurrentState=False):
        if isCurrentState:
            self.eligibilityMap[state][action] = 1
        else:
            self.eligibilityMap[state][action] = (
                self.discountFactor
                * self.eligibilityDecayRate
                * self.eligibilityMap[state][action]
            )

    def chooseAction(self, state):
        probability = random.randint(0, 100) / 100
        self.epsilon = self.epsilon * self.epsilonDecayRate
        if self.epsilon > probability:
            return random.choice(list(self.policy[state].keys()))
        else:
            return max(self.policy[state], key=self.policy[state].get)

    def updatePolicy(self, state, action, TDerror):
        self.policy[state][action] = (
            self.policy[state][action]
            + self.learningRate * TDerror * self.eligibilityMap[state][action]
        )

