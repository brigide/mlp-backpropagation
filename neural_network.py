from matrix import Matrix
import math

class NeuralNetwork:
    """Neural Network class"""
    def __init__(self, *arg):
        """Constructor accepts any number of arguments
            first argument being number of inputs
            middle arguments being hidden layers number of nodes,
            last being number of outputs"""
        if len(arg) <= 2:
            return 'at least 2 arguments are necessary'
        
        self.input_nodes = arg[1]
        self.output_nodes = arg[-1]

        self.hidden_nodes = [n for n in arg[1:-1]]
        self.hidden_layers = len(self.hidden_nodes)

        # input to first hidden
        self.weights_ih = Matrix(self.hidden_nodes[0], self.input_nodes)
        self.weights_ih.randomize()

        # hidden layers
        self.weights_h = [Matrix(self.hidden_nodes[i+1], self.hidden_nodes[i]) for i in range(self.hidden_layers)[:-1]]
        for w in self.weights_h: w.randomize()
        self.bias_h = [Matrix(self.hidden_nodes[i], 1) for i in range(self.hidden_layers)]
        for b in self.bias_h: b.randomize()

        # last hidden to output
        self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes[-1])
        self.weights_ho.randomize()
        self.bias_ho = Matrix(self.output_nodes, 1)
        self.bias_ho.randomize()

    def feed_forward(self, input_array):

        inputs = Matrix.from_array(input_array)

        inputs.log()
        self.weights_ih.log()

        # input to hidden
        first_hidden = Matrix.multiply_matrix(self.weights_ih, inputs)
        first_hidden.add(self.bias_h[0])

        first_hidden.map(NeuralNetwork.sigmoid) # activation function


        # hidden layers
        current_layer = first_hidden
        for i in range(self.hidden_layers)[1:]:
            next_layer = Matrix.multiply_matrix(self.weights_h[i], current_layer)
            next_layer.add(self.bias_h[i])
            next_layer.map(NeuralNetwork.sigmoid)
            current_layer = next_layer

        # last hidden to output
        output_layer = Matrix.multiply_matrix(self.weights_ho, current_layer)
        output_layer.add(self.bias_ho)

        output_layer.map(NeuralNetwork.sigmoid)

        return output_layer.to_array()


    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.e ** -x)
