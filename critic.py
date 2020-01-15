class Critic():

    def __init__(
            self,
            learningRate,
            eligibilityDecayRate,
            discountFactor,
            epsilon,
            epsilonDecayRate,
        ):
            self.learningRate = learningRate
            self.eligibilityDecayRate = eligibilityDecayRate
            self.discountFactor = discountFactor
            self.epsilon = epsilon
            self.epsilonDecayRate = epsilonDecayRate
            self.eligibilityMap = {} #map on state action pairs
            self.values = {}
    
