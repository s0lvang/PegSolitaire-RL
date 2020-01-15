from diamond import Diamond
from actor import Actor
from critic import Critic
from game import Game


class Agent():
    def __init__(self):
        self.actor = Actor()
        self.critic = Critic()
    
    
    def runEpisodes(self, numberOfEpisodes):
        for _ in range numberOfEpisodes:
            enviroment = Game() # new game ish don't know the interface excactly
            state = enviroment.getState() # the board represented in a bitstring maybe initalize as None
            action = None # No action should be done initially.
            SAPpairs = []
            while enviroment.endState == False:
                newState, reinforcement = enviroment.doAction(action) #I think the reinforcement should be the number of Pegs left if there is the endstate is reached. else 0
                legalActions = enviroment.getLegalActions() #I have not decided in which format the actions should be, I think they can be the state of the board after a given action.
                newAction = self.actor.getAction(newState, legalActions) # The article about reinforcement learning, just states that the actor chooses an action, but i think it should know which actions are legal. 
                self.actor.updateEligibility(newState, newAction) # This should update the eligibility of the SAP to 1, but that will be handled in the function
                TDError = self.critic.getTDError(state, newState, reinforcement)
                self.critic.updateEligibility(newState, isCurrentState=True) # Should be updated to 1
                SAPpairs.append((state, action))
                
                for SAP in SAPpairs:
                    s, a = SAP
                    self.critic.updateValueFunction(s, TDError) # updates the entry for s in the valuefunction
                    self.critic.updateEligibility(s) # should be Y * gamma * e(s)
                    self.actor.updatePolicy(s, a, TDError) # update the entry for the sap in the actor
                    self.actor.updateEligibility(s,a) # update the eligibility y * gamma * e(s,a)
                state, action = newState, newAction
