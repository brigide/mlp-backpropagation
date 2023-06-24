from matrix import Matrix
import math

class NeuralNetwork:
    """Neural Network class"""
    def __init__(self, *arg):
        """Constructor accepts any number of arguments
            first argument being number of inputs
            middle arguments being hidden layers number of nodes,
            last being number of outputs"""
        if len(arg) < 2:
            return 'at least 2 arguments are necessary'
        
        self.input_nodes = arg[0]
        self.output_nodes = arg[-1]

        self.hidden_nodes = [n for n in arg[1:-1]]
        self.hidden_layers = len(self.hidden_nodes)

        # setup weights
        self.weights = []
        self.weights.append(Matrix(self.hidden_nodes[0], self.input_nodes))

        for i in range(self.hidden_layers - 1):
            self.weights.append(Matrix(self.hidden_nodes[i+1], self.hidden_nodes[i]))
                                
        self.weights.append(Matrix(self.output_nodes, self.hidden_nodes[-1]))   

        for w in self.weights:
            w.randomize()



        # setup biases
        self.biases = []
        self.biases.append(Matrix(self.hidden_nodes[0], 1))

        for i in range(self.hidden_layers - 1):
            self.biases.append(Matrix(self.hidden_nodes[i+1], 1))
                                
        self.biases.append(Matrix(self.output_nodes, 1))   

        for b in self.biases:
            b.randomize()

        self.learning_rate = 0.1

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.e ** -x)
    
    @staticmethod
    def derivative_sigmoid(y):
        return y * (1 - y)
    

    def predict(self, input_array):
        return self.feed_forward(input_array)[-1].to_array()


    def feed_forward(self, input_array):
        steps = []
        current_step = Matrix.from_array(input_array)
        steps.append(current_step)
        for i in range(len(self.weights)):
            current_step = Matrix.multiply_matrix(self.weights[i], current_step)
            current_step.add(self.biases[i])
            current_step.map(NeuralNetwork.sigmoid)
            steps.append(current_step)

        return steps

    def train(self, input_array, target_array):
        """Backpropagation algorithm"""
        steps = self.feed_forward(input_array)
        targets = Matrix.from_array(target_array)

        i = len(steps) - 1
        while i >= 1:
            # get error
            if i != len(steps) - 1:
                targets = Matrix.transpose(self.weights[i])
                errors = Matrix.multiply_matrix(targets, errors)
            else:
                errors = Matrix.subtract(targets, steps[i])

            # get gradient
            gradient = Matrix.static_map(steps[i], NeuralNetwork.derivative_sigmoid)

            # gradient.log()
            # errors.log()
            # targets.log()
        
            gradient.multiply_hamard(errors)
            gradient.multiply_scalar(self.learning_rate)

            # get deltas
            transposed = Matrix.transpose(steps[i - 1])
            delta = Matrix.multiply_matrix(gradient, transposed)

            # adjust weights
            self.weights[i - 1].add(delta)
            #self.biases[i - 1].add(gradient)

            i -= 1
