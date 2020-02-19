actor = dict(
    learningRate=0.1,
    eligibilityDecayRate=0.99,
    discountFactor=0.99,
    epsilon=1,
    epsilonDecayRate=0.99,
)

critic = dict(learningRate=0.1, eligibilityDecayRate=0.99, discountFactor=0.99)

# game = dict(size=6, boardType="D", state="1111111111111110111111111111111111111111111")

game = dict(size=5, boardType="T", state="1111011111111111")
