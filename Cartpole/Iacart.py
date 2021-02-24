import gym 
import random
import numpy as np 
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
"""env = gym.make('CartPole-v1')
env.reset()

for step_index in range(1000):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print(f"Step:{step_index}")
    print("action: {}".format(action))
    print("observation: {}".format(observation))
    print("reward: {}".format(reward))
    print("done: {}".format(done))
    print(f"info: {info}")
    print(info)
    if done: 
        break"""

env = gym.make('CartPole-v1')
env.reset()
goal_steps= 500
score_requirement = 60
initial_games = 1000

def model_data_preparation():
    training_data = []
    accepted_scores = []
    for game_index in range(initial_games):
        score = 0
        game_memory = []
        previous_observation = []
        for step_index in range(goal_steps):
            action = random.randrange(0, 2)
            observation, reward, done, info = env.step(action)

            if len(previous_observation) > 0:
                game_memory.append([previous_observation,action])

            previous_observation = observation

            score += reward

            if done: 
                break

        if score >= score_requirement:
            accepted_scores.append(score)
            for data in game_memory:
                if data[1] == 1:
                    output = [0,1]
                elif data[1] == 0:
                    output = [1,0]
                training_data.append([data[0],output])
        env.reset()
    print(accepted_scores)
    return training_data

