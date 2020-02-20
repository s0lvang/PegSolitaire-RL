actor = dict(
    learningRate=0.1,
    eligibilityDecayRate=0.99,
    discountFactor=0.99,
    epsilon=1,
    epsilonDecayRate=0.99,
)

critic = dict(learningRate=0.1, eligibilityDecayRate=0.99, discountFactor=0.99)

neuralNet = dict(
    nodes=[16, 10],
    eligibilityDecayRate=0.99,
    learningRate=0.00001,
    discountFactor=0.99,
)

agent = dict(
    boardType="D",
    size=4,
    state="1111110111111111",
    episodesToRun=300,
    critic="ann",
    # critic="table",
    timeBetweenFrames=0.5,
    visualize=False,
    displayResults=False,
)

# T 5 ann=500e table=1000e 15 nodes
# boardType="T",
# size=5,
# state="111111011111111",

# D 4 table=500e 16 nodes
# boardType="D",
# size=4,
# state="1111110111111111",


# boardType="D", size=6, state="1111111111111110111111111111111111111111111"


board = dict(reinforcementOnWin=100, reinforcementOnLoss=-100)
