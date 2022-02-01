import gym
import pickle
from dqn_torch import Agent
import numpy as np
import time
from game import GameBoard

if __name__ == '__main__':
    env = gym.make('LunarLander-v2')
    new_game = GameBoard()
    agent = Agent(gamma=0.99, epsilon=1.0, batch_size=64, n_actions=4,
    eps_end=0.01, input_dims=[16], lr=0.0001)
    scores, eps_history = [], []
    n_games = 10000

    curr_max = 0
    curr_max_avg = 0

    for i in range(n_games):
        score = 0
        done = False
        obs = new_game.reset()
        while not done:
            action = agent.choose_action(obs)
            obs_, reward, done, info = new_game.step(action)
            score += reward
            agent.store_transition(obs, action, reward, obs_, done)
            agent.learn()
            obs = obs_
        
        if score > curr_max:
            print("Saving new Best")
            curr_max = score
            with open('best_max_agent.pkl', 'wb') as outp:
                pickle.dump(agent, outp, pickle.HIGHEST_PROTOCOL)
        


        scores.append(score)
        eps_history.append(agent.epsilon)
        avg_score = np.mean(scores[-100:])

        if avg_score > curr_max_avg and i > 100:
            print("Saving new Average")
            curr_max_avg = avg_score
            with open('best_avg_agent.pkl', 'wb') as outp:
                pickle.dump(agent, outp, pickle.HIGHEST_PROTOCOL)


        print('episode ', i, 'score %.2f' % score,
                'average score %.2f' % avg_score,
                'epsilon %.2f' % agent.epsilon)
        

with open('best_avg_agent.pkl', 'rb') as inp:
    max_agent = pickle.load(inp)
    fresh_game = GameBoard()
    done = False
    obs = fresh_game.reset()
    score = 0
    while not done:
        action = max_agent.choose_action(obs)
        obs_, reward, done, info = fresh_game.step(action)
        score += reward
        fresh_game.displayBoard()
        obs = obs_