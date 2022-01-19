from copy import deepcopy
from game import GameBoard
from ai import NeuralNetwork
from ai import Node
import random

network_layout = [16, 4]
sample_inputs = [2, 4, 8, 16, 512, 2, 4, 8, 16, 512, 2, 4, 8, 16, 512, 1024]
NUM_INPUTS = 16
sample_net = NeuralNetwork(network_layout, NUM_INPUTS)

def mutation(rate, the_network):
    for i in range(the_network.get_num_layers()):
        for j in range(the_network.get_layer_size(i)):
            
            new_node = the_network.get_node(i, j)
            node_weights = new_node.getWeights()

            if(random.random() <= rate):
                # print("Modifying")
                # print("i: " + str(i) + " j: " + str(j))
                for k in range(len(node_weights)):
                    node_weights[k] = node_weights[k] + ((random.random() - .5) / 4)
                new_node.setWeights(node_weights)
                the_network.replace_node(i, j, new_node)
    return the_network

def cross_breed(first_parent, second_parent):
        
    new_net = NeuralNetwork(network_layout, NUM_INPUTS)

    for i in range(new_net.get_num_layers()):
        for j in range(new_net.get_layer_size(i)):
            if(random.random() >= .5):
                new_net.replace_node(i, j, first_parent.get_node(i, j))
            else:
                new_net.replace_node(i, j, second_parent.get_node(i, j))
    
    return new_net


def play_turn(network, game):
    inputs = game.get_flat_board()
    output = network.feed_forward(inputs)
    move = output.index(max(output))
    if(move == 0):
        game.slideUp()
    elif(move == 1):
        game.slideRight()
    elif(move == 2):
        game.slideDown()
    elif(move == 3):
        game.slideLeft()

    return game.getScore()

def generate_generation(my_nets, scores):

    new_nets = []
    nets_to_gen = len(my_nets)
    avg_score = 0

    #top 10% will be copied
    for i in range(int(nets_to_gen * .2)):
        max_index = scores.index(max(scores))
        avg_score += scores[i]
        new_nets.append(deepcopy(my_nets[max_index]))
        my_nets.pop(max_index)
        scores.pop(max_index)

    print("Average Score of top 10%:" + str(avg_score/float(len(new_nets))))
    
    #next 60% will be bred
    for i in range(int(nets_to_gen * .7)):
        new_network = cross_breed(new_nets[random.randint(0, len(new_nets) - 1)], new_nets[random.randint(0, len(new_nets) - 1)])
        new_network = mutation(.1, new_network)
        new_nets.append(new_network)

    remaining = nets_to_gen - len(new_nets)
    for i in range(remaining):
        new_nets.append(NeuralNetwork(network_layout, NUM_INPUTS))

    return new_nets


networks = []
scores = []
games = []


num_moves = 1000
num_instances = 1000
num_generations = 100


for i in range(num_instances):
    networks.append(NeuralNetwork(network_layout, NUM_INPUTS))
    scores.append(0)
    games.append(GameBoard())

saved_scores = []
for x in range(num_generations):
    for i in range(num_moves):
        for j in range(num_instances):
            scores[j] = play_turn(networks[j], games[j])

    print("Generation " + str(x) + ": ", end="")
    
    print("\n-----------------------------")
    print("Top Gameboard")
    best_game = games[scores.index(max(scores))]
    best_game.displayBoard()

    saved_scores = deepcopy(scores)

    networks = generate_generation(networks, scores)
    scores = []
    games = []
    for i in range(len(networks)):
        scores.append(0)
        games.append(GameBoard())
        



print("Final Scores: ", end="")
print(saved_scores)