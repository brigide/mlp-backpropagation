from random import uniform

class Perceptron:
    """Single Perceptron class representation"""
    def __init__(self):
        """Constructor/Initialize weights randomly"""
        self.weights = [uniform(-1, 1) for x in range(2)]
        self.learning_rate = 0.1

    def get_output(self, inputs):
        """Sum inputs with weights and guesses an output"""
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i] * self.weights[i]

        return self.activation(sum)

    def activation(n):
        """activation function"""
        if n >= 0:
            return 1
        else:
            return -1
        
    def train(self, inputs, target):
        """adjust weights according to expected output"""
        result = self.get_output(inputs)
        error = target - result

        # correct all the weights
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * self.learning_rate
