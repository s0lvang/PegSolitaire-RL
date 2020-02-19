actor = dict(
    learningRate=0.1,
    eligibilityDecayRate=0.99,
    discountFactor=0.99,
    epsilon=1,
    epsilonDecayRate=0.99,
)

critic = dict(learningRate=0.1, eligibilityDecayRate=0.99, discountFactor=0.99)

neuralNet = dict(
    nodes=[15, 20, 30, 5],
    eligibilityDecayRate=0.99,
    learningRate=0.001,
    discountFactor=0.99,
)

agent = dict(
    boardType="T",
    size=5,
    state="1111110111111111",
    episodesToRun=500,
    critic="table",
    # critic="ann",
    timeBetweenFrames=0.5,
    visualize=True,
    displayResults=True,
)

# boardType="D", size=6, state="1111111111111110111111111111111111111111111"


board = dict(reinforcementOnWin=100, reinforcementOnLoss=-100)
