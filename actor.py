class Actor:
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
        self.eligibilityMap = {} # (s, a) -> eligibility
        self.policy = {} # (s,a) -> z where z is how desirable the action is in the current state
        

