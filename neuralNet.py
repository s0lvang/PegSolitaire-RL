import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


class NeuralNet(nn.Module):
    def __init__(self, nodes, discountFactor=0.5):
        super(NeuralNet, self).__init__()
        self.layers = []
        self.discountFactor = discountFactor
        for i in range(len(nodes) - 1):
            layer = nn.Linear(nodes[i], nodes[i + 1])
            self.layers.append(layer)
        outputLayer = nn.Linear(nodes[-1], 1)
        self.layers.append(outputLayer)
        self.model = nn.Sequential(*self.layers)
        self.optimizer = optim.RMSprop(self.model.parameters())

    def forward(self, state):
        x = torch.FloatTensor([int(x) for x in state])
        x = self.model(x)
        return x

    def criterion(self, state, newState, reinforcement):
        return (
            reinforcement
            + self.discountFactor * self.forward(newState)
            - self.forward(state)
        )

    def train(self, state, TDerror):
        self.optimizer.zero_grad()

        # forward + backward + optimize
        outputs = self.forward(state)
        loss = TDerror
        loss.backward(retain_graph=True) #Aner ikke hvorfor jeg har retain graph men det får da være
        self.optimizer.step()

