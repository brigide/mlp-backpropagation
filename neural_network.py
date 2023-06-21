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


        self.learning_rate = 0.1

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.e ** -x)
    
    @staticmethod
    def derivative_sigmoid(y):
        return y * (1 - y)
    

    def train(self, input_array, target_array):
        # get hidden outputs
        inputs = Matrix.from_array(input_array)
        targets = Matrix.from_array(target_array)
        hidden = Matrix.multiply_matrix(self.weights_ih, inputs)
        # activation funciton
        hidden.map(self.sigmoid)


        # get outputs
        outputs = Matrix.multiply_matrix(self.weights_ho, hidden)
        outputs.map(self.sigmoid)



        # get error
        # error = target - output
        output_errors = Matrix.subtract(targets, outputs)

        # get gradient
        # gradient = o * (1 - o)
        gradient = Matrix.static_map(outputs, NeuralNetwork.derivative_sigmoid)
        gradient.multiply_hamard(output_errors)
        gradient.multiply_scalar(self.learning_rate)

        # calculate deltas
        hidden_t = Matrix.transpose(hidden)
        delta_w_ho = Matrix.multiply_matrix(gradient, hidden_t)

        # adjust weights based on delta
        self.weights_ho.add(delta_w_ho)


        # now for hidden layer
        weight_ho_t = Matrix.transpose(self.weights_ho)
        hidden_errors = Matrix.multiply_matrix(weight_ho_t, output_errors)

        hidden_gradient = Matrix.static_map(hidden, NeuralNetwork.derivative_sigmoid)
        hidden_gradient.multiply_hamard(hidden_errors)
        hidden_gradient.multiply_scalar(self.learning_rate)

        input_t = Matrix.transpose(inputs)
        delta_w_ih = Matrix.multiply_matrix(hidden_gradient, input_t)

        self.weights_ih.add(delta_w_ih)