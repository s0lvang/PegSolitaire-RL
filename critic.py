from settings import critic as settings


class Critic:
    def __init__(
        self, eligibilityMap, values
    ):
        self.learningRate = settings["learningRate"]
        self.eligibilityDecayRate = settings["eligibilityDecayRate"]
        self.discountFactor = settings["discountFactor"]
        self.eligibilityMap = eligibilityMap
        self.values = values

    def getTDError(self, state, newState, reinforcement):
        return (
            reinforcement + discountFactor * self.values[newState] - self.values[state]
        )

    def updateEligibility(self, state, isCurrentState):
        if isCurrentState:
            self.eligibilityMap[state] = 1
        else:
            self.eligibilityMap[state] = (
                self.discountFactor
                * self.eligibilityDecayRate
                * self.eligibilityMap[state]
            )

    def updateValueFunction(self, state, TDerror):
        self.values[state] = (
            self.values[state]
            + self.learningRate * TDerror * self.eligibilityMap[state]
        )
