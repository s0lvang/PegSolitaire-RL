actor = dict(
    learningRate=0.9,
    eligibilityDecayRate=0.9,
    discountFactor=0.9,
    epsilon=0.9,
    epsilonDecayRate=0.04,
)

critic = dict(learningRate=0.9, eligibilityDecayRate=0.9, discountFactor=0.9)

game = dict(size=5, boardType="D", state="11111111011111111")

"""
game = dict(
    size = 4
    boardType = "D"
    state = "1111111111101111"
) """
