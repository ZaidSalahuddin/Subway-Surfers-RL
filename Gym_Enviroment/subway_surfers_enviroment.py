import gym
from gym import spaces

from Game_States.game_state_predictor import predict_state

class subwaySurfers(env):
    def __init__(self):
        #i honestly dont know what goes here
        self.action_space = gym.spaces.Discrete(5)
        self.observation_space = gym.spaces.Discrete(2)
        pass
    
    def step(self, action):
        #state is equal to screenshot
        #action come from the agent lol
        #reward increases for every step it survives
        #reward significantly decreases if the game ends

        #returns state, reward, done, info
        pass

    def move():
        pass

    def reset(self):
        #activates once run ends
        #check game state first
        #commit actions based off the game state to reset the game
        pass