import random
from time import process_time_ns
import copy

GAME_VALUES = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]

class Node:
    def __init__(self, num_weights):
        self.weights = [0.0] * num_weights

        for i in range(len(self.weights)):
            self.weights[i] = random.random()

        self.bias = random.random()

    def getWeights(self):
        return self.weights
    def getBias(self):
        return self.bias

    def setWeights(self, new_weights):
        for i in range(len(new_weights)):
            self.weights[i] = new_weights[i]

    def RELU(self, input):
        return max(0, input)

    def pass_through(self, inputs):
        output = 0
        for i in range(len(inputs)):
            output += (inputs[i] * self.weights[i])
        output += self.bias
        #pass all outputs through activation function

        return self.RELU(output)

class NeuralNetwork:
    def __init__(self, layout, input_size):
        self.layers = []
        self.NUM_INPUTS = input_size
        self.score = 0


        #for each layer establish all the nodes necessary
        for i in range(len(layout)):
            layer = []
            for j in range(layout[i]):
                if(i == 0):
                    layer.append(Node(self.NUM_INPUTS))
                else:
                    layer.append(Node(layout[i-1]))

            self.layers.append(layer)


    def process_inputs(self, inputs):
        new_inputs = []

        for val in inputs:
            new_inputs.append(GAME_VALUES.index(val) * .07)

        return new_inputs

    def replace_node(self, layer, node, new_node):
        self.layers[layer][node] = new_node

    def get_node(self, layer, node):
        return copy.deepcopy(self.layers[layer][node])

    def get_num_layers(self):
        return len(self.layers)
    
    def get_layer_size(self, layer):
        return len(self.layers[layer])

    def feed_forward(self, inputs):
        
        input = self.process_inputs(inputs)

        layer_results = []
        layer_results.append(input)

        for i in range(len(self.layers)):
            results = []
            for j in range(len(self.layers[i])):
                results.append(self.layers[i][j].pass_through(layer_results[i-1]))
            layer_results.append(results)

        return layer_results[len(layer_results) - 1]

    def print_network(self):
        i = 1
        print("Inputs: " + str(self.NUM_INPUTS))
        for j in range(len(self.layers) - 1):
            print("Layer " + str(i) + ": " + str(len(self.layers[j])))
            i += 1
        print("Outputs: " + str(len(self.layers[len(self.layers) - 1])))


