class Critic:
    def __init__(self, learningRate, eligibilityDecayRate, discountFactor):
        self.learningRate = learningRate
        self.eligibilityDecayRate = eligibilityDecayRate
        self.discountFactor = discountFactor
        self.eligibilityMap = {}  # map on state action pairs
        self.values = {}

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
