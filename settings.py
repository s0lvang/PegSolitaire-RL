actor = dict(
    learningRate=0.5,
    eligibilityDecayRate=0.9,
    discountFactor=0.9,
    epsilon=0.9,
    epsilonDecayRate=0.2,
)

critic = dict(learningRate=0.5, eligibilityDecayRate=0.9, discountFactor=0.9)

game = dict(size=4, boardType="D", state="1010111111101111")

"""
game = dict(
    size = 4
    boardType = "D"
    state = "1111111111101111"
) """
