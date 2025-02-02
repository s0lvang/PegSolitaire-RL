from actor import Actor
from critic import Critic as TableCritic
from neuralNetCritic import NeuralNetCritic
from config import agent as config
from matplotlib import pyplot as plt
from drawer import Drawer
from board import Board


class Agent:
    def __init__(self):
        if config["critic"] == "ann":
            self.critic = NeuralNetCritic()
        elif config["critic"] == "table":
            self.critic = TableCritic()
        self.actor = Actor()
        self.drawer = Drawer()

    def runEpisodes(self, numberOfEpisodes):
        scores = []
        for episodeNumber in range(numberOfEpisodes):
            history = self.runEpisode(episodeNumber, scores)
        if config["visualize"]:
            self.drawer.visualizeGame(history)
        if config["displayResults"]:
            self.drawer.displayResults(scores)
        return scores[-1]

    def runEpisode(self, episodeNumber, scores):
        board, state, action, SAPpairs = self.initalizeEpisode()
        while not board.isInEndState():
            newState, reinforcement, score = board.move(action)
            newAction = self.chooseNextAction(board, action, newState)
            self.actor.updateEligibility(newState, newAction, isCurrentState=True)
            TDError = self.critic.getTDError(state, newState, reinforcement)
            self.critic.updateEligibility(newState, isCurrentState=True)

            if action:
                SAPpairs.append((state, action))

            for (s, a) in SAPpairs:
                self.critic.updateValueFunction(s, TDError)
                self.critic.updateEligibility(s)
                self.actor.updatePolicy(s, a, TDError)
                self.actor.updateEligibility(s, a)

            state, action = newState, newAction
        scores.append(score)
        SAPpairs.append((state, action))
        return SAPpairs

    def initalizeEpisode(self):
        board = Board(config["size"], config["boardType"], config["state"])
        state = board.bitString
        action = None
        SAPpairs = []
        return board, state, action, SAPpairs

    def chooseNextAction(self, board, action, newState):
        legalMoves = board.allLegalMoves()
        if board.isInEndState():
            newAction = action
        else:
            newAction = self.actor.chooseAction(newState, legalMoves)

        return newAction


agent = Agent()
agent.runEpisodes(config["episodesToRun"])

# for i in range(20):
#     agent = Agent()
#     print(agent.runEpisodes(config["episodesToRun"]))
