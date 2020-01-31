import random
from settings import actor as settings


class Actor:
    def __init__(self):
        self.learningRate = settings["learningRate"]
        self.eligibilityDecayRate = settings["eligibilityDecayRate"]
        self.discountFactor = settings["discountFactor"]
        self.epsilon = settings["epsilon"]
        self.epsilonDecayRate = settings["epsilonDecayRate"]
        self.eligibilityMap = {}
        self.policy = (
            {}
        )  # (s,a) -> z where z is how desirable the action is in the current state

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
        randomNumber = random.uniform(0, 1)
        self.epsilon = self.epsilon * self.epsilonDecayRate
        if self.epsilon > randomNumber:
            return random.choice(legalMoves)
        else:
            policyWithRandomActions = {
                action: random.uniform(0, 1) for action in legalMoves
            }
            policyForState = self.policy.get(state, policyWithRandomActions)
            self.policy[state] = policyForState
            return max(self.policy[state], key=self.policy[state].get)

    def updatePolicy(self, state, action, TDerror):
        randomNumber = random.uniform(0, 1)
        currentPolicyForState = self.policy.get(state, {})
        actionInCurrentPolicy = currentPolicyForState.get(action, randomNumber)
        eligibilityForState = self.eligibilityMap.get(state, {}).get(
            action, randomNumber
        )
        newAction = (
            actionInCurrentPolicy + self.learningRate * TDerror * eligibilityForState
        )
        self.policy.get(state, {})[action] = newAction
