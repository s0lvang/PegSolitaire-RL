import random
from settings import actor as settings


class Actor:
    def __init__(self, eligibilityMap, policy):
        self.learningRate = settings["learningRate"]
        self.eligibilityDecayRate = settings["eligibilityDecayRate"]
        self.discountFactor = settings["discountFactor"]
        self.epsilon = settings["epsilon"]
        self.epsilonDecayRate = settings["epsilonDecayRate"]
        self.eligibilityMap = eligibilityMap  # (s, a) -> eligibility"]
        self.policy = (
            policy
        )  # (s,a) -> z where z is how desirable the action is in the current state

    def updateEligibility(state, action, isCurrentState):
        if isCurrentState:
            self.eligibilityMap[state, action] = 1
        else:
            self.eligibilityMap[state, action] = (
                self.discountFactor
                * self.eligibilityDecayRate
                * self.eligibilityMap[state, action]
            )

    def chooseAction(self, state):
        probability = random.randint(0, 100) / 100
        self.epsilon = self.epsilon * self.epsilonDecayRate
        if epsilon > probability:
            # choose random
            raise NotImplementedError
        else:
            # choose best
            raise NotImplementedError

        return 0

    def updatePolicy(state, action, TDerror):
        self.policy[state, action] = (
            self.policy[state, action]
            + self.learningRate * TDerror * eligibilityMap[state, action]
        )


# Actor(0,0,0,0,0).chooseAction()
