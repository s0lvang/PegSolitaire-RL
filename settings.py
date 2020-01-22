actor = dict(
    learningRate=0.3,
    eligibilityDecayRate=0.8,
    discountFactor=0.8,
    epsilon=1,
    epsilonDecayRate=0.99,
)

critic = dict(learningRate=0.3, eligibilityDecayRate=0.8, discountFactor=0.8)

game = dict(size=5, boardType="D", state="11111111011111111")

"""
game = dict(
    size = 4
    boardType = "D"
    state = "1111111111101111"
) """
