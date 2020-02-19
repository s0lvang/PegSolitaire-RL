import random
from config import actor as config


class Actor:
    def __init__(self):
        self.learningRate = config["learningRate"]
        self.eligibilityDecayRate = config["eligibilityDecayRate"]
        self.discountFactor = config["discountFactor"]
        self.epsilon = config["epsilon"]
        self.epsilonDecayRate = config["epsilonDecayRate"]
        self.eligibilityMap = {}
        self.policy = {}

    def updateEligibility(self, state, action, isCurrentState=False):
        if isCurrentState:
            self.eligibilityMap.get(state, {})[action] = 1
        else:
            eligibilityOfState = self.eligibilityMap.get(state, {}).get(
                action, random.uniform(0, 1)
            )
            self.eligibilityMap.get(state, {})[action] = (
                self.discountFactor * self.eligibilityDecayRate * eligibilityOfState
            )

    def chooseAction(self, state, legalMoves):
        self.epsilon = self.epsilon * self.epsilonDecayRate
        if self.epsilon > random.uniform(0, 1):
            return random.choice(legalMoves)
        else:
            initialStatePolicy = {action: random.uniform(0, 1) for action in legalMoves}
            policyForState = self.policy.get(state, initialStatePolicy)
            self.policy[state] = policyForState
            return max(policyForState, key=policyForState.get)

    def updatePolicy(self, state, action, TDerror):
        currentValuesForState = self.policy.get(state, {})
        valueForAction = currentValuesForState.get(action, random.uniform(0, 1))
        eligibilityForSAP = self.eligibilityMap.get(state, {}).get(
            action, random.uniform(0, 1)
        )
        newValueForAction = (
            valueForAction + self.learningRate * TDerror * eligibilityForSAP
        )
        self.policy.get(state, {})[action] = newValueForAction
