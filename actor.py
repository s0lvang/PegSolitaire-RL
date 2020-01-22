import random
from settings import actor as settings


class Actor:
    def __init__(self):
        self.learningRate = settings["learningRate"]
        self.eligibilityDecayRate = settings["eligibilityDecayRate"]
        self.discountFactor = settings["discountFactor"]
        self.epsilon = settings["epsilon"]
        self.epsilonDecayRate = settings["epsilonDecayRate"]
        self.eligibilityMap ={} 
        self.policy = {} # (s,a) -> z where z is how desirable the action is in the current state

    def updateEligibility(self, state, action, isCurrentState=False):
        if isCurrentState:
            self.eligibilityMap.get(state, {})[action] = 1
        else:
            self.eligibilityMap.get(state,{})[action] = (
                self.discountFactor
                * self.eligibilityDecayRate
                * self.eligibilityMap.get(state, {}).get(action, random.uniform(0,1))
            )

    def chooseAction(self, state, legalMoves):
        probability = random.randint(0, 100) / 100
        self.epsilon = self.epsilon * self.epsilonDecayRate
        if self.epsilon > probability:
            return random.choice(legalMoves)
        else:
            self.policy[state] = self.policy.get(state, {action: random.uniform(0,1) for action in legalMoves})
            return max(self.policy[state], key=self.policy[state].get)

    def updatePolicy(self, state, action, TDerror):
        self.policy.get(state, {})[action] = (
            self.policy.get(state, {}).get(action, random.uniform(0,1))
            + self.learningRate * TDerror * self.eligibilityMap.get(state, {}).get(action, random.uniform(0,1))
        )
