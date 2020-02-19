import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


class NeuralNet(nn.Module):
    def __init__(self, nodes, discountFactor=0.99):
        super(NeuralNet, self).__init__()
        self.layers = []
        self.discountFactor = discountFactor
        self.eligibilities = []
        for i in range(len(nodes) - 1):
            layer = nn.Linear(nodes[i], nodes[i + 1])
            reluLayer = nn.ReLU()
            eligibilityMatrix = torch.Tensor(nodes[i + 1], nodes[i])
            self.layers.append(layer)
            self.layers.append(reluLayer)
            self.eligibilities.append(eligibilityMatrix)
        outputLayer = nn.Linear(nodes[-1], 1)
        eligibilityMatrix = torch.Tensor(1, nodes[-1])
        self.eligibilities.append(eligibilityMatrix)
        self.layers.append(outputLayer)
        self.model = nn.Sequential(*self.layers)
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.01)

    def forward(self, state):
        x = torch.FloatTensor([int(x) for x in state])
        x = self.model(x)
        return x

    def criterion(self, state, newState, reinforcement):
        with torch.no_grad():
            return (
                reinforcement
                + self.discountFactor * self.forward(newState)
                - self.forward(state)
            )

    def train(self, state, TDError):
        self.optimizer.zero_grad()
        outputs = self.forward(state)
        outputs.backward()
        for i, layer in enumerate(
            list(filter(lambda layer: type(layer) == type(self.model[0]), self.model))
        ):
            self.eligibilities[i] += layer.weight.grad
            layer.weight.grad = -TDError * layer.weight.grad
        self.optimizer.step()

